#importação do banco de dados
import mysql.connector

# configurações da conexão com o banco de dados 
class Imprimir():
    def __init__(self):
         # configurações da conexão com o banco de dados 
        self.connection = mysql.connector.connect(
            user = 'root',
            password = '',
            host = 'localhost',
            database = 'clinica',
        )
    
    def buscRecep(self, cpf): 
            cursor = self.connection.cursor() 
            cursor.execute('SELECT cpf FROM recepcionista')
            dados = cursor.fetchall()   
            print(dados)
            for dado in dados:
                if cpf == dado[0]:
                    return cpf
            return None

    def buscMed(self, cpf):
            cursor = self.connection.cursor() 
            cursor.execute('SELECT cpf FROM medico')
            dados = cursor.fetchall()
            print(dados)
            for dado in dados:
                if cpf == dado[0]:
                    return cpf
            return None

    def buscFunc(self, cpf):
            cursor = self.connection.cursor() 
            cursor.execute('SELECT cpf_funcionario FROM funcionarios')
            dados = cursor.fetchall()
            print(dados)
            for dado in dados:
                if cpf == dado[0]:
                    return cpf
            return None

