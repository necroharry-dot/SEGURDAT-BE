from sqlalchemy import Column, Integer, String
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

    @staticmethod
    def get():
        return Session.query(Tipo_Armamento).all()

    @staticmethod
    def get_by_id(id_tipo_armamento):
        return Session.query(Tipo_Armamento)\
            .filter_by(id_tipo_armamento=id_tipo_armamento)\
            .first()
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}