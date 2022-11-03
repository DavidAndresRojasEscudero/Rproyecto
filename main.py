import pymongo
import certifi
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorMesas import ControladorMesas
from Controladores.ControladorPartido import ControladorPartidos
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorResultado import ControladorResultado


app = Flask(__name__)
cors = CORS(app)

miControladorPartidos = ControladorPartidos()
miControladorMesas = ControladorMesas()
miControladorCandidatos = ControladorCandidato()
miControladorResultado = ControladorResultado()


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

@app.route("/mesas/<string:id>", methods=['DELETE'])
def deleteMesa(id):
    jso = miControladorMesas.delete(id)
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


# Endpoint para mostrar un candidatos
@app.route("/candidatos", methods=['GET'])
def getCandidatos():
    jso = miControladorCandidatos.index()
    return jsonify(jso)


# Endpoint para mostrar un candidato por id
@app.route("/candidatos/<string:id>", methods=['GET'])
def getCandidato(id):
    jso = miControladorCandidatos.show(id)
    return jsonify(jso)


# Endpoint para crear un candidato

@app.route("/candidatos", methods=['POST'])
def crearCandidato():
    data = request.get_json()
    jso = miControladorCandidatos.create(data)
    return jsonify(jso)

# Endpoint para actualizar un candidato
@app.route("/candidatos/<string:id>", methods=['PUT'])
def actualizarCandidato(id):
    data = request.get_json()
    jso = miControladorCandidatos.update(id,data)
    return jsonify(jso)

# Endpoint para eliminar un candidato
@app.route("/candidatos/<string:id>", methods=['DELETE'])
def eliminarCandidato(id):
    jso = miControladorCandidatos.delete(id)
    return jsonify(jso)

@app.route("/candidatos/<string:id>/partido/<string:idPartido>", methods=['PUT'])
def asignarPartido(id,idPartido):
    jso = miControladorCandidatos.asignarPartido(id,idPartido)
    return jsonify(jso)

# Endpoint para mostrar un resultado
@app.route("/resultados", methods=['GET'])
def getResultados():
    jso = miControladorResultado.index()
    return jsonify(jso)

@app.route("/resultados/<string:id>", methods=['GET'])
def getResultado(id):
    jso = miControladorResultado.show(id)
    return jsonify(jso)


@app.route("/resultados/candidatos/<string:idCadidato>/mesas/<string:idMesa>", methods=['POST'])
def crearResultado(idCadidato,idMesa):
    data = request.get_json()
    print(data, idCadidato, idMesa)
    jso = miControladorResultado.create(data, idCadidato, idMesa)
    return jsonify(jso)

@app.route("/resultados/<string:id>/candidatos/<string:id_candidato>/mesas/<string:id_mesa>", methods=['PUT'])
def actualizarResultado(id,id_cadidato,id_mesa):
    data = request.get_json()
    jso = miControladorResultado.update(id, data, id_cadidato, id_mesa)
    return jsonify(jso)

@app.route("/resultados/<string:id>", methods=['DELETE'])
def eliminarResultado(id):
    jso = miControladorResultado.delete(id)
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
