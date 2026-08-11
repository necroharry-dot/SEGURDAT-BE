from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from src.models.cargo import Cargo

cargo_bp = Blueprint('cargo', __name__)

@cargo_bp.route('/', methods=['GET'])
def get_cargo():
    cargos = Cargo.get()
    cargo_list = []
    for cargo in cargos:
        cargo_list.append({
            'id_cargo': cargo.id_cargo,
            'nombre_cargo': cargo.nombre_cargo,
        })

    return jsonify(cargo_list), 200

@cargo_bp.route('/<int:id_cargo>', methods=['GET'])
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
def delete_cargo(id_cargo):
    cargo = Cargo.get_by_id(id_cargo)
    if not cargo:
        return jsonify({'error': 'Cargo no encontrado'}), 404

    cargo.delete()

    return jsonify({'message': 'Cargo eliminado exitosamente'}), 200