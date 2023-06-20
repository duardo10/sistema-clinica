from pessoa import Pessoa
class Cadastro:
    __slots__ = ['_lista_pessoas']
    
    def __init__(self):
        self._lista_pessoas = []

    
    def cadastro(self, pessoa):  
        existe = self.buscar(pessoa._cpf)
        print(existe)
        if existe == None:
            self._lista_pessoas.append(pessoa)
            return True
        else:
            return False


    def buscar(self, cpf):
        for lp in self._lista_pessoas:
            if lp._cpf == cpf:
                return lp
            
        return None
        

    