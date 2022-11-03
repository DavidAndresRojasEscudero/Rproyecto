from Modelos.Resultado import Resultado
from Modelos.Candidato import Candidato
from Modelos.Mesas import Mesas
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesas import RepositorioMesas

class ControladorResultado():
     def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesas = RepositorioMesas()

     def index(self):
        return self.repositorioResultado.findAll()

     """
     Asignacion candidato y mesa a resultado
     """    


     def create(self, infoResultado, idCandidato, idMesa):
        nuevoResultado = Resultado(infoResultado)
        print(nuevoResultado)
        elCandidato = Candidato(self.repositorioCandidato.findById(idCandidato))
        print(elCandidato)
        laMesa = Mesas(self.repositorioMesas.findById(idMesa))
        print(laMesa)
        nuevoResultado.candidato = elCandidato
        nuevoResultado.mesa = laMesa
        return self.repositorioResultado.save(nuevoResultado)
       

     def show(self, id):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

     """
     Modificación de resultado candidato y mesa
     """

     def update(self,id,infoResultado, idCandidato, idMesa):
        resultadoActual = Resultado(self.repositorioResultado.findById(id))
        resultadoActual.numero_votos=infoResultado["numero_votos"]
        elCandidato = Candidato(self.repositorioCandidato.findById(idCandidato))
        laMesa = Mesas(self.repositorioMesas.findById(idMesa))
        resultadoActual.candidato = elCandidato
        resultadoActual.mesa = laMesa
        return self.repositorioResultado.save(resultadoActual)
        

     def delete(self,id):
        return self.repositorioResultado.delete(id)
