from sqlalchemy import Column, Integer, String, func
from werkzeug.security import generate_password_hash, check_password_hash
from src.models import Base, Session
from src.models.cargo import Cargo


class Usuarios_Log(Base):
    __tablename__ = 'usuarios_log'

    id_usuario_log = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    nombre = Column(String(100), nullable=False)
    cargo = Column(String(100), nullable=False, default='cargo')

    def __init__(self, email, password, nombre, cargo):
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.nombre = nombre
        self.cargo = cargo

    def verificar_password(self, password):
        return check_password_hash(self.password_hash, password)

    def save(self):
        Session.add(self)
        Session.commit()

    @staticmethod
    def get_by_email(email):
        return Session.query(Usuarios_Log).filter_by(email=email).first()

    @staticmethod
    def get_by_id(id_usuario_log):
        return Session.query(Usuarios_Log).filter_by(id_usuario_log=id_usuario_log).first()

    def to_dict(self):
        return {
            'id_usuario_log': self.id_usuario_log,
            'email': self.email,
            'nombre': self.nombre,
            'cargo': self.cargo
        }
    







