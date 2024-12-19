from fastapi import APIRouter


class Router:
    def __init__(self, prefix: str):
        self.router = APIRouter(prefix=prefix)
        self._setup_routers()

    def _setup_routers(self):
        self.router.add_api_route("/", self.get_latest, methods=["GET"])
        self.router.add_api_route("/", self.save, methods=["POST"])
        self.router.add_api_route("/histories", self.get_history, methods=["GET"])

    async def get_latest(self):
        raise NotImplementedError("Should be implemented")

    async def save(self):
        raise NotImplementedError("Should be implemented")

    async def get_history(self):
        raise NotImplementedError("Should be implemented")
