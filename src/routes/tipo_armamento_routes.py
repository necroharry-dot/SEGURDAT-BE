from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from src.models.tipo_armamento import Tipo_Armamento
from src.utils.auth import token_requerido, cargo_requerido

tipo_armamento_bp = Blueprint('tipo_armamento', __name__)


@tipo_armamento_bp.route('/', methods=['GET'])
@token_requerido
@cargo_requerido(['Coordinador', 'Administrador', 'Getente', 'Supervisor'])
def get_tipo_armamento():

    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=5, type=int)

    tipo_armamentos, total = Tipo_Armamento.paginate(page, per_page)

    total_pages = (total + per_page - 1) // per_page  # Calcular el número total de páginas

    return jsonify({
        'data': [tipo_armamento.to_dict() for tipo_armamento in tipo_armamentos],
        'total': total,
        'total_pages': total_pages,
        'page': page,
        'per_page': per_page,
        'has_next': page < total_pages,
        'has_prev': page > 1
    }), 200

    tipo_armamento_list = []

    for tipo_armamento in tipo_armamentos:
        tipo_armamento_list.append({
            'id_tipo_armamento': tipo_armamento.id_tipo_armamento,
            'nombre': tipo_armamento.nombre
        })

    return jsonify(tipo_armamento_list), 200


@tipo_armamento_bp.route('/<int:id_tipo_armamento>', methods=['GET'])
@token_requerido
@cargo_requerido(['Coordinador', 'Administrador', 'Getente', 'Supervisor'])
def get_tipo_armamento_by_id(id_tipo_armamento):
    tipo_armamento = Tipo_Armamento.get_by_id(id_tipo_armamento)

    if tipo_armamento:
        return jsonify({
            'id_tipo_armamento': tipo_armamento.id_tipo_armamento,
            'nombre': tipo_armamento.nombre
        }), 200

    return jsonify({
        'error': 'Tipo de armamento no encontrado'
    }), 404


@tipo_armamento_bp.route('/', methods=['POST'])
def create_tipo_armamento():
    data = request.get_json()

    nombre = data.get('nombre', '').strip()

    if not nombre:
        return jsonify({
            'error': 'El nombre del tipo de armamento no puede estar vacío'
        }), 400

    tipo_armamento = Tipo_Armamento(nombre=nombre)

    try:
        tipo_armamento.save()
    except IntegrityError:
        return jsonify({
            'error': 'Ya existe un tipo de armamento con ese nombre'
        }), 409

    return jsonify({
        'message': 'Tipo de armamento creado exitosamente',
        'tipo_armamento': tipo_armamento.to_dict()
    }), 201


@tipo_armamento_bp.route('/<int:id_tipo_armamento>', methods=['PUT'])
@token_requerido
@cargo_requerido(['Coordinador', 'Administrador', 'Getente', 'Supervisor'])
def update_tipo_armamento(id_tipo_armamento):
    tipo_armamento = Tipo_Armamento.get_by_id(id_tipo_armamento)

    if not tipo_armamento:
        return jsonify({
            'error': 'Tipo de armamento no encontrado'
        }), 404

    data = request.get_json()

    nombre = data.get('nombre', '').strip()

    if not nombre:
        return jsonify({
            'error': 'El nombre del tipo de armamento no puede estar vacío'
        }), 400

    tipo_armamento.nombre = nombre

    tipo_armamento.save()

    return jsonify({
        'message': 'Tipo de armamento actualizado exitosamente',
        'tipo_armamento': tipo_armamento.to_dict()
    }), 200


@tipo_armamento_bp.route('/<int:id_tipo_armamento>', methods=['DELETE'])
@token_requerido
@cargo_requerido(['Coordinador', 'Administrador', 'Getente'])
def delete_tipo_armamento(id_tipo_armamento):
    tipo_armamento = Tipo_Armamento.get_by_id(id_tipo_armamento)

    if not tipo_armamento:
        return jsonify({
            'error': 'Tipo de armamento no encontrado'
        }), 404

    tipo_armamento.delete()

    return jsonify({
        'message': 'Tipo de armamento eliminado exitosamente'
    }), 200