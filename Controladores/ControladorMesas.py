from Repositorios.RepositorioMesas import RepositorioMesas
from Modelos.Mesas import Mesas


class ControladorMesas(Mesas):
    def __init__(self):
        self.repositorioMesas = RepositorioMesas()

    def index(self):
        return self.repositorioMesas.findAll()

    def create(self, infoMesa):
        nuevaMesa = Mesas(infoMesa)
        return self.repositorioMesas.save(nuevaMesa)

    def show(self, id):
        laMesa = Mesas(self.repositorioMesas.findById(id))
        return laMesa.__dict__
    
    def update(self, id, infoMesa):
        print("Actualizando mesa con id ", id)
        mesaActual = Mesas(self.mesaRepositorio.findById(id))
        mesaActual.numero_Mesa = infoMesa["numero_mesa"]
        mesaActual.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        return self.mesaRepositorio.save(mesaActual)

    def delete(self,id):
            return self.repositorioMesas.delete(id)
