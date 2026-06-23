from flask import Blueprint, jsonify, request
from src.models.cargo import Cargo

cargo_bp = Blueprint('cargo', __name__)

@cargo_bp.route('/', methods=['GET'])
def get_cargo():
    cargo = Cargo.get()
    cargo_list = []
    for cargo in cargo:
        cargo_list.append({
            'nombre_cargo': cargo.nombre_cargo,
        })

    return jsonify(cargo_list), 200

@cargo_bp.route('/<int:id_cargo>', methods=['GET'])
def get_cargo_by_id(id_cargo):
    cargo = Cargo.get_by_id(id_cargo)
    if cargo:
        cargo_data = {
            'nombre_cargo': cargo.nombre_cargo,
        }
        return jsonify(cargo_data), 200
    else:
        return jsonify({'error': 'Cargo no encontrado'}), 404
    
@cargo_bp.route('/', methods=['POST'])
def create_cargo():
    data = request.get_json()
    cargo = Cargo(
        nombre_cargo=data['nombre_cargo'],
    )
    cargo.save()
    return jsonify({'message': 'Cargo creado exitosamente'}), 201

@cargo_bp.route('/<int:id_cargo>', methods=['PUT'])
def update_cargo(id_cargo):
    cargo = Cargo.get_by_id(id_cargo)
    if cargo:
        data = request.get_json()
        cargo.nombre_cargo = data['nombre_cargo']
        cargo.save()
        return jsonify({'message': 'Cargo actualizado exitosamente'}), 200
    else:
        return jsonify({'error': 'Cargo no encontrado'}), 404
