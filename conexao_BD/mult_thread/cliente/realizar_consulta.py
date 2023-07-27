# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'realizar_consulta.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class RealizarConsulta(object):
    """
    Classe responsavel por configurar a interface grafica da janela de Realizar Consulta.

    Attributes
    ----------
    centralwidget : QtWidgets.QWidget
        Widget central da janela.
    label : QtWidgets.QLabel
        Rotulo de titulo da janela.
    pushButton : QtWidgets.QPushButton
        Botao para cadastrar.
    pushButton_2 : QtWidgets.QPushButton
        Botao para voltar.
    line : QtWidgets.QFrame
        Linha horizontal separadora.
    layoutWidget : QtWidgets.QWidget
        Widget para layout de rotulos.
    verticalLayout : QtWidgets.QVBoxLayout
        Layout vertical para organizar os rotulos.
    label_2 : QtWidgets.QLabel
        Rotulo para o CPF do paciente.
    label_3 : QtWidgets.QLabel
        Rotulo para o nome do paciente.
    label_11 : QtWidgets.QLabel
        Rotulo para o telefone.
    label_4 : QtWidgets.QLabel
        Rotulo para a data de nascimento.
    label_5 : QtWidgets.QLabel
        Rotulo para o medico.
    label_6 : QtWidgets.QLabel
        Rotulo para o CRM.
    label_7 : QtWidgets.QLabel
        Rotulo para o tipo de consulta.
    label_10 : QtWidgets.QLabel
        Rotulo para o CPF do medico.
    label_8 : QtWidgets.QLabel
        Rotulo para o CPF do recepcionista.
    layoutWidget1 : QtWidgets.QWidget
        Widget para layout de campos de entrada.
    verticalLayout_2 : QtWidgets.QVBoxLayout
        Layout vertical para organizar os campos de entrada.
    lineEdit : QtWidgets.QLineEdit
        Campo de entrada para o CPF do paciente.
    lineEdit_2 : QtWidgets.QLineEdit
        Campo de entrada para o nome do paciente.
    lineEdit_3 : QtWidgets.QLineEdit
        Campo de entrada para o telefone.
    lineEdit_4 : QtWidgets.QLineEdit
        Campo de entrada para a data de nascimento.
    comboBox : QtWidgets.QComboBox
        Campo de selecao para o medico.
    lineEdit_6 : QtWidgets.QLineEdit
        Campo de entrada para o CRM.
    lineEdit_7 : QtWidgets.QLineEdit
        Campo de entrada para o tipo de consulta.
    lineEdit_9 : QtWidgets.QLineEdit
        Campo de entrada para o CPF do medico.
    lineEdit_10 : QtWidgets.QLineEdit
        Campo de entrada para o CPF do recepcionista.

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
        MainWindow.setStyleSheet("")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: skyblue;")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 50, 421, 51))
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
        self.pushButton.setGeometry(QtCore.QRect(390, 480, 121, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: white;  /* Cor de fundo */\n"
"    color: rgb(65, 150, 183);  /* Cor do texto */\n"
"    border-radius: 10px;  /* Raio dos cantos */\n"
"    padding: 10px 20px;  /* Preenchimento interno */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: white;\n"
"    background-color: rgb(8, 113, 155);  /* Cor de fundo ao passar o mouse */\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 480, 121, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: white;  /* Cor de fundo */\n"
"    color: rgb(65, 150, 183);  /* Cor do texto */\n"
"    border-radius: 10px;  /* Raio dos cantos */\n"
"    padding: 10px 20px;  /* Preenchimento interno */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: white;\n"
"    background-color: rgb(8, 113, 155);  /* Cor de fundo ao passar o mouse */\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 110, 801, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 140, 201, 331))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("background-color: white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("background-color: white;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setStyleSheet("background-color: white;")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("background-color: white;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setStyleSheet("background-color: white;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setStyleSheet("background-color: white;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setStyleSheet("background-color: white;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setStyleSheet("background-color: white;")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setStyleSheet("background-color: white;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(240, 134, 511, 341))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit.setStyleSheet("background-color: white;")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setStyleSheet("background-color: white;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_3.setStyleSheet("background-color: white;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_4.setStyleSheet("background-color: white;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox.setStyleSheet("background-color: white;")
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_6.setStyleSheet("background-color: white;")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_2.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_7.setStyleSheet("background-color: white;")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_2.addWidget(self.lineEdit_7)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_9.setStyleSheet("background-color: white;")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_10.setStyleSheet("background-color: white;")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_2.addWidget(self.lineEdit_10)
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
        self.label.setText(_translate("MainWindow", "REALIZAR CONSULTA"))
        self.pushButton.setText(_translate("MainWindow", "CADASTRAR"))
        self.pushButton_2.setText(_translate("MainWindow", "VOLTAR"))
        self.label_2.setText(_translate("MainWindow", "CPF DO PACIENTE:"))
        self.label_3.setText(_translate("MainWindow", "NOME DO PACIENTE:"))
        self.label_11.setText(_translate("MainWindow", "TELEFONE:"))
        self.label_4.setText(_translate("MainWindow", "NASCIMENTO:"))
        self.label_5.setText(_translate("MainWindow", "MEDICO:"))
        self.label_6.setText(_translate("MainWindow", "CRM:"))
        self.label_7.setText(_translate("MainWindow", "TIPO DA CONSULTA:"))
        self.label_10.setText(_translate("MainWindow", "CPF MEDICO:"))
        self.label_8.setText(_translate("MainWindow", "CPF RECEPCIONISTA:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = RealizarConsulta()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
