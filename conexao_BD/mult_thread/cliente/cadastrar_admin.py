# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastrar_admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

class CadastrarAdmin(object):
    """
    Classe responsavel por configurar a interface grafica da janela de Cadastro de Administrador.

    Attributes
    ----------
    centralwidget : QtWidgets.QWidget
        Widget central da janela.
    label : QtWidgets.QLabel
        Geometria do rotulo de titulo da janela.
    pushButton : QtWidgets.QPushButton
        Botao para cadastrar administrador.
    pushButton_2 : QtWidgets.QPushButton
        Botao para voltar.
    line : QtWidgets.QFrame
        Linha horizontal separadora.
    label_7 : QtWidgets.QLabel
        Rotulo "CPF".
    label_8 : QtWidgets.QLabel
        Rotulo "Nome".
    label_9 : QtWidgets.QLabel
        Rotulo "Senha".
    lineEdit : QtWidgets.QLineEdit
        Caixa de texto para o CPF.
    lineEdit_2 : QtWidgets.QLineEdit
        Caixa de texto para o nome.
    lineEdit_3 : QtWidgets.QLineEdit
        Caixa de texto para a senha.

    Methods
    ------
    setupUi(MainWindow) : QtWidgets.QMainWindow
        Referencia para a janela principal
    retranslateUi(MainWindow) : QtWidgets.QMainWindow
        Traduz os textos da interface para o idioma selecionado.
    """
    
    def setupUi(self, MainWindow):
        """
        Configura a interface grafica da janela principal.

        Parameters
        ----------
        MainWindow : QtWidgets.QMainWindow
             Referencia para a janela principal
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 600)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(140, 211, 238);  /* Cor de fundo */")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 50, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 310, 121, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"            background-color: white;  /* Cor de fundo */\n"
"            color: rgb(65, 150, 183);  /* Cor do texto */\n"
"            border-radius: 10px;  /* Raio dos cantos */\n"
"            padding: 10px 20px;  /* Preenchimento interno */\n"
"        }\n"
"        \n"
"        QPushButton:hover {\n"
"            color: white;\n"
"            background-color: rgb(8, 113, 155);  /* Cor de fundo ao passar o mouse */\n"
"        }")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 370, 121, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"            background-color: white;  /* Cor de fundo */\n"
"            color: rgb(65, 150, 183);  /* Cor do texto */\n"
"            border-radius: 10px;  /* Raio dos cantos */\n"
"            padding: 10px 20px;  /* Preenchimento interno */\n"
"        }\n"
"        \n"
"        QPushButton:hover {\n"
"            color: white;\n"
"            background-color: rgb(8, 113, 155);  /* Cor de fundo ao passar o mouse */\n"
"        }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 110, 801, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 140, 109, 32))
        self.label_7.setStyleSheet(" background-color: white;  /* Cor de fundo */")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 190, 109, 32))
        self.label_8.setStyleSheet(" background-color: white;  /* Cor de fundo */")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 240, 109, 32))
        self.label_9.setStyleSheet(" background-color: white;  /* Cor de fundo */")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 141, 479, 31))
        self.lineEdit.setStyleSheet(" background-color: white;  /* Cor de fundo */")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 191, 479, 31))
        self.lineEdit_2.setStyleSheet(" background-color: white;  /* Cor de fundo */")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 240, 479, 31))
        self.lineEdit_3.setStyleSheet(" background-color: white;  /* Cor de fundo */")
        self.lineEdit_3.setObjectName("lineEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
        Traduz os textos da interface para o idioma selecionado.

        Parameters
        ----------
        MainWindow : QtWidgets.QMainWindow
            Referencia para a janela principal
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CADASTRAR ADMIN"))
        self.pushButton.setText(_translate("MainWindow", "CADASTRAR"))
        self.pushButton_2.setText(_translate("MainWindow", "VOLTAR"))
        self.label_7.setText(_translate("MainWindow", "CPF:"))
        self.label_8.setText(_translate("MainWindow", "NOME:"))
        self.label_9.setText(_translate("MainWindow", "SENHA:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CadastrarAdmin()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
