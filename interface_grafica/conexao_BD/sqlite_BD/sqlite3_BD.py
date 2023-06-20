import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget

#from tela_busc import Tela_busca
from tela_cad import Tela_cadastro
from tela_principal import Tela_principal
from tela_busc import Tela_busca
from cadastro import Cadastro
from pessoa import Pessoa

import sqlite3

conexao = sqlite3.connect('teste.sqlite')
cursor = conexao.cursor()

sql = """CREATE TABLE IF NOT EXISTS usuarios(nome text NOT NULL, cpf text NOT NULL PRIMARY KEY,
         endereco text NOT NULL, nascimento text NOT NULL)"""

nome = 'eduardo'
email = 'duardos36@gmail.com'
cursor.execute(sql)

class Ui_main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640,480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow() 
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_principal()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastro = Tela_cadastro()
        self.tela_cadastro.setupUi(self.stack1)



        self.tela_buscar = Tela_busca()
        self.tela_buscar.setupUi(self.stack2)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)

class Main(QMainWindow, Ui_main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        
        self.cad = Cadastro()
        self.tela_inicial.pushButton.clicked.connect(self.abrirTelaCadastro)
        self.tela_inicial.pushButton_2.clicked.connect(self.abrirTelaBuscar)
        self.tela_inicial.pushButton_3.clicked.connect(self.sair)

        self.tela_cadastro.pushButton.clicked.connect(self.cadastrar)
        self.tela_cadastro.pushButton_2.clicked.connect(self.voltar)
        #self.tela_cadastro.pushButton_3.clicked.connect(self.sair)

        self.tela_buscar.pushButton_2.clicked.connect(self.busca)
        self.tela_buscar.pushButton_3.clicked.connect(self.excluir)
        self.tela_buscar.pushButton.clicked.connect(self.voltar)
    
    def cadastrar(self):
        nome = self.tela_cadastro.lineEdit.text()
        cpf = self.tela_cadastro.lineEdit_2.text()
        endereco = self.tela_cadastro.lineEdit_3.text()
        nascimento = self.tela_cadastro.lineEdit_4.text()
     
        # verifico se todos os dados foram preenchidos
        if not(nome=='' or cpf=='' or endereco=='' or nascimento==''):
            pessoa = Pessoa(nome,cpf,endereco,nascimento)
            cursor.execute('SELECT cpf FROM usuarios')
            dados = cursor.fetchall()
            conexao.commit()
            
            print(dados)
            retorno = self.cad.buscar(pessoa.cpf)
            result = self.cad.cadastro(pessoa.cpf)
            print(retorno)
            print(result)
            if self.cad.cadastro(pessoa.cpf):
                cursor.execute("INSERT INTO usuarios(nome,cpf,endereco,nascimento) VALUES(?,?,?,?)", (nome,cpf,endereco,nascimento))
                conexao.commit()
                #imprime uma menssagem de sucesso
                QtWidgets.QMessageBox.information(None, 'interface_grafica', 'Cadastro realizado com sucesso!')
                #limpar os dados             
                self.tela_cadastro.lineEdit.setText('')
                self.tela_cadastro.lineEdit_2.setText('')
                self.tela_cadastro.lineEdit_3.setText('')
                self.tela_cadastro.lineEdit_4.setText('')
                
            else:
                QtWidgets.QMessageBox.information(None, 'interface_grafica', 'CPF ja cadastrado!') 
            """
            if retorno == None:
                cursor.execute("INSERT INTO usuarios(nome,cpf,endereco,nascimento) VALUES(?,?,?,?)", (nome,cpf,endereco,nascimento))
                #imprime uma menssagem de sucesso
                QtWidgets.QMessageBox.information(None, 'interface_grafica', 'Cadastro realizado com sucesso!')
                 #limpar os dados             
                self.tela_cadastro.lineEdit.setText('')
                self.tela_cadastro.lineEdit_2.setText('')
                self.tela_cadastro.lineEdit_3.setText('')
                self.tela_cadastro.lineEdit_4.setText('')
                conexao.commit()

            else:
                QtWidgets.QMessageBox.information(None, 'interface_grafica', 'CPF ja cadastrado!') 
            """
        else:
             # imprime uma menssagem de erro
            QtWidgets.QMessageBox.information(None, 'interface_grafica', 'Cadastro não realizado! informe todos os campos.')

        #conexao.close()
    def busca(self):
        cpf = self.tela_buscar.lineEdit_5.text()
    
        pessoa = self.cad.buscar(cpf) 
          
        if (pessoa != None):
            print(pessoa)
            cursor.execute('SELECT nome FROM usuarios WHERE cpf = ?', (pessoa,))
            nome = cursor.fetchone()[0]
            cursor.execute('SELECT endereco FROM usuarios WHERE cpf = ?', (pessoa,))
            endereco = cursor.fetchone()[0]
            cursor.execute('SELECT nascimento FROM usuarios WHERE cpf = ?', (pessoa,))
            nascimento = cursor.fetchone()[0]
            conexao.commit()
            print(nome)
            print(endereco)
            print(nascimento)
            self.tela_buscar.lineEdit_6.setText(nome)
            self.tela_buscar.lineEdit_7.setText(endereco)
            self.tela_buscar.lineEdit_8.setText(nascimento)
        else:
            QtWidgets.QMessageBox.warning(None, "interface_grafica", 'Nenhuma pessoa foi registrada com este CPF.')
        #else:
            #QtWidgets.QMessageBox.warning(None, "interface_grafica", "Por favor, digite o CPF para realizar a busca.")
            """
            pessoa = Pessoa(nome,cpf,endereco,nascimento)
            cursor.execute('SELECT cpf FROM usuarios')
            dados = cursor.fetchall()  
            print(dados)
            for dado in dados: 
                if dado[0] != pessoa.cpf : 
                    # cpf ja existe na lista
                    cursor.execute("INSERT INTO usuarios(nome,cpf,endereco,nascimento) VALUES(?,?,?,?)", (nome,cpf,endereco,nascimento))
                    cursor.execute('SELECT * FROM usuarios')
                    
                    #imprime uma menssagem de sucesso
                    QtWidgets.QMessageBox.information(None, 'interface_grafica', 'Cadastro realizado com sucesso!')
                
                    #limpar os dados             
                    self.tela_cadastro.lineEdit.setText('')
                    self.tela_cadastro.lineEdit_2.setText('')
                    self.tela_cadastro.lineEdit_3.setText('')
                    self.tela_cadastro.lineEdit_4.setText('')

                    for c in cursor:
                        if c != None:
                            print(c) 
                else:
                    # cpf ja existe na lista
                    QtWidgets.QMessageBox.information(None, 'interface_grafica', 'CPF ja cadastrado!') 
        else:
            # imprime uma menssagem de erro
            QtWidgets.QMessageBox.information(None, 'interface_grafica', 'Cadastro não realizado! informe todos os campos.')
            
        """
    
    def excluir(self):
        cpf = self.tela_buscar.lineEdit_5.text()
        #if cpf:   
        pessoa = self.cad.buscar(cpf) 
        print('excluir')
        print(pessoa)
        if (pessoa != None):
            print('entrou')
            cursor.execute('DELETE FROM usuarios WHERE cpf = ?',(pessoa))
            conexao.commit()
            print('saiu')
            QtWidgets.QMessageBox.warning(None, "interface_grafica", 'Pessoa removida.')
            self.tela_buscar.lineEdit_6.setText('')
            self.tela_buscar.lineEdit_7.setText('')
            self.tela_buscar.lineEdit_8.setText('')
        else:
            QtWidgets.QMessageBox.warning(None, "interface_grafica", 'Nenhuma pessoa foi registrada com este CPF.')
            self.tela_buscar.lineEdit_6.setText('')
            self.tela_buscar.lineEdit_7.setText('')
            self.tela_buscar.lineEdit_8.setText('')
        #else:
            #QtWidgets.QMessageBox.warning(None, "interface_grafica", "Por favor, digite o CPF para realizar a busca.")
        

    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)
    
    def abrirTelaBuscar(self):
        self.QtStack.setCurrentIndex(2)
    
    def sair(self):
        return exit()

    def voltar(self):
        self.QtStack.setCurrentIndex(0)
    

    
    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())

conexao.close()


