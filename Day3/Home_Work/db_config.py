from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from product import Base

engine = create_engine("sqlite:///products.db")
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
