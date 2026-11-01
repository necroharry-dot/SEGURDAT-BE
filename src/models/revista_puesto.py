from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.exc import SQLAlchemyError
from src.models import Base, Session
from src.models.armamento import Armamento
from src.models.comunicacion import Comunicacion
from src.models.puesto import Puesto 
from src.models.usuarios import Usuarios

class Revista_puesto(Base):
    __tablename__ = 'revista_puesto'

    id_revista_puesto = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'), nullable=False)
    id_armamento = Column(Integer, ForeignKey("armamento.id_armamento"), nullable=False)
    id_comunicacion = Column(Integer, ForeignKey("comunicacion.id_comunicacion"), nullable=False)
    obervaciones = Column(String(255), nullable=True)
    recomendaciones = Column(String(255), nullable=True)
    novedades = Column(String(255), nullable=True)
    geolocalizacion = Column(String(255), nullable=True)
    id_puesto = Column(Integer, ForeignKey('puesto.id_puesto'), nullable=False)

    def __init__(
        self,
        id_usuario,
        id_armamento,id_tipo_comunicacion,obervaciones=None,
        recomendaciones=None,novedades=None,geolocalizacion=None,id_puesto=None
    ):
        self.id_usuario = id_usuario
        self.id_armamento = id_armamento
        self.id_tipo_comunicacion = id_tipo_comunicacion
        self.obervaciones = obervaciones
        self.recomendaciones = recomendaciones
        self.novedades = novedades
        self.geolocalizacion = geolocalizacion
        self.id_puesto = id_puesto

    def save(self):
        try:
            Session.add(self)
            Session.commit()
        except SQLAlchemyError:
            # deshace la transacción fallida para que la sesión siga funcionando
            Session.rollback()
            raise

    def delete(self):
        try:
            Session.delete(self)
            Session.commit()
        except SQLAlchemyError:
            Session.rollback()
            raise

    @staticmethod
    def get():
        return Session.query(Revista_puesto).all()

    @staticmethod
    def get_by_id(id_revista_puesto):
        return Session.query(Revista_puesto)\
            .filter_by(id_revista_puesto=id_revista_puesto)\
            .first()
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def paginate(page=1, per_page=5):
        total = (Session.query(func.count(Revista_puesto.id_revista_puesto)).scalar())
        revista_puesto = Session.query(Revista_puesto).offset((page - 1) * per_page).limit(per_page).all()
        return revista_puesto, total