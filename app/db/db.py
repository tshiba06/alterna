from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine(
    "TODO: データベースURLの設定",
    encoding="utf-8",
    echo=False
)

session = Session(
    autocommit = False,
    autoflush = True,
    bind = engine
)
