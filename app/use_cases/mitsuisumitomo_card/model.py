from datetime import datetime

from pydantic import BaseModel, ConfigDict


class GetHistoryOutput(BaseModel):
    total: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class GetHistoriesOutput(BaseModel):
    histories: list[GetHistoryOutput]
