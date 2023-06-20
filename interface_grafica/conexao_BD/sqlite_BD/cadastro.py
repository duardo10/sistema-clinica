import sqlite3


class Cadastro:
    
    def cadastro(self, pessoa):
        conexao = sqlite3.connect('teste.sqlite')
        cursor = conexao.cursor()
        
        busc = self.buscar(pessoa)
        cursor.close()
        conexao.commit()
        conexao.close()
        if busc == None:
            return True
        else:
            return False
        
        
        
       


    def buscar(self, cpf):
        conexao = sqlite3.connect('teste.sqlite')
        cursor = conexao.cursor()
        cursor.execute('SELECT cpf FROM usuarios')
        dados = cursor.fetchall()
        cursor.close()
        conexao.commit()
        conexao.close()
        print(dados)
        for dado in dados:
            if cpf == dado[0]:
                return cpf
        return None
        


        

    