from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorMesas import ControladorMesas
from Controladores.ControladorPartido import ControladorPartidos

app = Flask(__name__)
cors = CORS(app)

miControladorPartidos = ControladorPartidos()
miControladorMesas = ControladorMesas()


@app.route("/", methods=['GET'])
def test():
    dicc = {"Test:": "Servidor en ejecucion"}
    return jsonify(dicc)


# Endpoint para mostrar todas las mesas

@app.route("/mesas", methods=['GET'])
def getMesas():
    jso = miControladorMesas.index()
    return jsonify(jso)


# Endpoint para mostrar una mesa por su id
@app.route("/mesas/<string:id>", methods=['GET'])
def getMesa(id):
    jso = miControladorMesas.show(id)
    return jsonify(jso)


# Endpoint para crear una mesa

@app.route("/mesas", methods=['POST'])
def crearMesa():
    data = request.get_json()
    jso = miControladorMesas.create(data)
    return jsonify(jso)


####################
@app.route("/partidos", methods=['GET'])
def getPartidos():
    jso = miControladorPartidos.index()
    return jsonify(jso)


# Endpoint para mostrar un partido
@app.route("/partidos/<string:id>", methods=['GET'])
def getPartido(id):
    jso = miControladorPartidos.show(id)
    return jsonify(jso)


# Endpoint para crear un partido

@app.route("/partidos", methods=['POST'])
def crearPartido():
    data = request.get_json()
    jso = miControladorPartidos.create(data)
    return jsonify(jso)


# Endpoint para actualizar un estudiante
# @app.route("/estudiantes/<string:id>", methods=['PUT'])
# def modificarEstudiante(id):
#   data = request.get_json()
#  jso = miControladorEstudiante.update(id, data)
# return jsonify(jso)


# Endpoint para eliminar un estudiante
# @app.route("/estudiantes/<string:id>", methods=['DELETE'])
# def eliminarEstudiante(id):
#   jso = miControladorEstudiante.delete(id)
#  return jsonify(jso)


# leer archivo json
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + " http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])

# aqui
