from sqlalchemy import Column, Integer, String
from src.models import Base, Session

class Tipo_Comunicacion(Base):
    __tablename__ = 'tipo_comunicacion'

    id_tipo_comunicacion = Column(Integer, primary_key=True)
    nombre_Tcomunicacion = Column(String(50), nullable=False)

    def __init__(self, nombre):
        self.nombre_Tcomunicacion = nombre

    def save(self):
        Session.add(self)
        Session.commit()

    def delete(self):
        Session.delete(self)
        Session.commit()

    @staticmethod
    def get():
        return Session.query(Tipo_Comunicacion).all()

    @staticmethod
    def get_by_id(id_tipo_comunicacion):
        return Session.query(Tipo_Comunicacion)\
            .filter_by(id_tipo_comunicacion=id_tipo_comunicacion)\
            .first()

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}