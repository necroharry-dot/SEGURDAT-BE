#liberias de importacion framework
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import pymysql




#controlador encargado de la conexion a la base de datos

connection = engine.connect()

Session = sessionmaker(bind=engine)

Session = Session()

# esta sentencia nos ayudara a crear la base de datos si no existe 
Base = declarative_base()
Base.metadata.bind = engine

