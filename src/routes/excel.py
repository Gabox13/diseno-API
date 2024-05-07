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

@main.route('/recuperar/')
def recuperar_Excel():
    try:
        
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
