class Pessoa():
    """
    A classe pessoa é a classe Mae de paciente, os atributos utilizados foram cpf, nome, telefone e data de nascimento
    """
    __slots__ = ['_cpf','_nome','_telefone','_dt_nasc']
    def __init__(self, cpf, nome, telefone,dt_nasc):
        self._cpf = cpf
        self._nome = nome
        self._telefone = telefone
        self._telefone = dt_nasc
