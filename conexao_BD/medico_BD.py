import mysql.connector
class Medico():
    def __init__(self):
        # configurações da conexão com o banco de dados 
        self.connection = mysql.connector.connect(
            user = 'root',
            password = '',
            host = 'localhost',
            database = 'mydb',
        ) 
       
    def imprimir_pacientes(self, medico):
        cursor = self.connection.cursor()
        lista = "SELECT * FROM lista_pacientes WHERE medico = %s"
        cursor.execute(lista,(medico,))
        resultado = cursor.fetchall()
        self.connection.commit()
        if len(lista) != 0:
            return resultado
        else:
            return False
    
    def excluir(self):
        cursor = self.connection.cursor()
        selecione = "SELECT * FROM lista_pacientes ORDER BY id_paciente"
        cursor.execute(selecione)
        resultado = cursor.fetchone()
        self.connection.commit()
        if resultado is not None:
            excluido = "DELETE FROM lista_pacientes WHERE id_paciente = %s"
            cursor.execute(excluido,(resultado[0],))
            pacientes = cursor.fetchone()
            self.connection.commit()
            print(pacientes)
            print(f"O registro com ID {resultado[0]} foi excluído com sucesso.")
        else:
            print("A tabela está vazia ou não há registros para excluir.")
      
        #self.imprimir_pacientes(resultado[3])
        #self.connection.commit()

        
       
        
        