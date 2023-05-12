from pessoa import Pessoa

"""
A classe Funcionario herda os atributos da classe pessoa. que representam os dados de um funcionario. com excessão do email
"""
class Funcionario(Pessoa):
    def __init__(self, cpf, nome, telefone, dt_nasc, email):
        super().__init__(cpf, nome, telefone, dt_nasc)
        self._email = email
    