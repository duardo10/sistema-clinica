# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recepcionista.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class TelaRecepcionista(object):
    """
    Classe responsavel por definir a interface grafica da tela do recepcionista.

    Attributes
    ---------
    centralwidget : QtWidgets.QWidget 
        Widget central da janela principal.
    label : QtWidgets.QLabel 
        Rotulo para exibir o titulo da janela.
    layoutWidget : QtWidgets.QWidget 
        Widget para agrupar os elementos visuais.
    verticalLayout : QtWidgets.QVBoxLayout
        Layout vertical para organizar os botoes.
    pushButton_2 : QtWidgets.QPushButton 
        Botao para acessar o atendimento.
    pushButton_3 : QtWidgets.QPushButton
        Botao para acessar a consulta.
    pushButton_5 : QtWidgets.QPushButton
        Botao para voltar.
    line : QtWidgets.QFrame 
        Linha horizontal para separar os elementos visuais.

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
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(140, 211, 238);  /* Cor de fundo */")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 40, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 130, 531, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"            background-color: rgb(65, 150, 183);  /* Cor de fundo */\n"
"            color: white;  /* Cor do texto */\n"
"            border-radius: 10px;  /* Raio dos cantos */\n"
"            padding: 10px 20px;  /* Preenchimento interno */\n"
"        }\n"
"        \n"
"        QPushButton:hover {\n"
"            color: rgb(8, 113, 155);\n"
"            background-color: white;  /* Cor de fundo ao passar o mouse */\n"
"        }")
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"            background-color: rgb(65, 150, 183);  /* Cor de fundo */\n"
"            color: white;  /* Cor do texto */\n"
"            border-radius: 10px;  /* Raio dos cantos */\n"
"            padding: 10px 20px;  /* Preenchimento interno */\n"
"        }\n"
"        \n"
"        QPushButton:hover {\n"
"            color: rgb(8, 113, 155);\n"
"            background-color: white;  /* Cor de fundo ao passar o mouse */\n"
"        }")
        self.pushButton_3.setAutoDefault(True)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 440, 121, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
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
        self.pushButton_5.setObjectName("pushButton_5")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 99, 801, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.label.setText(_translate("MainWindow", "RECEPCIONISTA"))
        self.pushButton_2.setText(_translate("MainWindow", "Atendimento"))
        self.pushButton_3.setText(_translate("MainWindow", "Consulta"))
        self.pushButton_5.setText(_translate("MainWindow", "VOLTAR"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaRecepcionista()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
