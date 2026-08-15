from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from src.models import Base, Session
from src.models.cargo import Cargo


class Usuarios(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    documento_identidad = Column(String(255), unique=True, nullable=False)
    celular = Column(String(255), nullable=False)
    fecha_nacimiento = Column(DateTime, nullable=False)
    edad = Column(Integer, nullable=False)
    direccion = Column(String(255), nullable=False)
    fecha_ingreso = Column(DateTime, nullable=False)
    eps = Column(String(255), nullable=False)
    fondo_pension = Column(String(255), nullable=False)
    id_cargo = Column(Integer, ForeignKey('cargo.id_cargo'), nullable=False)
    correo_electronico = Column(String(255),unique=True, nullable=False)


    def __init__(self, nombre, documento_identidad, celular, 
                 fecha_nacimiento, edad, direccion, fecha_ingreso, 
                 eps, fondo_pension, id_cargo, correo_electronico):
        self.nombre = nombre
        self.documento_identidad = documento_identidad
        self.celular = celular
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = edad
        self.direccion = direccion
        self.fecha_ingreso = fecha_ingreso
        self.eps = eps
        self.fondo_pension = fondo_pension
        self.id_cargo = id_cargo
        self.correo_electronico = correo_electronico


    def save(self):
        Session.add(self)
        Session.commit()

    def delete(self):   
        Session.delete(self)
        Session.commit()
    
    def get():
        usuarios = Session.query(Usuarios).all()
        return usuarios
    
    def get_by_id(id_usuario):
        usuario = Session.query(Usuarios).filter_by(id_usuario=id_usuario).first()
        return usuario
    
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def paginate(page=1, per_page=5):
        total = (Session.query(func.count(Usuarios.id_usuario)).scalar())

        usuarios = Session.query(Usuarios).offset((page - 1) * per_page).limit(per_page).all()
        return usuarios, total