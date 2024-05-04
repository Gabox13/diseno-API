from flask import Blueprint, jsonify

from models.profesModel import profesModel

main = Blueprint("profesores_blueprint", __name__)


@main.route('/<id>')
def get_profes(id):
    try:
       
        profes = profesModel.get_Profes(id)
        return jsonify(profes)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/guia/<correo>')
def get_profeGuia(correo):
    try:
        profe = profesModel.get_ProfeGuia(correo)
        return profe
    except Exception as ex:
        return jsonify({'message': str(ex)}),500