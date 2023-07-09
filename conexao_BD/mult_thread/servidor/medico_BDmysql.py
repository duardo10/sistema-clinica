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
       

    def buscarPacientes(self,cpf_paciente,cpf_medico):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cpf_paciente FROM consulta WHERE cpf_paciente = %s AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1",(cpf_paciente, cpf_medico,))
        resultado = cursor.fetchall()
        print(resultado)

        for dado in resultado:
            if cpf_paciente== dado[0]:
                return cpf_paciente
        return None

    def atualizaConsulta(self,cpf,cpf_medico):
        cursor = self.connection.cursor()
        selecione = "SELECT tipo_consulta FROM consulta WHERE cpf_paciente = %s AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1"
        cursor.execute(selecione,(cpf,cpf_medico))
        resultado = cursor.fetchone()
        print(resultado)
        if resultado is not None:       
            if resultado[0] != 'retorno':
                atualiza = "UPDATE consulta SET tipo_consulta = 'retorno' WHERE cpf_paciente = %s  AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1"
                cursor.execute(atualiza,(cpf,cpf_medico,))
                
                #confirmar a inserção
                self.connection.commit()
                return True
            elif resultado[0] == 'retorno':
                atualiza = "UPDATE consulta SET tipo_consulta = 'nova' WHERE cpf_paciente = %s  AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1"
                cursor.execute(atualiza,(cpf,cpf_medico,))
                
                #confirmar a inserção
                self.connection.commit()
                return False
            else:
                print('ERRO')
                
        else:
            return None
        
        
    

      
        #self.imprimir_pacientes(resultado[3])
        #self.connection.commit()

        
       
        
        