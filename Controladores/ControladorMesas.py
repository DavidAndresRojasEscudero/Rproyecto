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

    def delete(self,id):
            return self.repositorioMesas.delete(id)
