import os
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By


def run() -> int:
    # initialize
    load_dotenv()
    driver = webdriver.Chrome()

    driver.get('https://www.smbc-card.com/mem/index.jsp')

    # サイトの表示に時間がかかるので待つ
    sleep(2)

    id = os.getenv('MITSUISUMITOMO_CARD_ID')
    password = os.getenv('MITSUISUMITOMO_CARD_PASSWORD')

    input_id = driver.find_element(By.ID, "id_input")
    input_id.send_keys(id)
    sleep(1)
    input_password = driver.find_element(By.ID, "pw_input")
    input_password.send_keys(password)
    sleep(1)

    # TODO: clickができていないのか動かない
    login_button = driver.find_element(By.CLASS_NAME, "btnNormal")
    login_button.click()

    sleep(2)

    detail_button = driver.find_element(By.ID, "vp-view-WebApiId_U000100_9")
    detail_button.click()

    sleep(2)

    total = driver.find_element(By.ID, "vp_alcor_view_Label_9")
    amount = int(''.join(char for char in total.text if char.isdigit()))

    driver.quit()

    return amount

if __name__ == '__main__':
    amount = run()
    print(amount)
