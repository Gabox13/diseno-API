from flask import Flask
from flask_cors import CORS
from src.routes import Profesores
from src.routes import Planes
from src.routes import excel
from src.routes import Asistentes

app = Flask(__name__)
CORS(app)
@app.route('/')
def hello_world():
    return 'Hello world!'


def page_not_found(error):
    return "<h1>Pagina no encontrada</h1>", 404


if __name__ == '__main__':

    app.register_blueprint(Profesores.main, url_prefix='/profes')
    app.register_blueprint(Planes.main, url_prefix='/planes')
    app.register_blueprint(excel.main, url_prefix='/excel')
    app.register_blueprint(Asistentes.main, url_prefix='/asistentes')
    app.register_error_handler(404, page_not_found)
    app.run(debug=True,host='0.0.0.0',port =5000,ssl_context='adhoc')
