from sqlalchemy import column, Integer, String, DateTime, ForeignKey, create_engine
from src.models import Base, Session

class comunicacion(Base):
    __tablename__ = 'comunicacion'

    id_comunicacion = column(Integer, primary_key=True)
    id_tipo_comunicacion = column(Integer, ForeignKey('tipo_comunicacion.id_tipo_comunicacion'), nullable=False)
    numero_serial = column(String(255), nullable=False) 
    modelo = column(String(255), nullable=False)
    imei = column(String(255), nullable=False)
    estado = column(String(255), nullable=False)
    fabricante = column(String(255), nullable=False)
    simcard = column(String(255), nullable=False)

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
        comunicacion = Session.query(comunicacion).all()
        return comunicacion
    
    def get_by_id(id_comunicacion):
        comunicacion = Session.query(comunicacion).filter_by(id_comunicacion=id_comunicacion).first()
        return comunicacion