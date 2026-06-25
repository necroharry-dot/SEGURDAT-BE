from flask import Blueprint, jsonify, request
from src.models.Tipo_de_comunicacion import Tipo_Comunicacion

tipo_comunicacion_bp = Blueprint('tipo_comunicacion', __name__)

@tipo_comunicacion_bp.route('/', methods=['GET'])
def get_tipo_comunicacion():
    tipo_comunicacion = Tipo_Comunicacion.get()

    tipo_comunicacion_list = []

    for tipo_comunicacion in tipo_comunicacion:
        tipo_comunicacion_list.append({
            'id_tipo_comunicacion': tipo_comunicacion.id_tipo_comunicacion,
            'nombre_Tcomunicacion': tipo_comunicacion.nombre_Tcomunicacion
        })

    return jsonify(tipo_comunicacion_list)

@tipo_comunicacion_bp.route('/<int:id_tipo_comunicacion>', methods=['GET'])
def get_tipo_comunicacion_by_id(id_tipo_comunicacion):
    tipo_comunicacion = Tipo_Comunicacion.get_by_id(id_tipo_comunicacion)

    if tipo_comunicacion:
        return jsonify({
            'id_tipo_comunicacion': tipo_comunicacion.id_tipo_comunicacion,
            'nombre_Tcomunicacion': tipo_comunicacion.nombre_Tcomunicacion
        })
    return jsonify({
        'error': 'Tipo de comunicacion no encontrado'
    }), 404

@tipo_comunicacion_bp.route('/', methods=['POST'])
def create_tipo_comunicacion():
    data = request.get_json()

    nombre = data.get('nombre_Tcomunicacion')

    if not nombre or nombre.strip() == '':
        return jsonify({
            'error': 'El nombre del tipo de comunicacion no puede estar vacío'
        }), 400

    tipo_comunicacion = Tipo_Comunicacion(nombre)

    tipo_comunicacion.save()

    return jsonify({
        'message': 'Tipo de comunicacion creado exitosamente',
        'tipo_comunicacion': tipo_comunicacion.to_dict()
    }), 201



@tipo_comunicacion_bp.route('/<int:id_tipo_comunicacion>', methods=['PUT'])
def update_tipo_comunicacion(id_tipo_comunicacion):
    tipo_comunicacion = Tipo_Comunicacion.get_by_id(id_tipo_comunicacion)

    if tipo_comunicacion:
        data = request.get_json()
        nombre = data.get('nombre_Tcomunicacion')

        if not nombre or nombre.strip() == '':
            return jsonify({
                'error': 'El nombre del tipo de comunicacion no puede estar vacío'
            }), 400

        tipo_comunicacion.nombre_Tcomunicacion = nombre
        tipo_comunicacion.save()

        return jsonify({
            'message': 'Tipo de comunicacion actualizado exitosamente',
            'tipo_comunicacion': tipo_comunicacion.to_dict()
        }), 200

    return jsonify({
        'error': 'Tipo de comunicacion no encontrado'
    }), 404