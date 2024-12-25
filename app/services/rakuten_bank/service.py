import os

from dotenv import load_dotenv
from internal.log import logger
from selenium import webdriver
from selenium.common.exceptions import (
    ElementNotInteractableException,
    NoSuchElementException,
)
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from services.scraping_service import Service


class ServiceImpl(Service):
    def __init__(self):
        super().__init__()

    async def run(self) -> int:
        logger.info("run")
        # initialize
        # TODO: driverも外から渡す
        options = ChromeOptions()
        # options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
        logger.info("created webdriver")

        driver.get(
            "https://sfes.rakuten-bank.co.jp/MS/main/RbS?CID=M_START&CMD=LOGIN&l-id=smp_top_1214_45_CO800"
        )

        # サイトの表示に時間がかかるので待つ
        driver.implicitly_wait(2)

        id = os.getenv("RAKUTEN_BANK_ID")
        password = os.getenv("RAKUTEN_BANK_PASSWORD")
        branch_number = os.getenv("RAKUTEN_BRANCH_NUMBER")
        account_number = os.getenv("RAKUTEN_ACCOUNT_NUMBER")
        rakuten_secret1_question = os.getenv("RAKUTEN_SECRET1_QUESTION")
        rakuten_secret2_question = os.getenv("RAKUTEN_SECRET2_QUESTION")
        rakuten_secret3_question = os.getenv("RAKUTEN_SECRET3_QUESTION")
        rakuten_secret1_word = os.getenv("RAKUTEN_SECRET1_WORD")
        rakuten_secret2_word = os.getenv("RAKUTEN_SECRET2_WORD")
        rakuten_secret3_word = os.getenv("RAKUTEN_SECRET3_WORD")

        input_id = driver.find_element(By.XPATH, "//input[@placeholder='ユーザID']")
        input_id.send_keys(id)
        input_password = driver.find_element(
            By.XPATH, "//input[@placeholder='ログインパスワード（全桁）']"
        )
        input_password.send_keys(password)
        login_button = driver.find_element(By.XPATH, "//input[@value='ログイン']")
        login_button.click()

        driver.implicitly_wait(2)

        # 合言葉認証がある場合
        try:
            id = "j_id_1h:INPUT_BRANCH_CODE"
            # id = "INPUT_FORM:INPUT_BRANCH_CODE" # pattern1
            number = "j_id_1h:INPUT_ACCOUNT_NUMBER"
            # account_number = "INPUT_FORM:INPUT_ACCOUNT_NUMBER" # pattern1 これはID
            input_branch_code = driver.find_element(By.ID, id)
            select = Select(input_branch_code)
            # input_branch_code.send_keys(branch_number)
            select.select_by_value(branch_number)
            input_account_number = driver.find_element(By.NAME, number)
            input_account_number.send_keys(account_number)

            # 合言葉の分岐がある
            word = ""
            # question = driver.find_element(
            #     By.CLASS_NAME, "c00 margintop20 large marginleft20pc"
            # ) # pattern1
            questions = driver.find_elements(
                By.CLASS_NAME, "rf-form-label"
            )

            question = questions[2] # 最後の要素

            if rakuten_secret1_question in question.text:
                word = rakuten_secret1_word
            elif rakuten_secret2_question in question.text:
                word = rakuten_secret2_word
            elif rakuten_secret3_question in question.text:
                word = rakuten_secret3_word

            print("word", word)

            input_secret_word = driver.find_element(By.NAME, "j_id_1h:SECRET_WORD")
            # input_secret_word = driver.find_element(By.ID, "INPUT_FORM:SECRET_WORD")
            input_secret_word.send_keys(word)
            login_button = driver.find_element(By.ID, "j_id_7d")
            login_button.click()
        except ElementNotInteractableException as e:
            print(e)
            return -1
        except NoSuchElementException as e:
            print(e)
            print("合言葉なし")

        driver.implicitly_wait(2)

        total = driver.find_element(By.ID, "amount-displayed")
        amount = int("".join(char for char in total.text if char.isdigit()))

        driver.quit()

        return amount


if __name__ == "__main__":
    load_dotenv()
    s = ServiceImpl()
    amount = s.run()
    print(amount)
