from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from src.models import Base, Session
from src.models.Tipo_de_comunicacion import Tipo_Comunicacion

class Comunicacion(Base):
    __tablename__ = 'comunicacion'

    id_comunicacion = Column(Integer, primary_key=True)
    id_tipo_comunicacion = Column(Integer, ForeignKey('tipo_comunicacion.id_tipo_comunicacion'), nullable=False)
    numero_serial = Column(String(255), nullable=False) 
    modelo = Column(String(255), nullable=False)
    imei = Column(String(255), nullable=False)
    estado = Column(String(255), nullable=False)
    fabricante = Column(String(255), nullable=False)
    simcard = Column(String(255), nullable=False)

    def __init__(self, id_tipo_comunicacion, numero_serial, modelo, imei, estado, fabricante, simcard):
        self.id_tipo_comunicacion = id_tipo_comunicacion
        self.numero_serial = numero_serial
        self.modelo = modelo
        self.imei = imei
        self.estado = estado
        self.fabricante = fabricante
        self.simcard = simcard

    def save(self):
        Session.add(self)
        Session.commit()

    def delete(self):   
        Session.delete(self)
        Session.commit()
    
    def get():
        comunicacion = Session.query(Comunicacion).all()
        return comunicacion
    
    def get_by_id(id_comunicacion):
        comunicacion = Session.query(Comunicacion).filter_by(id_comunicacion=id_comunicacion).first()
        return comunicacion
    
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}    