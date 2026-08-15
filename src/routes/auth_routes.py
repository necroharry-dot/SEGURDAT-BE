from flask import Blueprint, request, jsonify

from src.models.usuarios_log import Usuarios_Log
from src.utils.auth import generar_token, token_requerido

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}

    for campo in ['email', 'password', 'nombre']:
        if not data.get(campo):
            return jsonify({'error': f'Campo {campo} es requerido'}), 400

    if len(data['password']) < 6:
        return jsonify({'error': 'La contraseña debe tener al menos 6 caracteres'}), 400

    if Usuarios_Log.get_by_email(data['email']):
        return jsonify({'error': 'El correo electrónico ya está registrado'}), 400

    usuario = Usuarios_Log(
        email=data['email'],
        password=data['password'],
        nombre=data['nombre'],
        cargo=data.get('cargo', 'usuario')
    )
    usuario.save()

    return jsonify({
        'message': 'Usuario registrado correctamente',
        'usuario': usuario.to_dict()
    }), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Correo electrónico y contraseña son requeridos'}), 400

    usuario = Usuarios_Log.get_by_email(email)



    if not usuario or not usuario.verificar_password(password):
        return jsonify({'error': 'Correo electrónico o contraseña incorrectos'}), 401

    return jsonify({
        'access_token': generar_token(usuario),
        'token_type': 'Bearer',
        'expires_in': 28800,
        'usuario': usuario.to_dict()
    }), 200


@auth_bp.route('/me', methods=['GET'])
@token_requerido
def me():
    return jsonify({'usuario': request.usuario.to_dict()}), 200
