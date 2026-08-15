from sqlalchemy.exc import IntegrityError
from src.models import Session
from flask import Blueprint, jsonify, request
from src.models.tipo_comunicacion import Tipo_Comunicacion
from src.utils.auth import token_requerido

tipo_comunicacion_bp = Blueprint('tipo_comunicacion', __name__)

@tipo_comunicacion_bp.route('/', methods=['GET'])
@token_requerido
def get_tipo_comunicacion():

    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=5, type=int)

    tipos, total = Tipo_Comunicacion.paginate(page, per_page)

    total_pages = (total + per_page - 1) // per_page

    return jsonify({
        'data': [t.to_dict() for t in tipos],
        'total': total,
        'total_pages': total_pages,
        'page': page,
        'per_page': per_page,
        'has_next': page < total_pages,
        'has_prev': page > 1
    }), 200


@tipo_comunicacion_bp.route('/<int:id_tipo_comunicacion>', methods=['GET'])
def get_tipo_comunicacion_by_id(id_tipo_comunicacion):
    tipo = Tipo_Comunicacion.get_by_id(id_tipo_comunicacion)

    if not tipo:
        return jsonify({
            'error': 'Tipo de comunicación no encontrado'
        }), 404

    return jsonify(tipo.to_dict())


@tipo_comunicacion_bp.route('/', methods=['POST'])
def create_tipo_comunicacion():
    data = request.get_json()

    nombre = data.get('nombre_Tcomunicacion')

    if not nombre or nombre.strip() == '':
        return jsonify({
            'error': 'El nombre del tipo de comunicacion no puede estar vacío'
        }), 400

    tipo_comunicacion = Tipo_Comunicacion(nombre)

    try:
        tipo_comunicacion.save()
    except IntegrityError:
        Session.rollback()
        return jsonify({
            'error': 'Ya existe un tipo de comunicación con ese nombre'
        }), 409

    return jsonify({
        'message': 'Tipo de comunicacion creado exitosamente',
        'tipo_comunicacion': tipo_comunicacion.to_dict()
    }), 201


@tipo_comunicacion_bp.route('/<int:id_tipo_comunicacion>', methods=['PUT'])

def update_tipo_comunicacion(id_tipo_comunicacion):
    tipo = Tipo_Comunicacion.get_by_id(id_tipo_comunicacion)

    if not tipo:
        return jsonify({
            'error': 'Tipo de comunicación no encontrado'
        }), 404

    data = request.get_json()
    nombre = data.get('nombre_Tcomunicacion')

    if not nombre or nombre.strip() == '':
        return jsonify({
            'error': 'El nombre del tipo de comunicacion no puede estar vacío'
        }), 400

    tipo.nombre_Tcomunicacion = nombre

    try:
        tipo.save()
    except IntegrityError:
        Session.rollback()
        return jsonify({
            'error': 'Ya existe un tipo de comunicación con ese nombre'
        }), 409

    return jsonify({
        'message': 'Tipo de comunicacion actualizado exitosamente',
        'tipo_comunicacion': tipo.to_dict()
    })