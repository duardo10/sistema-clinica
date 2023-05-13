from funcionario import Funcionario

class Recepcionista(Funcionario):
    """
    Na classe recepcionista foi utilizada herança( um recepcionista é um funcionario por isso herda atributos da classe funcionario)
    e recebe como atributos os dados do recepcionista.
    """
    def __init__(self, cpf, nome, telefone, dt_nasc, email):
        super().__init__(cpf, nome, telefone, dt_nasc, email)

    def imprimir(self):
        print('CPF: ', self._cpf)
        print('Nome: ', self._nome)
        print('Telefone: ', self._telefone)
        print('Data de nascimento: ', self._dt_nasc)
        print('Email: ',self._email)

    
    