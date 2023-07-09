from pessoa import Pessoa
class Paciente(Pessoa):
    __slots__ = ['_cpf','_nome','_telefone','_dt_nasc','_endereco','_email']
    def __init__(self, cpf, nome, telefone, dt_nasc, endereco, email=None):
        super().__init__(cpf, nome, telefone, dt_nasc)
        self._endereco = endereco
        self._email = email

    @property
    def cpf(self):
        return self._cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone
    
    @property
    def dt_nasc(self):
        return self._dt_nasc

    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email
