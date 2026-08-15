from flask import Blueprint, jsonify, request
from src.models.armamento import Armamento
from src.utils.auth import token_requerido, cargo_requerido

armamento_bp = Blueprint('armamento', __name__)

@armamento_bp.route('/', methods=['GET'])
@token_requerido
@cargo_requerido(['Administrador', 'Supervisor', 'Gerente'])
def get_armamento():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=5, type=int)

    armamento, total = Armamento.paginate(page=page, per_page=per_page)

    total_pages = (total + per_page - 1) // per_page  # Calcular el número total de páginas
    return jsonify({
        'data': [armamento.to_dict() for armamento in armamento],
        'meta': {
            'page': page,
            'per_page': per_page,
            'total': total,
            'total_pages': total_pages,
            'has_next': page < total_pages,
            'has_prev': page > 1
        }
    }), 200

    armamento_list = []
    for armamento in armamento:
        armamento_list.append({
            'id_armamento': armamento.id_armamento,
            'numero_serial': armamento.numero_serial,
            'numero_salvo': armamento.numero_salvo,
            'fecha_vencimiento': armamento.fecha_vencimiento,
            'estado': armamento.estado,
            'calibre': armamento.calibre,
            'fabricante': armamento.fabricante,
            'numero_cartuchos': armamento.numero_cartuchos,
            'id_tipo_armamento': armamento.id_tipo_armamento
        })
    return jsonify(armamento_list), 200

@armamento_bp.route('/<int:id_armamento>', methods=['GET'])
@token_requerido
@cargo_requerido(['Administrador', 'Supervisor', 'Gerente'])
def get_armamento_by_id(id_armamento):
    armamento = Armamento.get_by_id(id_armamento)
    if armamento:
        armamento_data = {
            'id_armamento': armamento.id_armamento,
            'numero_serial': armamento.numero_serial,
            'numero_salvo': armamento.numero_salvo,
            'fecha_vencimiento': armamento.fecha_vencimiento,
            'estado': armamento.estado,
            'calibre': armamento.calibre,
            'fabricante': armamento.fabricante,
            'numero_cartuchos': armamento.numero_cartuchos,
            'id_tipo_armamento': armamento.id_tipo_armamento
        }
        return jsonify(armamento_data), 200
    else:
        return jsonify({'error': 'Armamento no encontrado'}), 404

@armamento_bp.route('/', methods=['POST'])
@token_requerido
@cargo_requerido(['Administrador', 'Supervisor', 'Gerente'])
def create_armamento():
    data = request.get_json()
    armamento = Armamento(
        numero_serial=data['numero_serial'],
        numero_salvo=data['numero_salvo'],
        fecha_vencimiento=data['fecha_vencimiento'],
        estado=data['estado'],
        calibre=data['calibre'],
        fabricante=data['fabricante'],
        numero_cartuchos=data['numero_cartuchos'],
        id_tipo_armamento=data['id_tipo_armamento']
    )

    try:
        int(armamento.numero_cartuchos)
    except ValueError:
        return jsonify({'error': 'El número de cartuchos debe ser un entero'}), 400
    
    try:
        float(armamento.calibre)
    except ValueError:
        return jsonify({'error': 'El calibre debe ser un número'}), 400
    
    if armamento.numero_serial == '':
        return jsonify({'error': 'El número de serial no puede estar vacío'}), 400
    if armamento.numero_salvo == '':
        return jsonify({'error': 'El número de salvo no puede estar vacío'}), 400
    if armamento.estado == '':
        return jsonify({'error': 'El estado no puede estar vacío'}), 400
    if armamento.fabricante == '':
        return jsonify({'error': 'El fabricante no puede estar vacío'}), 400
    
    serial = Armamento.get_by_numero_serial(armamento.numero_serial)
    if serial:
        return jsonify({
            'error': 'No puedes ingresar este número de serial ya que se encuentra registrado en la base de datos.'
        }), 400
    
    salvo = Armamento.get_by_numero_salvo(armamento.numero_salvo)
    if salvo:
        return jsonify({
            'error': 'este numero de salvoconducto ya se encuentra registrado en la base de datos.'
        })


    armamento.save()
    return jsonify({'message': 'Armamento creado exitosamente', 'armamento': armamento.to_dict()}), 201


@armamento_bp.route('/<int:id_armamento>', methods=['PUT'])
@token_requerido
@cargo_requerido(['Administrador', 'Supervisor', 'Gerente'])
def update_armamento(id_armamento):
    armamento = Armamento.get_by_id(id_armamento)
    if not armamento:
        return jsonify({'error': 'Armamento no encontrado'}), 404

    data = request.get_json()
    armamento.numero_serial = data.get('numero_serial', armamento.numero_serial)
    armamento.numero_salvo = data.get('numero_salvo', armamento.numero_salvo)
    armamento.fecha_vencimiento = data.get('fecha_vencimiento', armamento.fecha_vencimiento)
    armamento.estado = data.get('estado', armamento.estado)
    armamento.calibre = data.get('calibre', armamento.calibre)
    armamento.fabricante = data.get('fabricante', armamento.fabricante)
    armamento.numero_cartuchos = data.get('numero_cartuchos', armamento.numero_cartuchos)
    armamento.id_tipo_armamento = data.get('id_tipo_armamento', armamento.id_tipo_armamento)

    try:
        int(armamento.numero_cartuchos)
    except ValueError:
        return jsonify({'error': 'El número de cartuchos debe ser un entero'}), 400
    
    try:
        float(armamento.calibre)
    except ValueError:
        return jsonify({'error': 'El calibre debe ser un número'}), 400
    
    
    serial = Armamento.get_by_numero_serial(armamento.numero_serial)
    if serial and serial.id_armamento != id_armamento:
        return jsonify({
            'error': 'No puedes ingresar este número de serial ya que se encuentra registrado en la base de datos.'
        }), 400

    salvo = Armamento.get_by_numero_salvo(armamento.numero_salvo)
    if salvo and salvo.id_armamento != id_armamento:
        return jsonify({
            'error': 'este numero de salvoconducto ya se encuentra registrado en la base de datos.'
        }), 400


    if armamento.numero_serial == '':
        return jsonify({'error': 'El número de serial no puede estar vacío'}), 400
    if armamento.numero_salvo == '':
        return jsonify({'error': 'El número de salvo no puede estar vacío'}), 400
    if armamento.estado == '':
        return jsonify({'error': 'El estado no puede estar vacío'}), 400
    if armamento.fabricante == '':
        return jsonify({'error': 'El fabricante no puede estar vacío'}), 400


 

    armamento.save()
    return jsonify({'message': 'Armamento actualizado exitosamente', 'armamento': armamento.to_dict()}), 200
    
