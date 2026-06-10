from sqlalchemy import column, Integer, String, DateTime, ForeignKey
from src.models import Base, Session

class revista_puesto(Base):
    __tablename__ = 'revista_puesto'

    id_revista_puesto = column(Integer, primary_key=True)
    id_usuario = column(Integer, Integer, ForeignKey('usuario.id_usuario'), nullable=False)
    id_tipo_armamento = column(Integer, ForeignKey('tipo_armamento.id_tipo_armamento'), nullable=False)
    id_tipo_comunicacion = column(Integer, ForeignKey('tipo_comunicacion.id_tipo_comunicacion'), nullable=False)
    obervaciones = column(String(255), nullable=True)
    recomendaciones = column(String(255), nullable=True)
    novedades = column(String(255), nullable=True)
    geolocalizacion = column(String(255), nullable=True)
    id_puesto = column(Integer, ForeignKey('puesto.id_puesto'), nullable=False)

    def __init__(self, id_revista_puesto, id_usuario, id_tipo_armamento, 
                 id_tipo_comunicacion, obervaciones=None, recomendaciones=None, 
                 novedades=None, geolocalizacion=None, id_puesto=None):
        
        self.id_revista_puesto = id_revista_puesto
        self.id_usuario = id_usuario
        self.id_tipo_armamento = id_tipo_armamento
        self.id_tipo_comunicacion = id_tipo_comunicacion
        self.obervaciones = obervaciones
        self.recomendaciones = recomendaciones
        self.novedades = novedades
        self.geolocalizacion = geolocalizacion
        self.id_puesto = id_puesto

    def save(self):
        Session.add(self)
        Session.commit()

    def delete(self):   
        Session.delete(self)
        Session.commit()
    
    def get():
        revista_puesto = Session.query(revista_puesto).all()
        return revista_puesto
    
    def get_by_id(id_revista_puesto):
        revista_puesto = Session.query(revista_puesto).filter_by(id_revista_puesto=id_revista_puesto).first()
        return revista_puesto