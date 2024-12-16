import os
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import (
    ElementNotInteractableException,
    NoSuchElementException,
)
from selenium.webdriver.common.by import By


def run() -> int:
    # initialize
    load_dotenv()
    # TODO: headless
    # TODO: 形が他も含めて同じなので、interfaceを定義してもよい
    driver = webdriver.Chrome()

    driver.get('https://site1.sbisec.co.jp/ETGate/?_ControlID=WPLEThmR001Control&_PageID=DefaultPID&_DataStoreID=DSWPLEThmR001Control&_ActionID=DefaultAID&getFlg=on')

    # サイトの表示に時間がかかるので待つ
    sleep(2)

    id = os.getenv('SBI_SECURITIES_ID')
    password = os.getenv('SBI_SECURITIES_PASSWORD')

    input_id = driver.find_element(By.NAME, "user_id")
    input_id.send_keys(id)
    input_password = driver.find_element(By.NAME, "user_password")
    input_password.send_keys(password)
    login_button = driver.find_element(By.NAME, "ACT_login")
    login_button.click()


    sleep(2)
    try:
        input_device_code = driver.find_element(By.NAME, "device_code")
        device_code = input('デバイス認証コード >> ')
        input_device_code.send_keys(device_code)
        login_button = driver.find_element(By.NAME, "ACT_deviceauth")
        login_button.click()
    except ElementNotInteractableException:
        print('not clicked')
    except NoSuchElementException:
        print('no secret page')

    sleep(10)

    account_management = driver.find_element(By.XPATH, "//a[img[@title='口座管理']]")
    account_management.click()

    total = driver.find_elements(By.XPATH, "//tr[@bgcolor='#e6e5ff']//b")
    total_digit = total[1] # 0には計という文字が入っている
    amount = int(''.join(char for char in total_digit.text if char.isdigit()))

    driver.quit()

    return amount

if __name__ == '__main__':
    amount = run()
    print(amount)
