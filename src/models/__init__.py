from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import pymysql


engine = create_engine("mysql+pymysql://root@localhost:3306/SEGURDAT?charset=utf8mb4")

connection = engine.connect()

Session = sessionmaker(bind=engine)

Session = Session()

Base = declarative_base()
Base.metadata.bind = engine

