from funcionario import Funcionario

class Recepcionista(Funcionario):
    """
    Na classe recepcionista foi utilizada herança( um recepcionista é um funcionario por isso herda atributos da classe funcionario)
    e recebe como atributos os dados do recepcionista.
    """
    def __init__(self, cpf, nome, telefone, dt_nasc, email, senha):
        super().__init__(cpf, nome, telefone, dt_nasc, email)
        self._senha = senha

    @property
    def cpf(self):
        return self._cpf
  

    
    