from flask import Blueprint, jsonify,request
import simplejson as json
from src.models.entities.Asistente import Asistente
from src.models.asistenteModel import asistenteModel

main = Blueprint("asistente_blueprint", __name__)



@main.route('/add/asistente', methods=['POST'])
def addAsistente():
    try:
        
        correo= request.json['correo']
        contra = request.json['contraseña']
        idSede = int(request.json['idSede'])
        
        affected_rows = asistenteModel.añadirAsistente(correo, contra, idSede)

        if affected_rows > 0:
            return jsonify(correo)
        else:
            return jsonify({'message': "Error on añadir Asistente"}),500
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/delete/Asistente/<correo>', methods=['DELETE'])
def quitarAsistente(correo):
    try:
        affected_rows = asistenteModel.deleteAsistente(correo)
        if affected_rows ==1:
            return jsonify(correo)
        else:
            return jsonify({'message': "No hay Asistente eliminado"}),500
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/getAsistente/<correoAsis>')
def getAsistente(correoAsis):
    try:


        affected_rows = asistenteModel.get_Asistente(correoAsis)

        return affected_rows  
    except Exception as ex:
        return jsonify({'message': str(ex)}),500