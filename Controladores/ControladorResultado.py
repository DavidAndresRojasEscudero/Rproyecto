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


     def create(self, infoResultado, idMesa, idCandidato):
        nuevoResultado = Resultado(infoResultado)
        print(nuevoResultado)
        laMesa = Mesas(self.repositorioMesas.findById(idMesa))
        print(laMesa)
        elCandidato = Candidato(self.repositorioCandidato.findById(idCandidato))
        print(elCandidato)  
        nuevoResultado.mesa = laMesa      
        nuevoResultado.candidato = elCandidato        
        return self.repositorioResultado.save(nuevoResultado)
       

     def show(self, id):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

     """
     Modificación de resultado candidato y mesa
     """

     def update(self,id,infoResultado, idMesa, idCandidato):
        resultadoActual = Resultado(self.repositorioResultado.findById(id))
        resultadoActual.numero_votos=infoResultado["numero_votos"]
        laMesa = Mesas(self.repositorioMesas.findById(idMesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(idCandidato))  
        resultadoActual.mesa = laMesa      
        resultadoActual.candidato = elCandidato        
        return self.repositorioResultado.save(resultadoActual)
        

     def delete(self,id):
        return self.repositorioResultado.delete(id)

     def listarResultadosEnCandidato(self, idCandidato):
        return self.repositorioResultado.getListadoResultadosEnCandidato(idCandidato)

   
