from pessoa import Pessoa

class Paciente(Pessoa):
    """
    Na classe Paciente foi utilizada herança( um paciente é uma pessoa por isso herda atributos da classe pessoa)
    e recebe como atributos os dados do de uma pessoa, o atributo email é opcional(pode ou não ser informado).
    """
    def __init__(self, cpf, nome, telefone, dt_nasc, endereco, email=None):
        super().__init__(cpf, nome, telefone, dt_nasc)
        self._endereco = endereco
        self._email = email