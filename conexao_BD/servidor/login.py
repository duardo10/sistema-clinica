import mysql.connector
class Login:
    def __init__(self):
         # configurações da conexão com o banco de dados 
        self.connection = mysql.connector.connect(
            user = 'root',
            password = '',
            host = 'localhost',
            database = 'clinica',
        )
    def fazerLoginRecep(self, cpf, password):
        verifica = self.verificaLoginRecep(cpf, password)    
        if verifica == None:  
            return False
        else:
            return True

    # verifica se o 
    def verificaLoginRecep(self, cpf, password):
        cursor = self.connection.cursor()
        self.connection.commit()
        cursor.execute("SELECT cpf,senha FROM recepcionista")
        selecionar = cursor.fetchall()
        for dado in selecionar:
            if dado[0] == cpf and dado[1] == password:
                return True
        return None
    
    def fazerLoginMed(self, cpf, password):
        verifica = self.verificaLoginMed(cpf, password)    
        if verifica == None:  
            return False
        else:
            return True

    # verifica se o 
    def verificaLoginMed(self, cpf, password):
        cursor = self.connection.cursor()
        self.connection.commit()
        cursor.execute("SELECT cpf,senha FROM medico")
        selecionar = cursor.fetchall()
        for dado in selecionar:
            if dado[0] == cpf and dado[1] == password:
                return True
        return None
    
    def fazerLoginAdmin(self, cpf, password):
        verifica = self.verificaLoginAdmin(cpf, password)    
        if verifica == None:  
            return False
        else:
            return True

    # verifica se o 
    def verificaLoginAdmin(self, cpf, password):
        cursor = self.connection.cursor()
        self.connection.commit()
        cursor.execute("SELECT cpf_admin,senha FROM admin")
        selecionar = cursor.fetchall()
        for dado in selecionar:
            if dado[0] == cpf and dado[1] == password:
                return True
        return None