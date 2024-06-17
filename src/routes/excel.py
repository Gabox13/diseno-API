from flask import Blueprint, jsonify,request

from src.models.excelModel import excelModel

main = Blueprint("excel_blueprint", __name__)


@main.route('/subir',methods=['POST'])
def add_Excel():
    try:
        
        filasAfectadas=excelModel.add_Excel(request.json)
        return jsonify(filasAfectadas)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/recuperar')
def recuperar_Excel():
    try:
        print("aqui")
        estudiantesExcel=excelModel.recuperar_Excel()
        return jsonify(estudiantesExcel)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/recuperarGrupoSede/<idSede>')
def recuperar_ExcelSede(idSede):
    try:
        
        estudiantesExcel=excelModel.recuperar_GrupoSede(idSede)
        return jsonify(estudiantesExcel)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
@main.route('/recuperarTodos')
def recuperar_todos():
    try:
        
        estudiantesExcel=excelModel.recuperar_todos()
        return jsonify(estudiantesExcel)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
@main.route('/InicioEstudiante/<correo>')
def iniciar_sesion_estudiante(correo):
    try:
        
        estudianteCargado=excelModel.inicio_sesion_es(correo)
        return jsonify(estudianteCargado)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500 
@main.route('/recuperarNotificaciones/<usuario>')
def recuperar_Notificaciones(usuario):
    try:
        
        notificaciones=excelModel.recuperar_notificaciones(usuario)
        return jsonify(notificaciones)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500    

    