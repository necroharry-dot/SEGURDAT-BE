from flask import Blueprint, jsonify, request
from src.models.revista_puesto import Revista_puesto

revista_puesto_bp = Blueprint('revista_puesto', __name__)

@revista_puesto_bp.route('/', methods=['GET'])
def get_revista_puesto():
    revista_puesto = Revista_puesto.get()
    revista_puesto_list = []
    for revista in revista_puesto:
        revista_puesto_list.append({
            'id_revista_puesto': revista.id_revista_puesto,
            'id_usuario': revista.id_usuario,
            'id_tipo_armamento': revista.id_tipo_armamento,
            'id_tipo_comunicacion': revista.id_tipo_comunicacion,
            'obervaciones': revista.obervaciones,
            'recomendaciones': revista.recomendaciones,
            'novedades': revista.novedades,
            'geolocalizacion': revista.geolocalizacion,
            'id_puesto': revista.id_puesto
        })
    return jsonify(revista_puesto_list), 200

@revista_puesto_bp.route('/<int:id_revista_puesto>', methods=['GET'])
def get_revista_puesto_by_id(id_revista_puesto):
    revista_puesto = Revista_puesto.get_by_id(id_revista_puesto)
    if revista_puesto:
        revista_data = {
            'id_revista_puesto': revista_puesto.id_revista_puesto,
            'id_usuario': revista_puesto.id_usuario,
            'id_tipo_armamento': revista_puesto.id_tipo_armamento,
            'id_tipo_comunicacion': revista_puesto.id_tipo_comunicacion,
            'obervaciones': revista_puesto.obervaciones,
            'recomendaciones': revista_puesto.recomendaciones,
            'novedades': revista_puesto.novedades,
            'geolocalizacion': revista_puesto.geolocalizacion,
            'id_puesto': revista_puesto.id_puesto
        }
        return jsonify(revista_data), 200
    else:
        return jsonify({'error': 'Revista de puesto no encontrada'}), 404

@revista_puesto_bp.route('/', methods=['POST'])
def create_revista_puesto():
    data = request.get_json()

    if not data:
        return jsonify({
            'error': 'No se recibieron datos'
        }), 400

    required_fields = [
        'id_usuario',
        'id_tipo_armamento',
        'id_tipo_comunicacion',
        'id_puesto'
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                'error': f'El campo {field} es obligatorio'
            }), 400

    revista_puesto = Revista_puesto(
        id_usuario=data['id_usuario'],
        id_tipo_armamento=data['id_tipo_armamento'],
        id_tipo_comunicacion=data['id_tipo_comunicacion'],
        obervaciones=data.get('obervaciones'),
        recomendaciones=data.get('recomendaciones'),
        novedades=data.get('novedades'),
        geolocalizacion=data.get('geolocalizacion'),
        id_puesto=data['id_puesto']
    )

    revista_puesto.save()

    return jsonify({
        'message': 'Revista de puesto creada exitosamente',
        'id_revista_puesto': revista_puesto.id_revista_puesto
    }), 201

@revista_puesto_bp.route('/<int:id_revista_puesto>', methods=['PUT'])
def update_revista_puesto(id_revista_puesto):
    revista_puesto = Revista_puesto.get_by_id(id_revista_puesto)
    if not revista_puesto:
        return jsonify({'error': 'Revista de puesto no encontrada'}), 404

    data = request.get_json()
  
    revista_puesto.id_usuario = data.get('id_usuario', revista_puesto.id_usuario)
    revista_puesto.id_tipo_armamento = data.get('id_tipo_armamento', revista_puesto.id_tipo_armamento)
    revista_puesto.id_tipo_comunicacion = data.get('id_tipo_comunicacion', revista_puesto.id_tipo_comunicacion)
    revista_puesto.obervaciones = data.get('obervaciones', revista_puesto.obervaciones)
    revista_puesto.recomendaciones = data.get('recomendaciones', revista_puesto.recomendaciones)
    revista_puesto.novedades = data.get('novedades', revista_puesto.novedades)
    revista_puesto.geolocalizacion = data.get('geolocalizacion', revista_puesto.geolocalizacion)
    revista_puesto.id_puesto = data.get('id_puesto', revista_puesto.id_puesto)

    if revista_puesto.id_usuario == "":
        return jsonify({'error': 'El id del usuario no puede estar vacío'}), 400
    if revista_puesto.id_tipo_armamento == "":
        return jsonify({'error': 'El id del tipo de armamento no puede estar vacío'}), 400
    if revista_puesto.id_tipo_comunicacion == "":
        return jsonify({'error': 'El id del tipo de comunicación no puede estar vacío'}), 400
    if revista_puesto.id_puesto == "":
        return jsonify({'error': 'El id del puesto no puede estar vacío'}), 400
    if revista_puesto.obervaciones == "":
        return jsonify({'error': 'Las observaciones no pueden estar vacías'}), 400
    if revista_puesto.recomendaciones == "":
        return jsonify({'error': 'Las recomendaciones no pueden estar vacías'}), 400
    if revista_puesto.novedades == "":
        return jsonify({'error': 'Las novedades no pueden estar vacías'}), 400
    if revista_puesto.geolocalizacion == "":
        return jsonify({'error': 'La geolocalización no puede estar vacía'}), 400
    

    revista_puesto.save()
    return jsonify({'message': 'Revista de puesto actualizada exitosamente'}), 200

