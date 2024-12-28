from datetime import datetime
from typing import List

from pydantic import BaseModel, RootModel


class GetHistoryOutput(BaseModel):
    created_at: datetime
    total: int

class GetHistoriesOutput(RootModel[List[GetHistoryOutput]]):
    pass
