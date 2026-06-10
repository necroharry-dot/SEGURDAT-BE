from sqlalchemy import column, Integer, String, DateTime, ForeignKey, create_engine
from src.models import Base, Session

class Armamento(Base):
    __tablename__ = 'armamento'

    id_armamento = column(Integer, primary_key=True)
    tipo_armamento = column(String(255), nullable=False)
    numero_serial = column(String(255), nullable=False) 
    numero_salvo = column(String(255), nullable=False)
    fecha_vencimiento = column(DateTime, nullable=False)
    estado = column(String(255), nullable=False)
    calibre = column(String(255), nullable=False)
    fabricante = column(String(255), nullable=False)
    numero_cartuchos = column(Integer, nullable=False)
    id_tipo_armamento = column(Integer, ForeignKey('tipo_armamento.id_tipo_armamento'), nullable=False)


    def __init__(self, tipo_armamento, numero_serial, numero_salvo, 
                 fecha_vencimiento, estado, calibre, fabricante, 
                 numero_cartuchos, id_tipo_armamento):
        
        self.tipo_armamento = tipo_armamento
        self.numero_serial = numero_serial
        self.numero_salvo = numero_salvo
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado
        self.calibre = calibre
        self.fabricante = fabricante
        self.numero_cartuchos = numero_cartuchos
        self.id_tipo_armamento = id_tipo_armamento 

    def save(self):
        Session.add(self)
        Session.commit()

    def delete(self):   
        Session.delete(self)
        Session.commit()
    
    def get():
        armamento = Session.query(Armamento).all()
        return armamento
    
    def get_by_id(id_armamento):
        armamento = Session.query(Armamento).filter_by(id_armamento=id_armamento).first()
        return armamento