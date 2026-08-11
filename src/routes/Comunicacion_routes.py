from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from src.models.comunicacion import Comunicacion

comunicacion_bp = Blueprint('comunicacion', __name__)

@comunicacion_bp.route('/', methods=['GET'])
def get_comunicacion():
    comunicacion = Comunicacion.get()
    comunicacion_list = []
    for comunicacion in comunicacion:
        comunicacion_list.append({
            'id_comunicacion': comunicacion.id_comunicacion,
            'id_tipo_comunicacion': comunicacion.id_tipo_comunicacion,
            'numero_serial': comunicacion.numero_serial,
            'modelo': comunicacion.modelo,
            'imei': comunicacion.imei,
            'estado': comunicacion.estado,
            'fabricante': comunicacion.fabricante,
            'simcard': comunicacion.simcard
        })
    return jsonify(comunicacion_list), 200


@comunicacion_bp.route('/<int:id_comunicacion>', methods=['GET'])
def get_comunicacion_by_id(id_comunicacion):
    comunicacion = Comunicacion.get_by_id(id_comunicacion)
    if comunicacion:
        comunicacion_data = {
            'id_comunicacion': comunicacion.id_comunicacion,
            'id_tipo_comunicacion': comunicacion.id_tipo_comunicacion,
            'numero_serial': comunicacion.numero_serial,
            'modelo': comunicacion.modelo,
            'imei': comunicacion.imei,
            'estado': comunicacion.estado,
            'fabricante': comunicacion.fabricante,
            'simcard': comunicacion.simcard
        }
        return jsonify(comunicacion_data), 200
    else:
        return jsonify({'error': 'Comunicacion no encontrada'}), 404
    
@comunicacion_bp.route('/', methods=['POST'])
def create_comunicacion():
    data = request.get_json()
    comunicacion = Comunicacion(
        id_tipo_comunicacion=data['id_tipo_comunicacion'],
        numero_serial=data['numero_serial'],
        modelo=data['modelo'],
        imei=data['imei'],
        estado=data['estado'],
        fabricante=data['fabricante'],
        simcard=data['simcard']
    )

    try:
        int(comunicacion.imei)
    except ValueError:
        return jsonify({'error': 'El IMEI debe ser un número entero'}), 400

    if comunicacion.numero_serial == "":
        return jsonify({'error': 'El número de serie no puede estar vacío'}), 400
    if comunicacion.modelo == "":
        return jsonify({'error': 'El modelo no puede estar vacío'}), 400
    if comunicacion.imei == "":
        return jsonify({'error': 'El IMEI no puede estar vacío'}), 400
    if comunicacion.estado == "":
        return jsonify({'error': 'El estado no puede estar vacío'}), 400
    if comunicacion.fabricante == "":
        return jsonify({'error': 'El fabricante no puede estar vacío'}), 400
    if comunicacion.simcard == "":
        return jsonify({'error': 'La SIM card no puede estar vacía'}), 400

    try:
        comunicacion.save()
    except IntegrityError:
        return jsonify({'error': 'Ya existe una comunicación con ese número serial, IMEI o SIM card'}), 409

    return jsonify({'message': 'Comunicacion creada exitosamente', 'comunicacion': comunicacion.to_dict()}), 201

@comunicacion_bp.route('/<int:id_comunicacion>', methods=['PUT'])
def update_comunicacion(id_comunicacion):
    comunicacion = Comunicacion.get_by_id(id_comunicacion)
    if not comunicacion:
        return jsonify({'error': 'Comunicacion no encontrada'}), 404

    data = request.get_json()
    comunicacion.id_tipo_comunicacion = data.get('id_tipo_comunicacion', comunicacion.id_tipo_comunicacion)
    comunicacion.numero_serial = data.get('numero_serial', comunicacion.numero_serial)
    comunicacion.modelo = data.get('modelo', comunicacion.modelo)
    comunicacion.imei = data.get('imei', comunicacion.imei)
    comunicacion.estado = data.get('estado', comunicacion.estado)
    comunicacion.fabricante = data.get('fabricante', comunicacion.fabricante)
    comunicacion.simcard = data.get('simcard', comunicacion.simcard)

    try:
        int(comunicacion.imei)
    except ValueError:
        return jsonify({'error': 'El IMEI debe ser un número entero'}), 400

    if comunicacion.numero_serial == "":
        return jsonify({'error': 'El número de serie no puede estar vacío'}), 400
    if comunicacion.modelo == "":
        return jsonify({'error': 'El modelo no puede estar vacío'}), 400
    if comunicacion.imei == "":
        return jsonify({'error': 'El IMEI no puede estar vacío'}), 400
    if comunicacion.estado == "":
        return jsonify({'error': 'El estado no puede estar vacío'}), 400
    if comunicacion.fabricante == "":
        return jsonify({'error': 'El fabricante no puede estar vacío'}), 400
    if comunicacion.simcard == "":
        return jsonify({'error': 'La SIM card no puede estar vacía'}), 400

    try:
        comunicacion.save()
    except IntegrityError:
        return jsonify({'error': 'Ya existe una comunicación con ese número serial, IMEI o SIM card'}), 409

    return jsonify({'message': 'Comunicacion actualizada exitosamente', 'comunicacion': comunicacion.to_dict()}), 200