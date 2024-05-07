from flask import Blueprint, jsonify,request
import simplejson as json
from src.models.entities.actividad import actividad
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
@main.route('/actividades/<id>')
def get_ActividadesXPlan(id):
    try:
       
        planes = planesModel.get_ActividadesXPlan(id)
        return json.dumps(planes)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/add/actividad', methods=['POST'])
def addActividad():
    try:
        nombre = request.json['nombre']
        semana = int(request.json['semana'])
        link = request.json['link']
        tipo = request.json['tipo']
        modalidad = request.json['modalidad']
        fechaPub = request.json['fechaPublicacion']
        fechaRea = request.json['fechaRealizacion']
        afiche = request.json['afiche']
        estado = request.json['estado']
        observacion = request.json['observacion']
        fechaCancel = request.json['fechaCancelacion']
        participantes = request.json['participantes']
        idPlan = int(request.json['idPlan'])

       

        affected_rows = planesModel.añadirActividad(nombre, semana, link, tipo, modalidad, fechaPub, fechaRea, afiche, estado, idPlan)

        if affected_rows > 0:
            return jsonify(nombre)
        else:
            return jsonify({'message': "Error on anadir actividad"}),500
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/update/actividad/<idActividad>', methods=['PUT'])
def updateActividad(idActividad):
    try:
        nombre = request.json['nombre']
        semana = int(request.json['semana'])
        link = request.json['link']
        tipo = request.json['tipo']
        modalidad = request.json['modalidad']
        fechaPub = request.json['fechaPublicacion']
        fechaRea = request.json['fechaRealizacion']
        afiche = request.json['afiche']
        estado = request.json['estado']
        observacion = request.json['observacion']
        fechaCancel = request.json['fechaCancelacion']
        participantes = request.json['participantes']

       

        affected_rows = planesModel.modificarActividad(idActividad, nombre, semana, link, tipo, modalidad, fechaPub, fechaRea, afiche, estado, observacion, fechaCancel, participantes)

        if affected_rows > 0:
            return jsonify(idActividad)
        else:
            return jsonify({'message': "Error on modificar actividad"}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/add/fechaRecordatorio', methods=['POST'])
def addFechaRecordatorio():
    try:
        idActividad = int(request.json['idActividad'])
        fecha = request.json['fechaRecordatorio']
        affected_rows = planesModel.añadirFechaRecordatorio(idActividad, fecha)

        if affected_rows > 0:
            return jsonify(idActividad)
        else:
            return jsonify({'message': "Error on anadir recordatorio"}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/delete/fechaRecordatorio/<idFechaR>', methods=['DELETE'])
def deleteFechaRecordatorio(idFechaR):
    try:
        affected_rows = planesModel.borrarFechaRecordatorio(idFechaR)

        if affected_rows > 0:
            return jsonify(idFechaR)
        else:
            return jsonify({'message': "Error on borrar Recordatorio"}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/add/Responsable', methods=['POST'])
def addResponsable():
    try:
        idActividad = int(request.json['idActividad'])
        correo = request.json['correo']
        affected_rows = planesModel.añadirResponsable(correo, idActividad)

        if affected_rows > 0:
            return jsonify(correo)
        else:
            return jsonify({'message': "Error on anadir Responsable"}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/delete/Responsable', methods=['DELETE'])
def deleteResponsable():
    try:
        idActividad = int(request.json['idActividad'])
        correo = request.json['correo']
        affected_rows = planesModel.quitarResponsable(correo, idActividad)

        if affected_rows > 0:
            return jsonify(correo)
        else:
            return jsonify({'message': "Error on borrar Responsable"}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/add/Comentario', methods=['POST'])
def addComentario():
    try:
        idActividad = int(request.json['idActividad'])
        correo = request.json['correo']
        comment = request.json['comentario']
        
        #Comentario = comentario(correo,idActividad, comment)
        affected_rows = planesModel.comentar(correo,idActividad, comment)

        if affected_rows > 0:
            return jsonify(correo)
        else:
            return jsonify({'message': "Error on comentar"}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/add/Respuesta', methods=['POST'])
def addRespuesta():
    try:
        idComentario = int(request.json['idComentario'])
        correo = request.json['correo']
        replay = request.json['respuesta']
        
        affected_rows = planesModel.responder(correo,idComentario, replay)

        if affected_rows > 0:
            return jsonify(correo)
        else:
            return jsonify({'message': "Error on responder"}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/delete/Respuesta', methods=['DELETE'])
def deleteRespuesta():
    try:
        idComentario = int(request.json['idComentario'])
        correo = request.json['correo']
        affected_rows = planesModel.borrarRespuesta(correo, idComentario)

        if affected_rows > 0:
            return jsonify(correo)
        else:
            return jsonify({'message': "Error on borrar respuesta"}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/delete/comentario', methods=['DELETE'])
def deleteComentario():
    try:
        idComentario = int(request.json['idComentario'])
        correo = request.json['correo']
        idActividad = int(request.json['idActividad'])
        affected_rows = planesModel.borrarComentario(idComentario, correo, idActividad)

        if affected_rows > 0:
            return jsonify(correo)
        else:
            return jsonify({'message': "Error on borrar Comentario"}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500