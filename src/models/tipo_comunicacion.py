from sqlalchemy import Column, Integer, String, func
from sqlalchemy.exc import IntegrityError
from src.models import Base, Session

class Tipo_Comunicacion(Base):
    __tablename__ = 'tipo_comunicacion'

    id_tipo_comunicacion = Column(Integer, primary_key=True)
    nombre_Tcomunicacion = Column(String(50), unique=True, nullable=False)

    def __init__(self, nombre):
        self.nombre_Tcomunicacion = nombre

    def save(self):
        try:
            Session.add(self)
            Session.commit()
        except IntegrityError:
            Session.rollback()
            raise

    def delete(self):
        try:
            Session.delete(self)
            Session.commit()
        except IntegrityError:
            Session.rollback()
            raise

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

    @staticmethod
    def paginate(page=1, per_page=5):
        total = (Session.query(func.count(Tipo_Comunicacion.id_tipo_comunicacion)).scalar())
        tipo_comunicacion = Session.query(Tipo_Comunicacion).offset((page - 1) * per_page).limit(per_page).all()
        return tipo_comunicacion, total
        