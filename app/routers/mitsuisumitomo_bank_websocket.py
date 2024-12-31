from fastapi import WebSocket
from selenium import webdriver
from use_cases.mitsuisumitomo_bank.use_case import UseCase

from routers.websocket_router import WebsocketRouter


class MitsuisumitomoBankWebsocketRouter(WebsocketRouter):
    def __init__(self, use_case: UseCase):
        super().__init__(prefix="/banks/mitsuisumitomo")
        self.use_case = use_case

    async def save(self, websocket: WebSocket):
        await websocket.accept()
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)

        try:
            img = await self.use_case.first_authentication(driver=driver)
            await websocket.send_text(img)
            while True:
                data = await websocket.receive_text()
                if data == "close":
                    await websocket.close()
                    driver.quit()
                    break
                elif data == "yes":
                    await self.use_case.second_authentication(driver=driver)
                    await websocket.send_text("finish")
                    await websocket.close()
                    driver.quit()
                    break
                else:
                    await websocket.close()
                    driver.quit()
                    break
        except Exception as e:
            print(e)
            await websocket.close()
            driver.quit()
