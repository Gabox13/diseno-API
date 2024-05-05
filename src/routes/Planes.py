from flask import Blueprint, jsonify

from src.models.planesModel import planesModel

main = Blueprint("planes_blueprint", __name__)

"""agregar parametro"""
@main.route('/')
def get_PlanesXEquipo():
    try:
       
        planes = planesModel.get_PlanesXEquipo()
        return jsonify(planes)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

