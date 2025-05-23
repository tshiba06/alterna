from sqlalchemy.orm import Session

from app.repositories.sbi_benefit_system.model import SbiBenefitSystem # Corrected import
from app.repositories.sbi_benefit_system.repository import Repository


class RepositoryMock(Repository):
    create_call_counts = 0
    create_call_args = []

    def create(self, session: Session, bank: SbiBenefitSystem):
        self.create_call_counts += 1
        self.create_call_args.append(bank)
