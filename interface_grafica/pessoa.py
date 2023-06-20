class Pessoa:
    __slots__ = ['_nome','_cpf','_endereco','_dt_nascimento']
    def __init__(self, nome, cpf, endereco, dt_nascimento):
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco
        self._dt_nascimento = dt_nascimento

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, novo_endereco):
        self._endereco = novo_endereco