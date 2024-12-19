from repositories.mitsuisumitomo_bank.repository import Repository as MBRepository

from app.services.mitsuisumitomo_bank.service import Service as MBService


class UseCase:
    def __init__(self, mb_repository: MBRepository, mb_service: MBService):
        self.mb_repository = mb_repository
        self.mb_service = mb_service

    def save(self):
        amount = self.run()
        print(amount)


if __name__ == "__main__":
    u = UseCase()
    u.save()
