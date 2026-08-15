from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.exc import SQLAlchemyError
from src.models import Base, Session


class Puesto(Base):
    __tablename__ = 'puesto'

    id_puesto = Column(Integer, primary_key=True)
    nombre_puesto = Column(String(255), nullable=False)
    direccion_puesto = Column(String(255), nullable=True)
    encargado_puesto = Column(String(255), nullable=True)
    numero_encargado = Column(String(255), nullable=True)
    nit_puesto = Column(String(255), unique=True, nullable=True)
    email_puesto = Column(String(255), nullable=True)
    descripcion_puesto = Column(String(255), nullable=True)
    georef_puesto = Column(String(255), nullable=True)
    id_armamento_puesto = Column(Integer, ForeignKey('armamento.id_armamento'), nullable=True)
    id_comunicacion = Column(Integer, ForeignKey('comunicacion.id_comunicacion'), nullable=True)

    def __init__(self, nombre_puesto, direccion_puesto=None, encargado_puesto=None,
                numero_encargado=None, nit_puesto=None, email_puesto=None,
                descripcion_puesto=None, georef_puesto=None, id_armamento_puesto=None):
        self.nombre_puesto = nombre_puesto
        self.direccion_puesto = direccion_puesto
        self.encargado_puesto = encargado_puesto
        self.numero_encargado = numero_encargado
        self.nit_puesto = nit_puesto
        self.email_puesto = email_puesto
        self.descripcion_puesto = descripcion_puesto
        self.georef_puesto = georef_puesto
        self.id_armamento_puesto = id_armamento_puesto

    def save(self):
        try:
            Session.add(self)
            Session.commit()
        except SQLAlchemyError:
            Session.rollback()
            raise

    def delete(self):
        try:
            Session.delete(self)
            Session.commit()
        except SQLAlchemyError:
            Session.rollback()
            raise
            
    def get():
        puesto = Session.query(Puesto).all()
        return puesto

    def get_by_id(id_puesto):
        puesto = Session.query(Puesto).filter_by(id_puesto=id_puesto).first()
        return puesto

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def paginate(page=1, per_page=5):
        total = (Session.query(func.count(Puesto.id_puesto)).scalar())
        puestos = Session.query(Puesto).offset((page - 1) * per_page).limit(per_page).all()
        return puestos, total
