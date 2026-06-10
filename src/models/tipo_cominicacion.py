from sqlalchemy import column, Integer, String, DateTime, ForeignKey
from src.models import Base, Session

class tipo_comunicacion(Base):
    __tablename__ = 'tipo_comunicacion'

    id_tipo_comunicacion = column(Integer, primary_key=True)
    nombre_Tcomunicacion = column(String(50), nullable=False)
    
    def __init__(self, nombre):
        self.nombre_Tcomunicacion = nombre

    def save(self):
        Session.add(self)
        Session.commit()

    def delete(self):   
        Session.delete(self)
        Session.commit()

    def get():
        tipo_comunicacion = Session.query(tipo_comunicacion).all()
        return tipo_comunicacion
    
    def get_by_id(id_tipo_comunicacion):
        tipo_comunicacion = Session.query(tipo_comunicacion).filter_by(id_tipo_comunicacion=id_tipo_comunicacion).first()
        return tipo_comunicacion