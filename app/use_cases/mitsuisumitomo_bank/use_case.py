from repositories.mitsuisumitomo_bank.repository import Repository


class UseCase:
    def __init__(self, mitsuisumitomo_bank_repository: Repository):
        self.mitsuisumitomo_bank_repository = mitsuisumitomo_bank_repository
