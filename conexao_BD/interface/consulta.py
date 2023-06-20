from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget
import mysql.connector

class Consulta():
    def __init__(self):
        # configurações da conexão com o banco de dados 
        self.connection = mysql.connector.connect(
            user = 'root',
            password = '',
            host = 'localhost',
            database = 'clinica',
        )
    def verificar_tipo(self,cpf):
        """
        A função de verificar o tipo de consulta se é uma nova consulta ou se é o retorno do paciente ao médico:
        se a consulta for do tipo retorno ela retorna False é porque o paciente já pagou a consulta, portanto não é cobrado nenhum
        valor para a consulta. Mas se for uma nova consulta a função retorna True e então é cobrado na recepção o valor da consulta
        #parâmetros:#
            - sem parâmetros
        #retorno#
            - boll = True ou False
        """
        retorno = self.buscConsulta(cpf)
        if retorno:
            try:
                cursor = self.connection.cursor()
                
                sql = "SELECT tipo_consulta FROM consulta WHERE cpf_paciente = %s"
                cursor.execute(sql,(cpf,))
                tipo_consulta = cursor.fetchone()
                self.connection.commit()
                if tipo_consulta[0] == 'retorno':
                    return False
                else:
                    return True
                
            except mysql.connector.Error as error:
                QtWidgets.QMessageBox.information(None, 'interface', f'Eroo ao verificar um dado: {error}')
            finally:
                cursor.close()
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'CPF não encontrado')

    def excluir_consulta(self, cpf_paciente):
        # A função de excluir uma consulta recebe como parâmetros o cpf do cliente para que após 30 dias da primieira consulta
        # se o paciente não tiver voltado para o retorno, o recepcionista excluir os dados do paciente. caso o cliente tenha
        # retornado antes dos 30 dias. após o retorno já é excluido imediatamente os dados do cliente. 
        retorno = self.buscConsulta(cpf_paciente)
        print(retorno)
        if retorno:
            try:
                cursor = self.connection.cursor()
                sql = "DELETE FROM consulta WHERE cpf_paciente = %s"
                cursor.execute(sql,(cpf_paciente,))
                self.connection.commit()
                QtWidgets.QMessageBox.information(None, 'interface', 'Dado excluido')
            except mysql.connector.Error as error:
                QtWidgets.QMessageBox.information(None, 'interface', f'Eroo ao excluir um dado: {error}')
            finally:
                cursor.close()
        else:
            QtWidgets.QMessageBox.information(None, 'interface','Paciente não encontrado!')

    def vagas_disponiveis(self, medico):
        try:
            cursor = self.connection.cursor()
            medico_responsavel = "SELECT medico, qtd_vagas FROM consulta"
            cursor.execute(medico_responsavel)
            selecionar = cursor.fetchall()
            for dado in selecionar:
                if dado[0] == medico:
                    qtd_vagas = dado[1]
                    menssagem = 'Quantidade de vagas: '+ str(qtd_vagas)
                    QtWidgets.QMessageBox.information(None, 'interface', str(menssagem))
                    if qtd_vagas == 0:
                        return False
                    else:
                        return qtd_vagas
        
        except mysql.connector.Error as error:
            QtWidgets.QMessageBox.information(None, 'interface', f'Eroo ao atualizar a quantidade de vagas de um medico no banco de dados: {error}')
        finally:
            cursor.close()

    def enviar_consulta(self):
        # A função de enviar uma consulta recebe como parâmetro uma consulta que deve ser enviada pelo recepcionista para o
        # médico responsável pelo paciente.
        self.connection.commit()
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM consulta ORDER BY id_consulta DESC LIMIT 1")
            ultimo_elemento = cursor.fetchone()
            print(ultimo_elemento)
           
            retorno = self.vagas_disponiveis(ultimo_elemento[5])
            print('vagas:', retorno)
            if retorno == False:
                QtWidgets.QMessageBox.information(None, 'interface', 'Não há mais vagas para este médico') 
            else:
                cpf = ultimo_elemento[1]
                nome = ultimo_elemento[2]
                medico = ultimo_elemento[9]
                result = self.buscMedico(medico)
                print(result)
                
                if result == None:
                    QtWidgets.QMessageBox.warning(None, "interface", 'Dados do Médico estão errados! verifique os campos.') 
                else:
                    result = self.buscarPaciente(cpf)
                    print('PROCURANDO:', result)
                    if result != None:
                        QtWidgets.QMessageBox.warning(None, "interface", 'O paciente já está na lista de pacientes do médico!')
                    else:
                        sql = "INSERT INTO lista_pacientes (cpf,nome,medico_cpf) VALUES (%s,%s,%s)"
                        try:
                            cursor.execute(sql,(cpf,nome,medico,))
                            self.connection.commit()
                            QtWidgets.QMessageBox.information(None, 'interface', 'Paciente enviado para a lista de pacientes')
                            retorno -= 1
                            atualiza =  "UPDATE consulta SET qtd_vagas = %s WHERE medico = %s"
                            cursor.execute(atualiza,(retorno,medico,))
                            self.connection.commit()
                            menssagem = 'Quantidade de vagas: '+ str(retorno)
                            QtWidgets.QMessageBox.information(None, 'interface', str(menssagem))
                            cursor.execute("SELECT qtd_vagas FROM consulta")
                            vagas = cursor.fetchall()
                            print('vagas:', vagas)
                        
                        except mysql.connector.errors.IntegrityError:
                                QtWidgets.QMessageBox.information(None, 'interface', 'Erro: O paciente ja esta na lista de pacientes!')
    

            """
            retorno = self.vagas_disponiveis(dado[5])
            if retorno == False:
                QtWidgets.QMessageBox.information(None, 'interface', 'Não há mais vagas para este médico') 
            else:
                menssagem = ('Quantidade de vagas: ', retorno)
                QtWidgets.QMessageBox.information(None, 'interface', menssagem)
                cpf = ultimo_elemento[1]
                nome = ultimo_elemento[2]
                medico = ultimo_elemento[4]
                sql = "INSERT INTO lista_pacientes (cpf,nome,medico) VALUES (%s,%s,%s)"
                cursor.execute(sql,(cpf,nome,medico,))
                self.connection.commit()

                QtWidgets.QMessageBox.information(None, 'interface', 'Paciente enviado para a lista de pacientes') 
            """
        except mysql.connector.Error as error:
            QtWidgets.QMessageBox.information(None, 'interface', f'Eroo ao enviar um dado para a lista de pacientes: {error}')
        finally:
            cursor.close()
    
    def verificaMedico(self,medico,crm,cpf_medico):
        cursor = self.connection.cursor()
        cursor.execute("SELECT nome,crm,cpf FROM medico WHERE nome = %s AND crm = %s AND cpf = %s",(medico,crm,cpf_medico))
        resultado = cursor.fetchall()
        print(resultado)

        for dado in resultado:
            if medico == dado[0] and int(crm) == dado[1] and cpf_medico == dado[2]:
                return True
        return None
    
    def verificaRecep(self,cpf_recepcionista):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cpf FROM recepcionista WHERE cpf = %s",(cpf_recepcionista,))
        resultado = cursor.fetchall()
        print(resultado)

        for dado in resultado:
            if cpf_recepcionista == dado[0]:
                return True
        return None
    
    def buscarPaciente(self,cpf):
        cursor = self.connection.cursor() 
        cursor.execute("SELECT cpf FROM lista_pacientes")
        selecionar = cursor.fetchall()
        print(selecionar)
        for dado in selecionar:
            if cpf == dado[0]:
                return cpf
        return None
        
    def buscMedico(self,cpf):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cpf FROM medico WHERE cpf = %s",(cpf,))
        resultado = cursor.fetchall()
        print(resultado)

        for dado in resultado:
            if cpf == dado[0]:
                return True
        return None

    def buscConsulta(self,cpf):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cpf_paciente FROM consulta WHERE cpf_paciente = %s",(cpf,))
        resultado = cursor.fetchall()
        print(resultado)

        for dado in resultado:
            if cpf == dado[0]:
                return cpf
        return None
    
    def buscPaciente(self, cpf):
        cursor = self.connection.cursor()
        cursor.execute("SELECT cpf_paciente FROM consulta WHERE cpf = %s",(cpf,))
        resultado = cursor.fetchall()
        print(resultado)

        for dado in resultado:
            if cpf == dado[0]:
                return cpf
        return None
        
        
    def fechar_conecao(self):
        self.connection.close()

        




    