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
        # options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)

        driver.get(
            "https://www.netbk.co.jp/contents/pages/wpl010101/i010101CT/DI01010210"
        )

        # sleep
        driver.implicitly_wait(3)

        user_name = os.getenv("SUMISHIN_SBI_BANK_USER_NAME")
        password = os.getenv("SUMISHIN_SBI_BANK_PASSWORD")

        # ログイン処理
        input_user_name = driver.find_element(By.NAME, "userNameNewLogin")
        input_user_name.send_keys(user_name)
        input_password = driver.find_element(By.ID, "loginPwdSet")
        input_password.send_keys(password)
        login_button = driver.find_element(By.XPATH, "//button[@data-js='login']")
        login_button.click()

        # 口座一覧をクリック
        balance_button = driver.find_element(By.CLASS_NAME, "m-icon-ps_balance")
        balance_button.click()

        total = driver.find_element(By.CLASS_NAME, "m-hdr-bankAc-money")
        amount = int("".join(char for char in total.text if char.isdigit()))

        driver.quit()

        return amount


if __name__ == "__main__":
    s = ServiceImpl()
    amount = s.run()
    print(amount)
