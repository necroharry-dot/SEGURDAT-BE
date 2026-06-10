from sqlalchemy import column, Integer, String, DateTime, ForeignKey
from src.models import Base, Session

class usuarios(Base):
    __tablename__ = 'usuarios'

    id_usuario = column(Integer, primary_key=True)
    nombre = column(String(255), nullable=False)
    apellido = column(String(255), nullable=False)
    documento_identidad = column(String(255), nullable=False)
    celular = column(String(255), nullable=False)
    fecha_nacimiento = column(DateTime, nullable=False)
    edad = column(Integer, nullable=False)
    direccion = column(String(255), nullable=False)
    fecha_ingreso = column(DateTime, nullable=False)
    eps = column(String(255), nullable=False)
    fondo_pension = column(String(255), nullable=False)
    id_cargo = column(Integer, ForeignKey('cargo.id_cargo'), nullable=False)
    usuario = column(String(255), nullable=False)
    correo_electronico = column(String(255), nullable=False)
    contrasena = column(String(255), nullable=False)

    def __init__(self, nombre, apellido, documento_identidad, celular, fecha_nacimiento, edad, direccion, fecha_ingreso, eps, fondo_pension, id_cargo, usuario, correo_electronico, contrasena):
        self.nombre = nombre
        self.apellido = apellido
        self.documento_identidad = documento_identidad
        self.celular = celular
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = edad
        self.direccion = direccion
        self.fecha_ingreso = fecha_ingreso
        self.eps = eps
        self.fondo_pension = fondo_pension
        self.id_cargo = id_cargo
        self.usuario = usuario
        self.correo_electronico = correo_electronico
        self.contrasena = contrasena

    def save(self):
        Session.add(self)
        Session.commit()

    def delete(self):   
        Session.delete(self)
        Session.commit()
    
    def get():
        usuarios = Session.query(usuarios).all()
        return usuarios
    
    def get_by_id(id_usuario):
        usuario = Session.query(usuarios).filter_by(id_usuario=id_usuario).first()
        return usuario