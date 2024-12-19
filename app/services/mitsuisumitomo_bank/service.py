import os
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from services.two_factor_scraping_service import TwoFactorService


class ServiceImpl(TwoFactorService):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def initial_run(self, driver: webdriver.Chrome) -> int:
        # initialize
        # TODO: これもmainで一度だけ
        load_dotenv()

        self.driver.get("https://direct.smbc.co.jp/aib/aibgsjsw5001.jsp")

        # サイトの表示に時間がかかるので待つ
        sleep(2)

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

        # TODO: websocketで双方向通信
        # 2段階認証があるものについてはそこだけ待つ必要がある
        # QRコードの画像を一度返す必要があるのでこれだけServiceのinterfaceを満たすことはできない
        # TwoFactorServiceというInterfaceを定義する
        # initial_run, second_runとかで後で命名は見直す
        # driverは同一にしないといけないはずなので、driverは外から注入する必要が最低限ありそう

        # driver.quit()


if __name__ == "__main__":
    service = ServiceImpl()
    amount = service.run()
    print(amount)
