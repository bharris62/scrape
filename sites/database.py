from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
import config

engine = create_engine(config.postgres_url)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    product_dealer = Column(String)
    product_name = Column(String)
    product_url = Column(String)
    product_price = Column(String)
    product_price_per_serving = Column(String)
    product_type = Column(String)
    product_image = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)