from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(500))
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    tags = Column(String(255))  # e.g., comma-separated tags

    def __repr__(self):
        return (f"[id={self.id}, name={self.name}, description={self.description}, price={self.price}, "
                f"stock={self.stock}, tags={self.tags}]")
