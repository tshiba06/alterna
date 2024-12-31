from fastapi import APIRouter, WebSocket


class WebsocketRouter:
    def __init__(self, prefix: str):
        self.router = APIRouter(prefix=prefix)
        self._setup_routers()

    def _setup_routers(self):
        self.router.add_websocket_route("/", self.save)

    async def save(self, websocket: WebSocket):
        raise NotImplementedError("Should be implemented")
