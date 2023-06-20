from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget
import mysql.connector
class MedicoFunc():
    def __init__(self):
        # configurações da conexão com o banco de dados 
        self.connection = mysql.connector.connect(
            user = 'root',
            password = '',
            host = 'localhost',
            database = 'clinica',
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
    
    def excluir(self, cpf):
        print(cpf)
        cursor = self.connection.cursor()
        selecione = "SELECT * FROM lista_pacientes WHERE medico_cpf = %s ORDER BY id_paciente LIMIT 1"
        cursor.execute(selecione,(cpf,))
        resultado = cursor.fetchone()
        print(resultado)
        if resultado is not None:
            excluido = "DELETE FROM lista_pacientes WHERE id_paciente = %s"
            cursor.execute(excluido,(resultado[0],)) 
            pacientes = cursor.fetchone()
            self.connection.commit()
            print(pacientes)
            QtWidgets.QMessageBox.information(None, 'interface', f"O registro com ID {resultado[0]} foi excluído com sucesso.")
        else:
            QtWidgets.QMessageBox.information(None, 'interface', "A tabela está vazia ou não há registros para excluir.")
       

    def buscarPacientes(self,cpf_medico):
        pass

    def atualizaConsulta(self,cpf):
        cursor = self.connection.cursor()
        selecione = "SELECT tipo_consulta FROM consulta WHERE cpf_paciente = %s"
        cursor.execute(selecione,(cpf,))
        resultado = cursor.fetchone()
        print(resultado)
        if resultado is not None:       
            if resultado[0] != 'retorno':
                atualiza = "UPDATE consulta SET tipo_consulta = 'retorno' WHERE cpf_paciente = %s"
                cursor.execute(atualiza,(cpf,))
                QtWidgets.QMessageBox.information(None, 'interface', f"A consulta foi atualizada para o RETORNO")
                #confirmar a inserção
                self.connection.commit()
            else:
                QtWidgets.QMessageBox.information(None, 'interface', f"A consulta já é RETORNO")
        else:
            QtWidgets.QMessageBox.information(None, 'interface', f"A consulta não foi encontrada!")

      
        #self.imprimir_pacientes(resultado[3])
        #self.connection.commit()

        
       
        
        