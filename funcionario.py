
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
    