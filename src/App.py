from flask import Flask 
from src.models import Base, engine
from src.models.armamento import Armamento
from src.models.comunicacion import Comunicacion
from src.models.revista_puesto import Revista_puesto
from src.routes import all_blueprints
import os
from dotenv import load_dotenv


load_dotenv() 

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

Base.metadata.create_all(engine)

prefix = '/api/v1'
for bp in all_blueprints:
    print(bp)
    url_prefix=f"{prefix}/{bp.name}"
    print(url_prefix)
    app.register_blueprint(bp, url_prefix=url_prefix)

if __name__ == '__main__':
    app.run(debug=True)

