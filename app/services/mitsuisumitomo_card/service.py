import sys # Added for sys.path modification
import os
# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
import asyncio # Added for async execution
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions # Added import
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.services.scraping_service import Service # Modified import


class ServiceImpl(Service):
    def __init__(self):
        super().__init__()

    async def run(self) -> int: # Added self to signature
        # initialize
        load_dotenv() # This should ideally be outside run if service is instantiated multiple times
        
        options = ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)

        driver.get("https://www.smbc-card.com/mem/index.jsp")

        # Wait for the ID input field to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "id_input"))
        )

        id = os.getenv("MITSUISUMITOMO_CARD_ID")
        password = os.getenv("MITSUISUMITOMO_CARD_PASSWORD")

        input_id = driver.find_element(By.ID, "id_input")
        input_id.send_keys(id)
        input_password = driver.find_element(By.ID, "pw_input")
        input_password.send_keys(password)

        # Wait for the login button to be clickable
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btnNormal"))
        )
        try:
            login_button.click()
        except Exception as e:
            print(f"Standard click failed: {e}. Trying JavaScript click.")
            driver.execute_script("arguments[0].click();", login_button)

        # Wait for the detail button to be clickable
        detail_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "vp-view-WebApiId_U000100_9"))
        )
        detail_button.click()

        # Wait for the total amount element to be visible
        total = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "vp_alcor_view_Label_9"))
        )
        amount_text = total.text
        amount = int("".join(char for char in amount_text if char.isdigit()))

        driver.quit()

        return amount


if __name__ == "__main__":
    s = ServiceImpl()
    # amount = s.run() # Old synchronous call
    amount = asyncio.run(s.run()) # New asynchronous call
    print(amount)
