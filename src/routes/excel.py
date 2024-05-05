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

@main.route('/recuperar/<nombreExcel>')
def recuperar_Excel(nombreExcel):
    try:
        
        estudiantesExcel=excelModel.recuperar_Excel(nombreExcel)
        return jsonify(estudiantesExcel)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

