from Modelos.Partidos import Partidos
from Repositorios.RepositorioPartido import RepositorioPartidos


class ControladorPartidos(Partidos):
    def __init__(self):
        self.RepositorioPartidos = RepositorioPartidos()

    def index(self):
        return self.RepositorioPartidos.findAll()

    def create(self, infoPartido):
        nuevoPartido = Partidos(infoPartido)
        return self.RepositorioPartidos.save(nuevoPartido)

    def show(self, id):
        elPartido  = Partidos(self.RepositorioPartidos.findById(id))
        return elPartido.__dict__

    def update(self, id, infoPartido):
        print("Actualizando Partido con id ", id)
        partidoActual = Partidos(self.RepositorioPartidos.findById(id))
        partidoActual.nombre = infoPartido["nombre"]
        partidoActual.lema = infoPartido["lema"]
        return self.RepositorioPartidos.save(partidoActual)

    def delete(self, id):
        return self.RepositorioPartidos.delete(id)
