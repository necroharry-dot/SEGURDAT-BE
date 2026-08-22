from flask import Blueprint, jsonify, request
from src.models.usuarios import Usuarios
from src.utils.auth import token_requerido

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/', methods=['GET'])
@token_requerido
def get_usuarios():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=5, type=int)


    usuarios, total = Usuarios.paginate(page=page, per_page=per_page)

    total_pages = (total + per_page - 1) // per_page  # Calcular el número total de páginas

    return jsonify({
        'data': [usuario.to_dict() for usuario in usuarios],
        'meta': {
            'page': page,
            'per_page': per_page,
            'total': total,
            'total_pages': total_pages,
            'has_next': page < total_pages,
            'has_prev': page > 1
        }
        }), 200

    usuarios_list = []
    for usuario in usuarios:
        usuarios_list.append({
            'id_usuario': usuario.id_usuario,
            'nombre': usuario.nombre,
            'documento_identidad': usuario.documento_identidad,
            'celular': usuario.celular,
            'fecha_nacimiento': usuario.fecha_nacimiento,
            'edad': usuario.edad,
            'direccion': usuario.direccion,
            'fecha_ingreso': usuario.fecha_ingreso,
            'eps': usuario.eps,
            'fondo_pension': usuario.fondo_pension,
            'id_cargo': usuario.id_cargo,
            'correo_electronico': usuario.correo_electronico,
        })
    return jsonify(usuarios_list), 200

@usuarios_bp.route('/<int:id_usuario>', methods=['GET'])
def get_usuario_by_id(id_usuario):
    usuario = Usuarios.get_by_id(id_usuario)
    if usuario:
        usuario_data = {
            'id_usuario': usuario.id_usuario,
            'nombre': usuario.nombre,
            'documento_identidad': usuario.documento_identidad,
            'celular': usuario.celular,
            'fecha_nacimiento': usuario.fecha_nacimiento,
            'edad': usuario.edad,
            'direccion': usuario.direccion,
            'fecha_ingreso': usuario.fecha_ingreso,
            'eps': usuario.eps,
            'fondo_pension': usuario.fondo_pension,
            'id_cargo': usuario.id_cargo,
            'correo_electronico': usuario.correo_electronico,

        }
        return jsonify(usuario_data), 200
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    
@usuarios_bp.route('/', methods=['POST'])
def create_usuario():
    data = request.get_json()
    usuario = Usuarios(
        nombre=data['nombre'],
        documento_identidad=data['documento_identidad'],
        celular=data['celular'],
        fecha_nacimiento=data['fecha_nacimiento'],
        edad=data['edad'],
        direccion=data['direccion'],
        fecha_ingreso=data['fecha_ingreso'],
        eps=data['eps'],
        fondo_pension=data['fondo_pension'],
        id_cargo=data['id_cargo'],
        correo_electronico=data['correo_electronico'],

    )

    try:
        int(usuario.documento_identidad)
    except ValueError:
        return jsonify({'error': 'El documento de identidad debe ser un número entero'}), 400
    
    try:
        int(usuario.celular)
    except ValueError:
        return jsonify({'error': 'El celular debe ser un número entero'}), 400
    
    if usuario.nombre == '':
        return jsonify({'error': 'El nombre no puede estar vacío'}), 400
    if usuario.documento_identidad == '':
        return jsonify({'error': 'El documento de identidad no puede estar vacío'}), 400
    if usuario.celular == '':
        return jsonify({'error': 'El celular no puede estar vacío'}), 400
    if usuario.fecha_nacimiento == '':
        return jsonify({'error': 'La fecha de nacimiento no puede estar vacía'}), 400
    if usuario.edad == '':
        return jsonify({'error': 'La edad no puede estar vacía'}), 400
    if usuario.direccion == '':
        return jsonify({'error': 'La dirección no puede estar vacía'}), 400
    if usuario.fecha_ingreso == '':
        return jsonify({'error': 'La fecha de ingreso no puede estar vacía'}), 400
    if usuario.eps == '':
        return jsonify({'error': 'La EPS no puede estar vacía'}), 400
    if usuario.fondo_pension == '':
        return jsonify({'error': 'El fondo de pensión no puede estar vacío'}), 400
    if usuario.id_cargo == '':
        return jsonify({'error': 'El ID del cargo no puede estar vacío'}), 400
    if usuario.correo_electronico == '':
        return jsonify({'error': 'El correo electrónico no puede estar vacío'}), 400

    

    usuario.save()
    return jsonify({'message': 'Usuario creado exitosamente', 'usuario': usuario.to_dict()}), 201

@usuarios_bp.route('/<int:id_usuario>', methods=['PUT'])
def update_usuario(id_usuario):
    usuario = Usuarios.get_by_id(id_usuario)
    if not usuario:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    data = request.get_json()
    usuario.nombre = data.get('nombre', usuario.nombre)
    usuario.documento_identidad = data.get('documento_identidad', usuario.documento_identidad)
    usuario.celular = data.get('celular', usuario.celular)
    usuario.fecha_nacimiento = data.get('fecha_nacimiento', usuario.fecha_nacimiento)
    usuario.edad = data.get('edad', usuario.edad)
    usuario.direccion = data.get('direccion', usuario.direccion)
    usuario.fecha_ingreso = data.get('fecha_ingreso', usuario.fecha_ingreso)
    usuario.eps = data.get('eps', usuario.eps)
    usuario.fondo_pension = data.get('fondo_pension', usuario.fondo_pension)
    usuario.id_cargo = data.get('id_cargo', usuario.id_cargo)
    usuario.correo_electronico = data.get('correo_electronico', usuario.correo_electronico)


    try:
        int(usuario.documento_identidad)
    except ValueError:
        return jsonify({'error': 'El documento de identidad debe ser un número entero'}), 400
    
    try:
        int(usuario.celular)
    except ValueError:
        return jsonify({'error': 'El celular debe ser un número entero'}), 400
    
    if usuario.nombre == '':
        return jsonify({'error': 'El nombre no puede estar vacío'}), 400
    if usuario.documento_identidad == '':
        return jsonify({'error': 'El documento de identidad no puede estar vacío'}), 400
    if usuario.celular == '':
        return jsonify({'error': 'El celular no puede estar vacío'}), 400
    if usuario.fecha_nacimiento == '':
        return jsonify({'error': 'La fecha de nacimiento no puede estar vacía'}), 400
    if usuario.edad == '':
        return jsonify({'error': 'La edad no puede estar vacía'}), 400
    if usuario.direccion == '':
        return jsonify({'error': 'La dirección no puede estar vacía'}), 400
    if usuario.fecha_ingreso == '':
        return jsonify({'error': 'La fecha de ingreso no puede estar vacía'}), 400
    if usuario.eps == '':
        return jsonify({'error': 'La EPS no puede estar vacía'}), 400
    if usuario.fondo_pension == '':
        return jsonify({'error': 'El fondo de pensión no puede estar vacío'}), 400
    if usuario.id_cargo == '':
        return jsonify({'error': 'El ID del cargo no puede estar vacío'}), 400
    if usuario.correo_electronico == '':
        return jsonify({'error': 'El correo electrónico no puede estar vacío'}), 400

    
    usuario.save()
    return jsonify({'message': 'Usuario actualizado exitosamente', 'usuario': usuario.to_dict()}), 200
    
    