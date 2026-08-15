from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine,func
from src.models import Base, Session
from src.models.tipo_armamento import Tipo_Armamento

class Armamento(Base):
    __tablename__ = 'armamento'

    id_armamento = Column(Integer, primary_key=True)
    numero_serial = Column(String(255), unique=True, nullable=False) 
    numero_salvo = Column(String(255), unique=True, nullable=False)
    fecha_vencimiento = Column(DateTime, nullable=False)
    estado = Column(String(255), nullable=False)
    calibre = Column(String(255), nullable=False)
    fabricante = Column(String(255), nullable=False)
    numero_cartuchos = Column(Integer, nullable=False)
    id_tipo_armamento = Column(Integer, ForeignKey('tipo_armamento.id_tipo_armamento'), nullable=False)


    def __init__(self, numero_serial, numero_salvo, 
                 fecha_vencimiento, estado, calibre, fabricante, 
                 numero_cartuchos, id_tipo_armamento):
        
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
    
    def get_by_numero_serial(numero_serial):
        return Session.query(Armamento).filter_by(numero_serial=numero_serial).first()
    
    def get_by_numero_salvo(numero_salvo):
        return Session.query(Armamento).filter_by(numero_salvo=numero_salvo).first()


    def get_by_numero_salvo(numero_salvo):
        return Session.query(Armamento).filter_by(numero_salvo=numero_salvo).first()
        
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def paginate(page=1, per_page=5):
        total = (Session.query(func.count(Armamento.id_armamento)).scalar())
        
        armamento = Session.query(Armamento).offset ((page - 1) * per_page).limit(per_page).all()
        return armamento, total