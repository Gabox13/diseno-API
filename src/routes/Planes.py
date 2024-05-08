from flask import Blueprint, jsonify,request
import simplejson as json
from src.models.entities.actividad import actividad
from src.models.entities.ActividadFactory import ActividadFactory
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

@main.route('/actividadProxima')
def get_ActividadProxima():
    try:
       
        planes = planesModel.get_ActividadProxima()
        return json.dumps(planes)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/add/actividad', methods=['POST'])
def addActividad():
    try:

        nombre = request.json['valoresGenerales']['nombre']
        print(nombre)
        print("aqui")
        semana = int(request.json['valoresGenerales']['semana'])
        link = request.json['valoresGenerales']['direccion']
        tipo = request.json['valoresGenerales']['tipo']
        modalidad = request.json['valoresGenerales']['modalidad']
        fechaPub = request.json['valoresGenerales']['fechaPublicacion']
        fechaRea = request.json['valoresGenerales']['fechaRealizacion']
        afiche = request.json['valoresGenerales']['afiche']
        estado = request.json['valoresGenerales']['estado']
        idPlan = int(request.json['idPlan'])
        fechaRec = request.json['valoresGenerales']['fechaRecordatorio']
        responsables = request.json['valoresGenerales']['responsables']
        
        act = ActividadFactory.crear_actividad(1000,nombre,semana,link,tipo,modalidad
                 ,fechaPub,fechaRea,afiche,estado,fechaRec)
        print(act)
        affected_rows, idActividad = planesModel.añadirActividad(act, idPlan)
        
        for respon in responsables:
            affected_rows += planesModel.añadirResponsable(respon['correo'], idActividad)
        for fecR in fechaRec:
            affected_rows += planesModel.añadirFechaRecordatorio(idActividad, fecR['fechaR'])
        if affected_rows > 0:
            return jsonify(nombre)
        else:
            return jsonify({'message': "Error on anadir actividad"}),500
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/update/actividad', methods=['PUT'])
def updateActividad():
    try:
        idActividad =int(request.json['valoresGenerales']['idActividad'])
        nombre = request.json['valoresGenerales']['nombre']
        semana = int(request.json['valoresGenerales']['semana'])
        link = request.json['valoresGenerales']['direccion']
        tipo = request.json['valoresGenerales']['tipo']
        modalidad = request.json['valoresGenerales']['modalidad']
        fechaPub = request.json['valoresGenerales']['fechaPublicacion']
        fechaRea = request.json['valoresGenerales']['fechaRealizacion']
        afiche = request.json['valoresGenerales']['afiche']
        estado = request.json['valoresGenerales']['estado']
        fechaRec = request.json['valoresGenerales']['fechaRecordatorio']
        fechaCancelacion = request.json['fechaCancelacion']
        fotos = request.json['fotos']
        observacion = request.json['descripcionCancelacion']
        profesRespons = request.json['profesoresAgregados']
        profesResponsQ = request.json['profesoresEliminados']
        fechasRecAgregar = request.json['fechasAgregadas']
        fechasRecQ = request.json['fechasEliminadas']

        act = ActividadFactory.crear_actividad(idActividad,nombre,semana,link,tipo,modalidad
                 ,fechaPub,fechaRea,afiche,estado,fechaRec, descripcion_cancelacion=observacion, fecha_cancelacion=fechaCancelacion)
        affected_rows = planesModel.modificarActividad(act)

        for responq in profesResponsQ:
            affected_rows += planesModel.quitarResponsable(responq['correo'], idActividad)

        for respon in profesRespons:
            affected_rows += planesModel.añadirResponsable(respon['correo'], idActividad)
       
        for fecRq in fechasRecQ:
            affected_rows += planesModel.borrarFechaRecordatorio(fecRq['idFecRec'])

        for fecR in fechasRecAgregar:
            affected_rows += planesModel.añadirFechaRecordatorio(idActividad, fecR['fechaR'])
        
        planesModel.quitarFotos(idActividad)
        for foto in fotos:
            affected_rows += planesModel.añadirFotos(idActividad, foto['ruta'])

        if affected_rows > 0:
            return jsonify(idActividad)
        else:
            return jsonify({'message': "Error on modificar actividad"}),404
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