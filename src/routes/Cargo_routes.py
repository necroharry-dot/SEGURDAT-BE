from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from src.models.cargo import Cargo
from src.utils.auth import token_requerido, cargo_requerido

cargo_bp = Blueprint('cargo', __name__)

@cargo_bp.route('/', methods=['GET'])
@token_requerido
@cargo_requerido(['Gerente', 'Coordinador', 'Administrador', 'Supervisor'])
def get_cargo():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=20, type=int)

    cargos, total = Cargo.paginate(page=page, per_page=per_page)

    total_pages = (total + per_page - 1) // per_page  # Calcular el número total de páginas

    return jsonify({
        'data': [cargo.to_dict() for cargo in cargos],
        'meta': {
            'page': page,
            'per_page': per_page,
            'total': total,
            'total_pages': total_pages,
            'has_next': page < total_pages,
            'has_prev': page > 1
        }
    }), 200



    cargo_list = []
    for cargo in cargos:
        cargo_list.append({
            'id_cargo': cargo.id_cargo,
            'nombre_cargo': cargo.nombre_cargo,
        })

    return jsonify(cargo_list), 200

@cargo_bp.route('/<int:id_cargo>', methods=['GET'])
@token_requerido
@cargo_requerido(['Gerente', 'Coordinador', 'Administrador', 'Supervisor'])
def get_cargo_by_id(id_cargo):
    cargo = Cargo.get_by_id(id_cargo)
    if cargo:
        cargo_data = {
            'id_cargo': cargo.id_cargo,
            'nombre_cargo': cargo.nombre_cargo,
        }
        return jsonify(cargo_data), 200
    else:
        return jsonify({'error': 'Cargo no encontrado'}), 404

@cargo_bp.route('/', methods=['POST'])
@token_requerido
@cargo_requerido(['Gerente', 'Coordinador', 'Administrador'])
def create_cargo():
    data = request.get_json()

    nombre_cargo = data.get('nombre_cargo', '').strip()

    if not nombre_cargo:
        return jsonify({'error': 'El nombre del cargo no puede estar vacío'}), 400

    cargo = Cargo(nombre_cargo=nombre_cargo)

    try:
        cargo.save()
    except IntegrityError:
        return jsonify({'error': 'Ya existe un cargo con ese nombre'}), 409

    return jsonify({'message': 'Cargo creado exitosamente', 'cargo': cargo.to_dict()}), 201

@cargo_bp.route('/<int:id_cargo>', methods=['PUT'])
@token_requerido
@cargo_requerido(['Gerente', 'Coordinador', 'Administrador'])
def update_cargo(id_cargo):
    cargo = Cargo.get_by_id(id_cargo)
    if not cargo:
        return jsonify({'error': 'Cargo no encontrado'}), 404

    data = request.get_json()
    nombre_cargo = data.get('nombre_cargo', '').strip()

    if not nombre_cargo:
        return jsonify({'error': 'El nombre del cargo no puede estar vacío'}), 400

    cargo.nombre_cargo = nombre_cargo

    try:
        cargo.save()
    except IntegrityError:
        return jsonify({'error': 'Ya existe un cargo con ese nombre'}), 409

    return jsonify({'message': 'Cargo actualizado exitosamente', 'cargo': cargo.to_dict()}), 200

@cargo_bp.route('/<int:id_cargo>', methods=['DELETE'])
@token_requerido
@cargo_requerido(['Gerente', 'Coordinador', 'Administrador'])
def delete_cargo(id_cargo):
    cargo = Cargo.get_by_id(id_cargo)
    if not cargo:
        return jsonify({'error': 'Cargo no encontrado'}), 404

    cargo.delete()

    return jsonify({'message': 'Cargo eliminado exitosamente'}), 200