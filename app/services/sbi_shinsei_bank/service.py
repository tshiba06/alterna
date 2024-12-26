import os

from selenium import webdriver
from selenium.webdriver.common.by import By

from services.scraping_service import Service


class ServiceImpl(Service):
    def __init__(self):
        super().__init__()

    async def run(self) -> int:
        # initialize
        driver = webdriver.Chrome()

        driver.get(
            "https://bk.web.sbishinseibank.co.jp/SFC/apps/services/www/SFC/desktopbrowser/default/login?mode=1"
        )

        # サイトの表示に時間がかかるので待つ
        driver.implicitly_wait(3)

        id = os.getenv("SBI_SHINSEI_BANK_ID")
        password = os.getenv("SBI_SHINSEI_BANK_PASSWORD")

        # ログイン処理
        input_id = driver.find_element(By.NAME, "nationalId")
        input_id.send_keys(id)
        input_password = driver.find_element(By.NAME, "password")
        input_password.send_keys(password)
        login_button = driver.find_element(By.XPATH, "//button[@translate='btn_login']")
        login_button.click()
        # ページ遷移に時間がかかるので待つ

        # ログイン後ページ
        # 残高一覧をクリック
        balance_list = driver.find_element(By.XPATH, "//a[@ui-sref='top.account_info']")
        balance_list.click()
        # ページ遷移に時間がかかるので待つ

        # totalの金額を取得
        total = driver.find_element(By.XPATH, "//*[contains(@class, 'totalAmount') and contains(@class, 'accountInfo') and contains(@class, 'amounMoney') and contains(@class, 'ng-binding')]")
        # カンマ入りの数字だけ抜き出す
        amount = int("".join(char for char in total.text if char.isdigit()))

        driver.quit()

        return amount


if __name__ == "__main__":
    s = ServiceImpl()
    amount = s.run()
    print(amount)
