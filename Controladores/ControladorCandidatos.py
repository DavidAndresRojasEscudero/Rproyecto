from Rproyecto.Modelos.Candidatos import Candidatos


class ControladorCandidatos():

    def __int__(self):
        print("")

    def index(self):
        Candidato = {
            "no_resolucion": "123",
            "cedula_candidato": "12345",
            "nombre_candidato": "pepito",
            "apellido_candidato": "gonzales",
        }
        return [Candidato]

    def create(self, infoCandidato):
        Elcandidato = Candidatos(infoCandidato)
        return Elcandidato.__dict__


