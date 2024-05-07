from flask import Blueprint, jsonify,request
from src.models.entities.profeGuia import profeGuia
from src.models.profesModel import profesModel
from src.models.entities.profe import profe

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
@main.route('/detalle')
def get_detalleEquipo():
    try:
        integrantes = profesModel.get_detalleEquipo()
        return jsonify(integrantes)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/detalleF/<sede>')
def get_detalleF(sede):
    try:
        
        integrantes = profesModel.get_detalleEquipo()
        profe = profesModel.get_Profes(sede)
        

        return jsonify({'profesGuia':integrantes,'profes':profe})
    except Exception as ex:
        return jsonify({'message': str(ex)}),500



@main.route('/add/profesorGuia', methods=['POST'])
def addProfeGuia():
    try:
        
        correo= request.json['correo']
        nombre = request.json['nombreCompleto']
        telefono = request.json['telefono']
        celular = request.json['celular']
        idSede = int(request.json['idSede'])
        foto = request.json['foto']
        contraseña = request.json['contraseña']
        codigoSede = request.json['codigoSede']
        coordinador = request.json['coordinador']
        
        profesorG = profeGuia(correo, nombre, 1,telefono, celular, idSede, foto, contraseña, codigoSede, coordinador)
        
        affected_rows = profesModel.añadirProfeGuia(profesorG)

        if affected_rows > 1:
            return jsonify(profesorG.correo)
        else:
            return jsonify({'message': "Error on Update Profesor"}),500
    except Exception as ex:
        return jsonify({'message': str(ex)}),500



@main.route('/update/', methods=['PUT'])
def update_profe():
    try:
        correo=request.json['correo']
        nombre = request.json['nombre']
        telefono = request.json['telefono']
        celular = request.json['celular']
        foto = request.json['foto']
        profesor = profe(correo, nombre, 1,telefono, celular, foto,1,1,1)

        affected_rows = profesModel.updateProfesor(profesor)

        if affected_rows ==1:
            return jsonify(profesor.correo)
        else:
            return jsonify({'message': "Error on Update Profesor"}),500
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

   
@main.route('/setCoordinador', methods=['PUT'])
def definirCoordinador():
    try:
        correo = request.json['correo']
        equipo = int(request.json['idEquipo'])

        affected_rows = profesModel.definirCoordinador(correo, equipo)

        if affected_rows ==1:
            return jsonify(correo)
        else:
            return jsonify({'message': "Error on definirCoordinador"}),500
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/addIntegrante', methods=['POST'])
def añadirIntegrante():
    try:
        correo = request.json['correo']
        equipo = int(request.json['idEquipo'])

        affected_rows = profesModel.añadirIntegrante(correo, equipo)

        if affected_rows ==1:
            return jsonify(correo)
        else:
            return jsonify({'message': "Error on añadir integrante"}),500
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/deleteIntegrante', methods=['DELETE'])
def quitarIntegrante():
    try:
        correo = request.json['correo']
        equipo = int(request.json['idEquipo'])

        affected_rows = profesModel.quitarIntegrante(correo, equipo)
        affected_rows += profesModel.quitarGuia(correo)

        if affected_rows ==1:
            return jsonify(correo)
        else:
            return jsonify({'message': "No hay integrante eliminado"}),500
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/deleteProfesor/<correo>', methods=['PUT'])
def darDeBajaProfesor(correo):
    try:
        affected_rows = profesModel.darDeBajaProfesor(correo)
        
        if affected_rows ==1:
            return jsonify(correo)
        else:
            return jsonify({'message': "Error on dar de bajar Profesor"}),500
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
@main.route('/add/profesor', methods=['POST'])
def addProfe():
    try:

        correo= request.json['correo']
        nombre = request.json['nombreCompleto']
        telefono = request.json['telefono']
        celular = request.json['celular']
        idSede = int(request.json['idSede'])
        foto = request.json['foto']

        affected_rows = profesModel.añadirProfe(correo, nombre, telefono, celular, idSede, foto)

        if affected_rows > 1:
            return jsonify(correo)
        else:
            return jsonify({'message': "Error on añadir Profesor"}),500
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
