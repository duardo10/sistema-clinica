from funcionario import Funcionario

class Recepcionista(Funcionario):
    """
    Na classe recepcionista foi utilizada herança( um recepcionista é um funcionario por isso herda atributos da classe funcionario)
    e recebe como atributos os dados do recepcionista.
    """
    def __init__(self, cpf, nome, telefone, dt_nasc, email):
        super().__init__(cpf, nome, telefone, dt_nasc, email)

    