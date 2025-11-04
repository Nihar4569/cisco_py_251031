from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from employee import Base

engine = create_engine("sqlite:///employees.db")

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)