from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from src.models import Base, Session    

class Tipo_Armamento(Base):
    __tablename__ = 'tipo_armamento'

    id_tipo_armamento = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    
    def __init__(self, nombre):
        self.nombre = nombre

    def save(self):
        Session.add(self)
        Session.commit()

    def delete(self):   
        Session.delete(self)
        Session.commit()

    def get():
        tipo_armamento = Session.query(tipo_armamento).all()
        return tipo_armamento
    
    def get_by_id(id_tipo_armamento):
        tipo_armamento = Session.query(tipo_armamento).filter_by(id_tipo_armamento=id_tipo_armamento).first()
        return tipo_armamento
    
