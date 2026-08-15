from sqlalchemy import Column, Integer, String, DateTime, ForeignKey,func
from sqlalchemy.exc import IntegrityError
from src.models import Base, Session

class Cargo(Base):
    __tablename__ = 'cargo'

    id_cargo = Column(Integer, primary_key=True)
    nombre_cargo = Column(String(255), unique=True, nullable=False)

    def __init__(self, nombre_cargo):
        self.nombre_cargo = nombre_cargo

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
        except Exception:
            Session.rollback()
            raise

    @staticmethod
    def get():
        return Session.query(Cargo).all()

    @staticmethod
    def get_by_id(id_cargo):
        return Session.query(Cargo).filter_by(id_cargo=id_cargo).first()

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def paginate(page=1, per_page=5):
        total = (Session.query(func.count(Cargo.id_cargo)).scalar())

        cargos = Session.query(Cargo).offset((page - 1) * per_page).limit(per_page).all()
        return cargos, total
    