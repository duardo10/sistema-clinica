from pessoa import Pessoa
class Paciente(Pessoa):
    __slots__ = ['_nome','_cpf','_endereco','_nascimento']
    def __init__(self, cpf, nome, telefone, dt_nasc, endereco, email=None):
        super().__init__(cpf, nome, telefone, dt_nasc)
        self._endereco = endereco
        self._email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def endereco(self):
        return self._endereco
    @property
    def cpf(self):
        return self._cpf
    @property
    def nascimento(self):
        return self._nascimento

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco