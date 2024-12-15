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
    driver = webdriver.Chrome()

    driver.get('https://sfes.rakuten-bank.co.jp/MS/main/RbS?CID=M_START&CMD=LOGIN&l-id=smp_top_1214_45_CO800')

    # サイトの表示に時間がかかるので待つ
    sleep(2)

    id = os.getenv('RAKUTEN_BANK_ID')
    password = os.getenv('RAKUTEN_BANK_PASSWORD')
    branch_number = os.getenv('RAKUTEN_BRANCH_NUMBER')
    account_number = os.getenv('RAKUTEN_ACCOUNT_NUMBER')
    rakuten_secret1_question = os.getenv('RAKUTEN_SECRET1_QUESTION')
    rakuten_secret2_question = os.getenv('RAKUTEN_SECRET2_QUESTION')
    rakuten_secret3_question = os.getenv('RAKUTEN_SECRET3_QUESTION')
    rakuten_secret1_word = os.getenv('RAKUTEN_SECRET1_WORD')
    rakuten_secret2_word = os.getenv('RAKUTEN_SECRET2_WORD')
    rakuten_secret3_word = os.getenv('RAKUTEN_SECRET3_WORD')


    input_id = driver.find_element(By.XPATH, "//input[@placeholder='ユーザID']")
    input_id.send_keys(id)
    input_password = driver.find_element(By.XPATH, "//input[@placeholder='ログインパスワード（全桁）']")
    input_password.send_keys(password)
    login_button = driver.find_element(By.XPATH, "//input[@value='ログイン']")
    login_button.click()

    sleep(2)

    # 合言葉認証がある場合
    try:
        input_branch_code = driver.find_element(By.ID, "INPUT_FORM:INPUT_BRANCH_CODE")
        input_branch_code.send_keys(branch_number)
        input_account_number = driver.find_element(By.ID, "INPUT_FORM:INPUT_ACCOUNT_NUMBER")
        input_account_number.send_keys(account_number)

    # 合言葉の分岐がある
        word = ''
        question = driver.find_element(By.CLASS_NAME, "c00 margintop20 large marginleft20pc")
        if question.text == rakuten_secret1_question:
            word = rakuten_secret1_word
        elif question.text == rakuten_secret2_question:
            word = rakuten_secret2_word
        elif question.text == rakuten_secret3_question:
            word = rakuten_secret3_word

        input_secret_word = driver.find_element(By.ID, "INPUT_FORM:SECRET_WORD")
        input_secret_word.send_keys(word)
        login_button = driver.find_element()
        login_button.click()
    except ElementNotInteractableException:
        print('not clicked')
    except NoSuchElementException:
        print('no secret page')

    sleep(2)

    total = driver.find_element(By.ID, "amount-displayed")
    amount = int(''.join(char for char in total.text if char.isdigit()))

    driver.quit()

    return amount


if __name__ == '__main__':
    amount = run()
    print(amount)
