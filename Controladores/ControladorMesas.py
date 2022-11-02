from Modelos.Mesas import Mesas


class ControladorMesas():
    def __init__(self):
        print("")

    def index(self):
        MesasR ={
            "_id": "1",
            "cedulas_registradas": "123456789",
            }
        return [MesasR]

    def create(self, infoMesa):
        LaMesa = Mesas(infoMesa)
        return LaMesa.__dict__

    def show(self, id):
        laMesa = {
            "_id": "1",
            "cedulas_registradas": "123456789",
        }
        return laMesa

    # funsion para actualizar un estudiante
    # def update(self,id,infoEstudiante):
    #   print("Actualizando estudiante con id", id)
    #  elEstudiante=Estudiante(infoEstudiante)
    # return elEstudiante.__dict__

    # funsion para eliminar un estudiante
    # def delete(self,id):
    #   print("eliminando estudiante con id",id)
    #  return {"deleted_count": 1}
