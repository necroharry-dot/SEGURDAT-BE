from flask import Blueprint, jsonify, request
from src.models.puesto import Puesto

puesto_bp = Blueprint('puesto', __name__)

@puesto_bp.route('/', methods=['GET'])
def get_puesto():
    puesto = Puesto.get()
    puesto_list = []
    for puesto in puesto:
        puesto_list.append({
            'nombre_puesto': puesto.nombre_puesto,
            'direccion_puesto': puesto.direccion_puesto,
            'encargado_puesto': puesto.encargado_puesto,
            'numero_encargado': puesto.numero_encargado,
            'nit_puesto': puesto.nit_puesto,
            'email_puesto': puesto.email_puesto,
            'descripcion_puesto': puesto.descripcion_puesto,
            'georef_puesto': puesto.georef_puesto,
            'id_armamento_puesto': puesto.id_armamento_puesto
        })
    return jsonify(puesto_list), 200

@puesto_bp.route('/<int:id_puesto>', methods=['GET'])
def get_puesto_by_id(id_puesto):
    puesto = Puesto.get_by_id(id_puesto)
    if puesto:
        puesto_data = {
            'nombre_puesto': puesto.nombre_puesto,
            'direccion_puesto': puesto.direccion_puesto,
            'encargado_puesto': puesto.encargado_puesto,
            'numero_encargado': puesto.numero_encargado,
            'nit_puesto': puesto.nit_puesto,
            'email_puesto': puesto.email_puesto,
            'descripcion_puesto': puesto.descripcion_puesto,
            'georef_puesto': puesto.georef_puesto,
            'id_armamento_puesto': puesto.id_armamento_puesto,

        }
        return jsonify(puesto_data), 200
    else:
        return jsonify({'error': 'Puesto no encontrado'}), 404
    
@puesto_bp.route('/', methods=['POST'])
def create_puesto():
    data = request.get_json()
    puesto = Puesto(
        nombre_puesto=data['nombre_puesto'],
        direccion_puesto=data.get('direccion_puesto'),
        encargado_puesto=data.get('encargado_puesto'),
        numero_encargado=data.get('numero_encargado'),
        nit_puesto=data.get('nit_puesto'),
        email_puesto=data.get('email_puesto'),
        descripcion_puesto=data.get('descripcion_puesto'),
        georef_puesto=data.get('georef_puesto'),
        id_armamento_puesto=data.get('id_armamento_puesto'),

    )

    try:
        int(puesto.numero_encargado)
    except ValueError:
        return jsonify({'error': 'El número de encargado debe ser un entero'}), 400
    
    if puesto.nombre_puesto == "":
        return jsonify({'error': 'El nombre del puesto no puede estar vacío'}), 400
    if puesto.direccion_puesto == "":
        return jsonify({'error': 'La dirección del puesto no puede estar vacía'}), 400
    if puesto.encargado_puesto == "":
        return jsonify({'error': 'El encargado del puesto no puede estar vacío'}), 400
    if puesto.numero_encargado == "":
        return jsonify({'error': 'El número del encargado no puede estar vacío'}), 400
    if puesto.nit_puesto == "":
        return jsonify({'error': 'El NIT del puesto no puede estar vacío'}), 400
    if puesto.email_puesto == "":
        return jsonify({'error': 'El email del puesto no puede estar vacío'}), 400
    if puesto.descripcion_puesto == "":
        return jsonify({'error': 'La descripción del puesto no puede estar vacía'}), 400
    
    puesto.save()
    return jsonify({'message': 'Puesto creado exitosamente', 'puesto': puesto.to_dict()}), 201

@puesto_bp.route('/<int:id_puesto>', methods=['PUT'])
def update_puesto(id_puesto):
    puesto = Puesto.get_by_id(id_puesto)
    if puesto:
        data = request.get_json()
        puesto.nombre_puesto = data['nombre_puesto']
        puesto.direccion_puesto = data.get('direccion_puesto')
        puesto.encargado_puesto = data.get('encargado_puesto')
        puesto.numero_encargado = data.get('numero_encargado')
        puesto.nit_puesto = data.get('nit_puesto')
        puesto.email_puesto = data.get('email_puesto')
        puesto.descripcion_puesto = data.get('descripcion_puesto')
        puesto.georef_puesto = data.get('georef_puesto')
        puesto.id_armamento_puesto = data.get('id_armamento_puesto')


        try:
            int(puesto.numero_encargado)
        except ValueError:
            return jsonify({'error': 'El número de encargado debe ser un entero'}), 400
        
        if puesto.nombre_puesto == "":
            return jsonify({'error': 'El nombre del puesto no puede estar vacío'}), 400
        if puesto.direccion_puesto == "":
            return jsonify({'error': 'La dirección del puesto no puede estar vacía'}), 400
        if puesto.encargado_puesto == "":
            return jsonify({'error': 'El encargado del puesto no puede estar vacío'}), 400
        if puesto.numero_encargado == "":
            return jsonify({'error': 'El número del encargado no puede estar vacío'}), 400
        if puesto.nit_puesto == "":
            return jsonify({'error': 'El NIT del puesto no puede estar vacío'}), 400
        if puesto.email_puesto == "":
            return jsonify({'error': 'El email del puesto no puede estar vacío'}), 400
        if puesto.descripcion_puesto == "":
            return jsonify({'error': 'La descripción del puesto no puede estar vacía'}), 400

        puesto.save()
    from sqlalchemy.exc import IntegrityError, SQLAlchemyError
    try:
        puesto.save()
    except IntegrityError:
        return jsonify({'error': 'El NIT ya existe o el armamento indicado no es válido'}), 409
    except SQLAlchemyError:
        return jsonify({'error': 'Error al guardar el puesto en la base de datos'}), 500

    return jsonify({'message': 'Puesto creado exitosamente', 'puesto': puesto.to_dict()}), 201
    