from flask import Flask 
from src.models import Base, engine
from src.models.armamento import Armamento
from src.models.comunicacion import Comunicacion
from src.models.revista_puesto import Revista_puesto
from src.routes import all_blueprints
import os
from dotenv import load_dotenv
from flask_cors import CORS

# Cargar variables de entorno desde el archivo .env
load_dotenv() 

app = Flask(__name__)
CORS(app)

# Configuración de la clave secreta para JWT
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

Base.metadata.create_all(engine)
# Registro de los blueprints de las rutas de la aplicación con un prefijo común
prefix = '/api/v1'
for bp in all_blueprints:
    print(bp)
    url_prefix=f"{prefix}/{bp.name}"
    print(url_prefix)
    app.register_blueprint(bp, url_prefix=url_prefix)

if __name__ == '__main__':
    app.run(debug=True)

