
"""
A classe Funcionario é a classe mãe. que representam os dados de um funcionario. com excessão do email
"""
class Funcionario():
    def __init__(self, cpf, nome, telefone, dt_nasc, email):
        self._cpf = cpf
        self._nome = nome
        self._telefone = telefone
        self._dt_nasc = dt_nasc
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

    @dt_nasc.setter
    def dt_nasc(self, dt_nasc):
        self._dt_nasc = dt_nasc
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email
    

    