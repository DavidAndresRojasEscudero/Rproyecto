from Modelos.Partidos import Partidos


class ControladorPartidos(Partidos):
    def __init__(self):
        print("")

    def index(self):
        unPartido ={
                "_id": "1",
                "nombre_partido": "Partido liberal",
                "Lema": "Equidad para todos"
            }

        return [unPartido]

    def create(self, infoPartido):
        elPartido = Partidos(infoPartido)
        return elPartido.__dict__

    def show(self, id):
        elPartido = {"_id": id,
                "nombre_partido": "Partido liberal",
                "Lema": "Equidad para todos"}
        return elPartido
