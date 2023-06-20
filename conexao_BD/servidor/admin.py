
"""
A classe Funcionario é a classe mãe. que representam os dados de um funcionario. com excessão do email
"""
class Admin():
    def __init__(self, cpf_admin, nome, senha):
        self._cpf_admin = cpf_admin
        self._nome = nome
        self._senha = senha
    
    @property
    def cpf_admin(self):
        return self._cpf_admin

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha
