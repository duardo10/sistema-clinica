import mysql.connector
class Cadastro:
    def __init__(self):
         # configurações da conexão com o banco de dados 
        self.connection = mysql.connector.connect(
            user = 'root',
            password = '',
            host = 'localhost',
            database = 'clinica',
        )
        
    def cadastroMedico(self, pessoa):  
        verifica = self.buscarMedico(pessoa)    
        if verifica == None:  
            return True
        else:
            return False
        
        
    def cadastroRecep(self, pessoa):
        verifica = self.buscarRecep(pessoa)    
        if verifica == None:  
            return True
        else:
            return False
        
    def cadastroAdmin(self, pessoa):
        verifica = self.buscarAdmin(pessoa)    
        if verifica == None:  
            return True
        else:
            return False


    def buscarMedico(self, cpf):
        cursor = self.connection.cursor() 
        cursor.execute("SELECT cpf FROM medico")
        selecionar = cursor.fetchall()
        print(selecionar)
        for dado in selecionar:
            if cpf == dado[0]:
                return cpf
        return None
    
    def buscarRecep(self, cpf):
        cursor = self.connection.cursor() 
        cursor.execute("SELECT cpf FROM recepcionista")
        selecionar = cursor.fetchall()
        print(selecionar)
        for dado in selecionar:
            if cpf == dado[0]:
                return cpf
        return None
    
    def buscarAdmin(self, cpf):
        cursor = self.connection.cursor() 
        cursor.execute("SELECT cpf_admin FROM admin")
        selecionar = cursor.fetchall()
        print(selecionar)
        for dado in selecionar:
            if cpf == dado[0]:
                return cpf
        return None
        

    