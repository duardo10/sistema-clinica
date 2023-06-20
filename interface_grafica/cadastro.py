class Cadastro:
    __slots__ = ['_lista_pessoas']
    def __init__(self):
        self._lista_pessoas = []

    
    def cadastro(self, pessoa):  
        verifica = self.buscar(pessoa._cpf)    
        if verifica == None:
            self._lista_pessoas.append(pessoa)
            return True
        else:
            return False


    def buscar(self, cpf):
        for nome in self._lista_pessoas:
            if nome._cpf == cpf:
                return nome
            return None
        

    