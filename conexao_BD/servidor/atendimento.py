import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget

import mysql.connector
class Guiche():
    """
    A classe Guichê é responsavel por receber os paciente através de um sistema de senhas para que então seja realizada
    a fixa de consulta. recebe como atributos o numero do Guichê o stsatus dele(livre/ocupado) o paciente e a senha do paciente para
    que então seja chamada a próxima senha. 
    """
    def __init__(self):
         # configurações da conexão com o banco de dados 
        self.connection = mysql.connector.connect(
            user = 'root',
            password = '',
            host = 'localhost',
            database = 'clinica',
        )
        
    
    """
    A função de iniciar atendimento, quando abre a clinica o staus dos Guichês são livres, porém quando é chamada uma nova senha,
    O status do Guichê ficará ocupado e o atributo senha é incrementado para quando o atendimento for finalizado o recepcionista
    chamar a proxima senha. A função irá retornar True se o status do Guichê for livre, e False se for ocupado. os parâmetros 
    utilizados foram um cliente e o numero do Guichê
    #Parâmetros:#
        cliente = object
        ident = int
    #Retorno:#
        boll = (True ou False)
  
    """
    def atualizar_senha(self):
        try:
            cursor = self.connection.cursor()
            selecionar =  "SELECT * FROM guiche"
            cursor.execute(selecionar)
            selecionar = cursor.fetchall()
            for dado in selecionar:
                if dado[3] == 'ativo':
                    senha = dado[2]
                    senha += 1
                    atualiza =  "UPDATE guiche SET senha = %s"
                    cursor.execute(atualiza,(senha,))
                    #confirmar da atualização da senha
                    self.connection.commit()
        
        except mysql.connector.Error as error:
            QtWidgets.QMessageBox.information(None, 'interface', f'Eroo ao atualizar uma senha no banco de dados: {error}')
            #QtWidgets.QMessageBox.critical(None, 'interface', f'Eroo ao atualizar uma senha no banco de dados: {error}', QMessageBox.OK)
            #print(f'Eroo ao atualizar uma senha no banco de dados: {error}')
        finally:
            cursor.close()
    

        
    def iniciar_atendimento(self, recep):
        try:
            print(recep)
            self.connection.commit()
            cursor = self.connection.cursor()
    
            
            consulta = "SELECT * FROM guiche WHERE recepcionista_cpf = %s"
            cursor.execute(consulta,(recep,))
            resultado = cursor.fetchone()
            print(resultado)
            if resultado:
                if resultado[1] == 'livre':
                    id_guiche_livre = resultado[0]
                    self.atualizar_senha()
                    chamada = "SELECT senha FROM guiche WHERE id_guiche = %s"
                    cursor.execute(chamada,(id_guiche_livre,))
                    resultado = cursor.fetchone()
                    QtWidgets.QMessageBox.information(None, 'interface', 'Senha: {}, se dirija ao Guiche {}'.format(resultado[0], id_guiche_livre))
                    #print('Senha: {}, se dirija ao Guiche {}'.format(resultado[0], id_guiche_livre))
                    # Atualiza o status do guichê para "ocupado"
                    atualizacao = "UPDATE guiche SET status = 'ocupado' WHERE id_guiche = %s"
                    cursor.execute(atualizacao, (id_guiche_livre,))
                    self.connection.commit()
                    menssagem = 'Guichê', id_guiche_livre, 'agora está ocupado'
                    QtWidgets.QMessageBox.information(None, 'interface', str(menssagem), QMessageBox.Ok)
                else:
                    QtWidgets.QMessageBox.critical(None, 'interface','guiche está ocupado.', QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.critical(None, 'interface','Esse recepcionista não foi cadastrado em nenhum guiche.', QMessageBox.Ok)
            """
            cursor = self.connection.cursor()
            # Encontre o primeiro guichê livre
            consulta = "SELECT id_guiche FROM guiche WHERE status = 'livre' LIMIT 1"
            cursor.execute(consulta)
            resultado = cursor.fetchone()
            print(resultado)
            # Verifica se encontrou um guichê livre
            if resultado:
                id_guiche_livre = resultado[0]
                
                self.atualizar_senha()
                chamada = "SELECT senha FROM guiche WHERE id_guiche = %s"
                cursor.execute(chamada,(id_guiche_livre,))
                resultado = cursor.fetchone()
                QtWidgets.QMessageBox.information(None, 'interface', 'Senha: {}, se dirija ao Guiche {}'.format(resultado[0], id_guiche_livre))
                #print('Senha: {}, se dirija ao Guiche {}'.format(resultado[0], id_guiche_livre))
                # Atualiza o status do guichê para "ocupado"
                atualizacao = "UPDATE guiche SET status = 'ocupado' WHERE id_guiche = %s"
                cursor.execute(atualizacao, (id_guiche_livre,))
                self.connection.commit()
                menssagem = 'Guichê', id_guiche_livre, 'agora está ocupado'
                QtWidgets.QMessageBox.information(None, 'interface', str(menssagem), QMessageBox.Ok)
                #print('Guichê', id_guiche_livre, 'agora está ocupado.')
            else:
                QtWidgets.QMessageBox.critical(None, 'interface','Não há guichês disponíveis no momento.', QMessageBox.Ok)
                #print('Não há guichês disponíveis no momento.')
        """
        except mysql.connector.Error as error:
            QtWidgets.QMessageBox.information(None, 'interface', f'Eroo ao iniciar atendimento em um guiche no banco de dados: {error}')
            #print(f'Eroo ao iniciar atendimento em um guiche no banco de dados: {error}')
        finally:
            cursor.close()
        



    """
    A função de finalizar o atendimento, quando o staus do Guichê é ocupado, é porque há um paciente sendo atendido, ao realizar 
    o atendimento desse paciente o Guiche fica livre, e pode ser realizado um novo atendimento quando o atendimento for finalizado 
    o recepcionista chama a proxima senha. A função irá retornar True se o status do Guichê for ocupado, e False se for livre. 
    #Parâmetros:#
        - sem parâmetros
    #Retorno:#
        boll = (True ou False)
    """

    def finalizar_atendimento(self, recep):
        try:
            self.connection.commit()
            cursor = self.connection.cursor()
            consulta = "SELECT * FROM guiche WHERE recepcionista_cpf = %s"
            cursor.execute(consulta,(recep,))
            result = cursor.fetchone()
            print(result)
            if result:
                if result[1] == 'livre':
                    QtWidgets.QMessageBox.critical(None, 'interface','O guiche já está livre.', QMessageBox.Ok)
                else:
                    atualiza = "UPDATE guiche SET status = 'livre' WHERE id_guiche = %s"
                    cursor.execute(atualiza,(result[0],))
                    self.connection.commit()
                    menssagem = 'Guiche {} agora está liberado!'.format(result[0])
                    QtWidgets.QMessageBox.information(None, 'interface', menssagem, QMessageBox.Ok)
    
            else:
                QtWidgets.QMessageBox.critical(None, 'interface','Esse recepcionista não foi cadastrado em nenhum guiche.', QMessageBox.Ok)
    
            """
            guiche = int(objguiche)
            print(guiche)
            cursor = self.connection.cursor()
            cursor.execute("SELECT id_guiche FROM guiche")
            result = cursor.fetchall()
            for dado in result:
                if guiche == dado[0]:
                    cursor.execute('SELECT status FROM guiche WHERE id_guiche = %s',(guiche,))
                    resultado = cursor.fetchall()
                    for item in resultado:
                        if item[0] == 'ocupado':
                            atualiza = "UPDATE guiche SET status = 'livre' WHERE id_guiche = %s"
                            cursor.execute(atualiza,(guiche,))
                            self.connection.commit()
                            menssagem = 'Guiche {} agora está liberado!'.format(guiche)
                            QtWidgets.QMessageBox.information(None, 'interface', menssagem, QMessageBox.Ok)
                            return guiche
                        else:
                            menssagem = ('O Guichê já está liberado!')
                            QtWidgets.QMessageBox.information(None, 'interface', menssagem, QMessageBox.Ok)
                            return guiche
                    
            # se não encontrar o guiche retorna None
            return None
             
            """
            
        except mysql.connector.Error as error:
            QtWidgets.QMessageBox.information(None, 'interface', f'Eroo ao finalizar um atendimento em um guiche no banco de dados: {error}')
            #print(f'Eroo ao finalizar um atendimento em um guiche no banco de dados: {error}')
        finally:
            cursor.close()


        
    def ativarGuiche(self, ident_guiche):
        try:
            cursor = self.connection.cursor()
            busc = "SELECT id_guiche,modo FROM guiche"
            cursor.execute(busc)
            busc = cursor.fetchall()
            self.connection.commit()
           
            for dado in busc:
                if dado[0] == int(ident_guiche):
                    if dado[1] == 'ativo':
                        return False
                    else:
                        return True
            
        except mysql.connector.Error as error:
            QtWidgets.QMessageBox.information(None, 'interface', f'Eroo ao ativar um guiche no banco de dados: {error}')
        finally:
            cursor.close()

        
    
    def desativarGuiche(self, idt_guiche):
        try:
            cursor = self.connection.cursor()
            busc = "SELECT id_guiche,modo FROM guiche"
            cursor.execute(busc)
            busc = cursor.fetchall()
            self.connection.commit()
            for dado in busc:
                if dado[0] == int(idt_guiche):
                    if dado[1] == 'ativo':
                        return True
                    else:
                        return False
            
        except mysql.connector.Error as error:
            print(f'Eroo ao desativar um guiche no banco de dados: {error}')
        finally:
            cursor.close()

    def excluir_guiche(self, id_guiche):
        retorno = self.buscGuiche(id_guiche)
        print(retorno)
        if retorno:
            try:
                cursor = self.connection.cursor()
                sql = "DELETE FROM guiche WHERE id_guiche = %s"
                cursor.execute(sql,(id_guiche,))
                self.connection.commit()
                QtWidgets.QMessageBox.information(None, 'interface', 'Guiche excluido')
            except mysql.connector.Error as error:
                QtWidgets.QMessageBox.information(None, 'interface', f'Eroo ao excluir um Guiche: {error}')
            finally:
                cursor.close()
        else:
            QtWidgets.QMessageBox.information(None, 'interface','Guiche não encontrado!')
    
    def buscGuiche(self, id_guiche):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id_guiche FROM guiche WHERE id_guiche = %s",(id_guiche,))
        resultado = cursor.fetchall()
        print(resultado)

        for dado in resultado:
            if int(id_guiche) == dado[0]:
                return True
        return None