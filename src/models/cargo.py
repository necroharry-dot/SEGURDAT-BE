from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from src.models import Base, Session

class Cargo(Base):
    __tablename__ = 'cargo'

    id_cargo = Column(Integer, primary_key=True)
    nombre_cargo = Column(String(255), nullable=False)

    def __init__(self, nombre_cargo):
        self.nombre_cargo = nombre_cargo

    def save(self):
        Session.add(self)
        Session.commit()

    def delete(self):   
        Session.delete(self)
        Session.commit()
    
    def get():
        cargo = Session.query(cargo).all()
        return cargo
    
    def get_by_id(id_cargo):
        cargo = Session.query(cargo).filter_by(id_cargo=id_cargo).first()
        return cargo