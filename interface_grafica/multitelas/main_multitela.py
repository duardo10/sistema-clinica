import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget

#from tela_busc import Tela_busca
from tela_cad import Tela_cadastro
from tela_principal import Tela_principal
from tela_buscar import Tela_busca
from cadastro import Cadastro
from pessoa import Pessoa

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
        self.tela_buscar.pushButton.clicked.connect(self.voltar)

        

    def cadastrar(self):
        nome = self.tela_cadastro.lineEdit.text()
        cpf = self.tela_cadastro.lineEdit_2.text()
        endereco = self.tela_cadastro.lineEdit_3.text()
        nascimento = self.tela_cadastro.lineEdit_4.text()

        # verifico se todos os dados foram preenchidos
        if not(nome=='' or cpf=='' or endereco=='' or nascimento==''):
            pessoa = Pessoa(nome, cpf, endereco, nascimento)
            if self.cad.cadastro(pessoa):
                # cpf ja existe na lista
                #imprime uma menssagem de sucesso
                QtWidgets.QMessageBox.information(None, 'interface_grafica', 'Cadastro realizado com sucesso!')
            
                #limpar os dados             
                self.tela_cadastro.lineEdit.setText('')
                self.tela_cadastro.lineEdit_2.setText('')
                self.tela_cadastro.lineEdit_3.setText('')
                self.tela_cadastro.lineEdit_4.setText('')
            else:
                QtWidgets.QMessageBox.information(None, 'interface_grafica', 'CPF ja cadastrado!')
           
                
        else:
            # imprime uma menssagem de erro
            QtWidgets.QMessageBox.information(None, 'interface_grafica', 'Cadastro não realizado! informe todos os campos.')
        

    def busca(self):
        cpf = self.tela_buscar.lineEdit_5.text()
        #if cpf:
        pessoa = self.cad.buscar(cpf)   
        print(pessoa)   
        if (pessoa != None):
            self.tela_buscar.lineEdit_6.setText(pessoa.nome)
            self.tela_buscar.lineEdit_7.setText(pessoa.endereco)
            self.tela_buscar.lineEdit_8.setText(pessoa.nascimento)
        else:
            QtWidgets.QMessageBox.warning(None, "interface_grafica", 'Nenhuma pessoa foi registrada com este CPF.')
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
