import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from services.two_factor_scraping_service import TwoFactorService


class ServiceImpl(TwoFactorService):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def initial_run(self) -> str | None:
        self.driver.get("https://direct.smbc.co.jp/aib/aibgsjsw5001.jsp")

        # TODO: getenvはすべて外で行って関数の引数として渡す
        branch_number = os.getenv("MITSUISUMITOMO_BANK_BRANCH_NUMBER")
        account_number = os.getenv("MITSUISUMITOMO_BANK_ACCOUNT_NUMBER")
        password = os.getenv("MITSUISUMITOMO_BANK_PASSWORD")

        input_branch_number = self.driver.find_element(By.NAME, "branchNo")
        input_branch_number.send_keys(branch_number)
        input_account_number = self.driver.find_element(By.NAME, "accountNo")
        input_account_number.send_keys(account_number)
        input_password = self.driver.find_element(By.ID, "inputpassword")
        input_password.send_keys(password)
        login_button = self.driver.find_element(By.CLASS_NAME, "js-login-submit")
        login_button.click()

        qr_container = self.driver.find_element(By.CLASS_NAME, "js-qrCode")
        qr_code = qr_container.find_element(By.TAG_NAME, "img")
        img = qr_code.get_attribute("src")

        return img

    def second_run(self) -> int:
        accept_button = self.driver.find_element(By.CLASS_NAME, "js-btnEvent")
        accept_button.click()

        link_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='main-area']/div/section/div[5]/div/ul/li[1]/a"))
        )
        link_element.click()


        total = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "price"))
        )

        amount = int(total.text.replace(",", ""))

        print(amount)

        return amount


if __name__ == "__main__":
    driver = webdriver.Chrome()
    service = ServiceImpl(driver=driver)
    img = service.initial_run()
    print(img)
    input("Press Enter to continue...")
    amount = service.second_run()
    print(amount)
