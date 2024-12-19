import os
from abc import ABC, abstractmethod
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from services.scraping_service import Service


class ServiceImpl(Service):
    def __init__(self):
        super().__init__()

    def run() -> int:
        # initialize
        load_dotenv()
        driver = webdriver.Chrome()

        driver.get("https://direct.smbc.co.jp/aib/aibgsjsw5001.jsp")

        # サイトの表示に時間がかかるので待つ
        sleep(2)

        branch_number = os.getenv("MITSUISUMITOMO_BANK_BRANCH_NUMBER")
        account_number = os.getenv("MITSUISUMITOMO_BANK_ACCOUNT_NUMBER")
        password = os.getenv("MITSUISUMITOMO_BANK_PASSWORD")

        input_branch_number = driver.find_element(By.NAME, "branchNo")
        input_branch_number.send_keys(branch_number)
        input_account_number = driver.find_element(By.NAME, "accountNo")
        input_account_number.send_keys(account_number)
        input_password = driver.find_element(By.ID, "inputpassword")
        input_password.send_keys(password)
        login_button = driver.find_element(By.CLASS_NAME, "js-login-submit")
        login_button.click()

        # これに関してはqrコードで認証が必要なので、厳しい可能性がある
        # 考え方
        # 楽天家計簿アプリにすべての情報を食わせて足りないsbiのものだけ取ってくるとかでもいいのかもしれない
        # いったん自分で開発するという現状の方向性でどうやって解決するか考える
        sleep(2)

        driver.quit()


if __name__ == "__main__":
    service = ServiceImpl()
    amount = service.run()
    print(amount)
