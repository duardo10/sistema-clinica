# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro_novo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from cadastro import Cadastro
from pessoa import Pessoa


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 30, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 280, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 310, 791, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 330, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 360, 491, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_bus_cpf = QtWidgets.QLabel(self.centralwidget)
        self.label_bus_cpf.setGeometry(QtCore.QRect(60, 360, 55, 16))
        self.label_bus_cpf.setObjectName("label_bus_cpf")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 390, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 420, 781, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(37, 110, 71, 141))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_nome = QtWidgets.QLabel(self.widget)
        self.label_nome.setObjectName("label_nome")
        self.verticalLayout.addWidget(self.label_nome)
        self.label_cpf = QtWidgets.QLabel(self.widget)
        self.label_cpf.setObjectName("label_cpf")
        self.verticalLayout.addWidget(self.label_cpf)
        self.label_endereco = QtWidgets.QLabel(self.widget)
        self.label_endereco.setObjectName("label_endereco")
        self.verticalLayout.addWidget(self.label_endereco)
        self.label_nascimento = QtWidgets.QLabel(self.widget)
        self.label_nascimento.setObjectName("label_nascimento")
        self.verticalLayout.addWidget(self.label_nascimento)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(120, 110, 491, 141))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(120, 440, 501, 82))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_3.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_3.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_3.addWidget(self.lineEdit_8)
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(40, 440, 73, 81))
        self.widget3.setObjectName("widget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_busc_nome = QtWidgets.QLabel(self.widget3)
        self.label_busc_nome.setObjectName("label_busc_nome")
        self.verticalLayout_4.addWidget(self.label_busc_nome)
        self.label_busc_endereco = QtWidgets.QLabel(self.widget3)
        self.label_busc_endereco.setObjectName("label_busc_endereco")
        self.verticalLayout_4.addWidget(self.label_busc_endereco)
        self.label_busc_nascimento = QtWidgets.QLabel(self.widget3)
        self.label_busc_nascimento.setObjectName("label_busc_nascimento")
        self.verticalLayout_4.addWidget(self.label_busc_nascimento)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuteste = QtWidgets.QMenu(self.menubar)
        self.menuteste.setObjectName("menuteste")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuteste.menuAction())

        """
        Modificações:
        """
        self.cad = Cadastro()
        self.pushButton.clicked.connect(self.cadastrar)
        self.pushButton_2.clicked.connect(self.busca)
        #self.pushButton.clicked.connect(self.buscar)





        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def cadastrar(self):
        nome = self.lineEdit.text()
        cpf = self.lineEdit_2.text()
        endereco = self.lineEdit_3.text()
        nascimento = self.lineEdit_4.text()

        # verifico se todos os dados foram preenchidos
        if nome and cpf and endereco and nascimento:
            pessoa = Pessoa(nome,cpf,endereco,nascimento)
            
            if self.cad.cadastro(pessoa):
                # cpf ja existe na lista
                #imprime uma menssagem de sucesso
                QtWidgets.QMessageBox.information(None, 'interface_grafica', 'Cadastro realizado com sucesso!')
               
                #limpar os dados             
                self.lineEdit.setText('')
                self.lineEdit_2.setText('')
                self.lineEdit_3.setText('')
                self.lineEdit_4.setText('')
            else:
                QtWidgets.QMessageBox.information(None, 'interface_grafica', 'CPF ja cadastrado!')
               
                
        else:
            # imprime uma menssagem de erro
            QtWidgets.QMessageBox.information(None, 'interface_grafica', 'Cadastro não realizado! informe todos os campos.')

    def busca(self):
        cpf = self.lineEdit_5.text()
        if cpf:
            pessoa = self.cad.buscar(cpf)      
            if pessoa != None:
                self.lineEdit_6.setText(pessoa._nome)
                self.lineEdit_7.setText(pessoa._endereco)
                self.lineEdit_8.setText(pessoa._dt_nascimento)
                return
            else:
                QtWidgets.QMessageBox.warning(None, "interface_grafica", 'Nenhuma pessoa foi registrada com este CPF.')
        else:
            QtWidgets.QMessageBox.warning(None, "interface_grafica", "Por favor, digite o CPF para realizar a busca.")
           
            




        """
        Modificações:
        self.pushButton.clicked.connect(self.cadastrar)
        self.pushButton.clicked.connect(self.buscar)

        def cadastrar(self):
            nome = self.lineEdit.text()
            cpf = self.lineEdit_2.text()
            endereco = self.lineEdit_3.text()
            nascimento = self.lineEdit_4.text()
        """
        
            
           


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CADASTRAR"))
        self.pushButton.setText(_translate("MainWindow", "CADASTRAR"))
        self.label_3.setText(_translate("MainWindow", "BUSCA"))
        self.label_bus_cpf.setText(_translate("MainWindow", "CPF:"))
        self.pushButton_2.setText(_translate("MainWindow", "BUSCAR"))
        self.label_nome.setText(_translate("MainWindow", "Nome"))
        self.label_cpf.setText(_translate("MainWindow", "CPF"))
        self.label_endereco.setText(_translate("MainWindow", "Endereco"))
        self.label_nascimento.setText(_translate("MainWindow", "Nascimento"))
        self.label_busc_nome.setText(_translate("MainWindow", "Nome:"))
        self.label_busc_endereco.setText(_translate("MainWindow", "Endereco:"))
        self.label_busc_nascimento.setText(_translate("MainWindow", "Nascimento:"))
        self.menuteste.setTitle(_translate("MainWindow", "teste"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
