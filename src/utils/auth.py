from datetime import datetime, timedelta, timezone
import functools 
from functools import wraps
import jwt

from flask import request, jsonify, current_app

from src.models.usuarios_log import Usuarios_Log

def generar_token(usuario, horas=8):
    payload = {
        'sub': str(usuario.id_usuario_log),
        'email': usuario.email,
        'cargo': usuario.cargo,
        'iat': datetime.now(timezone.utc),
        'exp': datetime.now(timezone.utc) + timedelta(hours=horas)
    }

    return jwt.encode(payload, current_app.config['JWT_SECRET_KEY'], algorithm='HS256')



def token_requerido(f):

    @wraps(f)
    def decorada(*args, **kwargs):
        auth = request.headers.get('Authorization', '')

        if not auth or not auth.startswith('Bearer '):
            return jsonify({'error': 'Token no proporcionado'}), 401

        token = auth.split(' ')[1].strip()

        try:
            payload = jwt.decode(token, current_app.config['JWT_SECRET_KEY'], 
                                 algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token expirado inicie sesión de nuevo'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Token inválido'}), 401

        usuario = Usuarios_Log.get_by_id(payload['sub'])
        if not usuario:
            return jsonify({'error': 'Usuario no encontrado'}), 404

        request.usuario = usuario
        return f(*args, **kwargs)

    return decorada

def cargo_requerido(cargo):

    def decorador(f):
        @wraps(f)
        def decorada(*args, **kwargs):
            if request.usuario.cargo not in cargo:
                return jsonify({'mensaje': 'Acceso denegado, no tiene el cargo requerido'}), 403
            return f(*args, **kwargs)
        return decorada
    return decorador
    