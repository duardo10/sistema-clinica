# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imprimir_dados.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ImpDados(object):
    """
    Classe responsavel por configurar a interface grafica da janela de Impressão de Dados.

    Attributes
    ----------
    centralwidget : QtWidgets.QWidget
        Widget central da janela.
    label : QtWidgets.QLabel
        Geometria do rotulo de titulo da janela.
    layoutWidget : QtWidgets.QWidget
        Widget para o layout vertical.
    verticalLayout : QtWidgets.QVBoxLayout
        Layout vertical para os botoes.
    pushButton : QtWidgets.QPushButton
        Botao para imprimir recepcionistas.
    pushButton_2 : QtWidgets.QPushButton
        Botao para imprimir medicos.
    pushButton_4 : QtWidgets.QPushButton
        Botao para voltar.
    line : QtWidgets.QFrame
        Linha horizontal separadora.

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
        self.label.setGeometry(QtCore.QRect(210, 40, 311, 51))
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
        self.layoutWidget.setGeometry(QtCore.QRect(100, 130, 531, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
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
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
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
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 390, 121, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
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
        self.pushButton_4.setObjectName("pushButton_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 100, 781, 16))
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
        self.label.setText(_translate("MainWindow", "IMPRIMIR DADOS"))
        self.pushButton.setText(_translate("MainWindow", "Imprimir Recepcionistas"))
        self.pushButton_2.setText(_translate("MainWindow", "Imprimir Médicos"))
        self.pushButton_4.setText(_translate("MainWindow", "VOLTAR"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ImpDados()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
