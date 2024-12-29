import os

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

from services.scraping_service import Service


class ServiceImpl(Service):
    def __init__(self):
        super().__init__()

    async def run(self) -> int:
        # initialize
        options = ChromeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)

        driver.get(
            "https://www.benefit401k.com/customer/RkDCMember/Common/JP_D_BFKLogin.aspx"
        )

        # サイトの表示に時間がかかるので待つ
        driver.implicitly_wait(10)

        id = os.getenv("SBI_BENEFIT_SYSTEMS_ID")
        password = os.getenv("SBI_BENEFIT_SYSTEMS_PASSWORD")

        input_id = driver.find_element(By.NAME, "txtUserID")
        input_id.send_keys(id)
        input_password = driver.find_element(By.NAME, "txtPassword")
        input_password.send_keys(password)
        login_button = driver.find_element(By.ID, "btnLogin")
        login_button.click()

        # パスワード変更ページをスキップする
        confirm_button = driver.find_element(By.ID, "btnHome")
        confirm_button.click()

        total = driver.find_element(By.ID, "D_Header1_lblKojinBalanceAssets")
        amount = int("".join(char for char in total.text if char.isdigit()))

        driver.quit()

        return amount


if __name__ == "__main__":
    s = ServiceImpl()
    amount = s.run()
    print(amount)
