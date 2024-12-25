from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine(url="postgresql://root:password@localhost/alterna", echo=False)

session = Session(autocommit=False, autoflush=True, bind=engine)
