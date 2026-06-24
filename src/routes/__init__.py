from .Armamento_routes import armamento_bp
from .Cargo_routes import cargo_bp
from .Comunicacion_routes import comunicacion_bp
from .Puesto_routes import puesto_bp
from .tipo_armamento_routes import tipo_armamento_bp
from .Tipo_de_comunicacion_routes import tipo_comunicacion_bp
from .usuarios_routes import usuarios_bp
from .revista_puesto_routes import revista_puesto_bp



all_blueprints = [
    armamento_bp,
    cargo_bp,
    comunicacion_bp,
    puesto_bp,
    tipo_armamento_bp,
    tipo_comunicacion_bp,
    usuarios_bp,
    revista_puesto_bp
]
