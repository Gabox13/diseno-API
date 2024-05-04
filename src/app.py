from flask import Flask
from routes import Profesores
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def page_not_found(error):
    return "<h1>Pagina no encontrada</h1>", 404


if __name__ == '__main__':

    app.register_blueprint(Profesores.main, url_prefix='/profes')

    app.register_error_handler(404, page_not_found)
    app.run(debug=True)
