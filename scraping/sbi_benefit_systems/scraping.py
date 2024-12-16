import os
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By


def run() -> int:
    # initialize
    load_dotenv()
    driver = webdriver.Chrome()

    driver.get('https://www.benefit401k.com/customer/RkDCMember/Common/JP_D_BFKLogin.aspx')

    # サイトの表示に時間がかかるので待つ
    sleep(2)

    id = os.getenv('SBI_BENEFIT_SYSTEMS_ID')
    password = os.getenv('SBI_BENEFIT_SYSTEMS_PASSWORD')

    input_id = driver.find_element(By.NAME, "txtUserID")
    input_id.send_keys(id)
    input_password = driver.find_element(By.NAME, "txtPassword")
    input_password.send_keys(password)
    login_button = driver.find_element(By.ID, "btnLogin")
    login_button.click()

    sleep(2)

    # パスワード変更ページをスキップする
    confirm_button = driver.find_element(By.ID, "btnHome")
    confirm_button.click()

    sleep(2)

    total = driver.find_element(By.ID, "D_Header1_lblKojinBalanceAssets")
    amount = int(''.join(char for char in total.text if char.isdigit()))

    driver.quit()

    return amount

if __name__ == '__main__':
    amount = run()
    print(amount)
