# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'excluir_guiche.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ExcluirGuiche(object):
    def setupUi(self, MainWindow):
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
        self.label.setGeometry(QtCore.QRect(210, 20, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 380, 121, 31))
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
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 420, 121, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 170, 801, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 199, 31))
        self.label_2.setStyleSheet("background-color: white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 100, 509, 31))
        self.lineEdit.setStyleSheet("background-color: white;")
        self.lineEdit.setObjectName("lineEdit")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 70, 801, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 140, 121, 31))
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
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 220, 199, 34))
        self.label_5.setStyleSheet("background-color: white;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 270, 199, 34))
        self.label_12.setStyleSheet("background-color: white;")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 320, 199, 34))
        self.label_6.setStyleSheet("background-color: white;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 220, 509, 31))
        self.lineEdit_2.setStyleSheet("background-color: white;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 270, 509, 31))
        self.lineEdit_3.setStyleSheet("background-color: white;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 320, 509, 31))
        self.lineEdit_4.setStyleSheet("background-color: white;")
        self.lineEdit_4.setObjectName("lineEdit_4")
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
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "EXCLUIR GUICHE"))
        self.pushButton_2.setText(_translate("MainWindow", "EXCLUIR"))
        self.pushButton_3.setText(_translate("MainWindow", "VOLTAR"))
        self.label_2.setText(_translate("MainWindow", "ID DO GUICHE:"))
        self.pushButton.setText(_translate("MainWindow", "BUSCAR"))
        self.label_5.setText(_translate("MainWindow", "STATUS:"))
        self.label_12.setText(_translate("MainWindow", "SENHA:"))
        self.label_6.setText(_translate("MainWindow", "MODO:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ExcluirGuiche()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
