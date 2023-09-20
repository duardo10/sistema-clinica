import typing
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget, QTableWidget, QTableWidgetItem

#importação das telas
from tela_login import TelaLogin
from tela_medico import TelaMedico
from tela_recepcionista import TelaRecepcionista
from tela_login_medico import LoginMedico
from tela_login_recepcionista import LoginRecepcionista
from cadastrar_recepcionista import CadastrarRecep
from cadastrar_recp import CadastroRecp
from cadastrar_medico import CadastrarMedico
from cadastrar_med import CadastroMed
from tela_cadastro import TelaCadastros
from tela_atendimento import TelaAtendimento
from adicionar_guiche import AddGuiche
#from ativar_guiche import AtivarGuiche
from imprimir_dados import ImpDados
from imprimir_medico import ImpMed
from imprimir_recepcionista import ImpRecp
# tatata
#from impressao import Imprimir
from tela_consulta import TelaConsulta
from realizar_consulta import RealizarConsulta
from excluir_consulta import ExcluirConsulta
from verifica_tipo import VerificaTipo
from atualizar_consulta import AtualizarConsulta
from lista_pacientes import ListaPacientes
from login_admin import LoginAdmin
from cadastrar_admin import CadastrarAdmin

import socket
ip = '10.0.0.105'
port = 8020
addr = ((ip, port))
cliente_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente_socket.connect(addr)

class Ui_main(QtWidgets.QWidget):
    """
    Responsavel por configurar a interface grafica principal do sistema.

    Gerencia as janelas e layouts para exibir as diferentes telas do programa.

    Attributes
    ---------
    tela_login : TelaLogin
        Objeto da classe de TelaLogin
    tela_login_medico : LoginMedico
        Objeto da classe LoginMedico
    tela_login_recepcionista : LoginRecepcionista
        Objeto da classe LoginRecepcionissta
    tela_medico : TelaMedico
        Objeto da classe TelaMedico
    tela_recepcionista : TelaRecepcionista
        Objeto da classe TelaRecepcionista
    cadastrar_medico : CadastrarMedico
        Objeto da classe CadastrarMedico 
    cadastrar_recepcionista : CadastrarRecep
        Objeto da classe CadastrarRecep
    tela_cadastro : TelaCadastros
        Objeto da classe TelaCadastros
    cadastrar_recp : CadastroRecp
        Objeto da classe CadastroRecp
    cadastrar_med : CadastroMed
        Objeto da classe CadastroMed
    cadastrar_admin : CadastrarAdmin
        Objeto da classe CadastrarAdmin
    tela_atendimento : TelaAtendimento
        Objeto da classe TelaAtendimento
    adicionar_guiche : AddGuiche
        Objeto da classe AddGuiche
    imprimir_dados : ImpDados
        Objeto da classe ImpDados
    imprimir_recepcionista : ImpRecp
        Objeto da classe ImpRecp
    imprimir_medico : ImpMed
        Objeto da classe ImpMed
    tela_consulta : TelaConsulta
        Objeto da classe TelaConsulta
    realizar_consulta : RealizarConsulta
        Objeto da classe RealizarConsulta
    excluir_consulta : ExcluirConsulta
        Objeto da classe ExcluirConsulta
    verifica_tipo : VerificaTipo
        Objeto da classe VerificaTipo
    atualizar_consulta : AtualizarConsulta
        Objeto da classe AtualizarConsulta
    lista_pacientes : ListaPacientes
        Objeto da classe ListaPacientes
    login_admin : LoginAdmin
        Objeto da classe LoginAdmin

    Methods
    ------
    setupUi
        Configura a interface grafica definindo as janelas e layouts necessarios
    """

    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640,480)   
        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow() 
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
        self.stack8 = QtWidgets.QMainWindow()
        self.stack9 = QtWidgets.QMainWindow()
        self.stack10 = QtWidgets.QMainWindow()
        self.stack11 = QtWidgets.QMainWindow()
        self.stack12 = QtWidgets.QMainWindow()
        self.stack13 = QtWidgets.QMainWindow()
        self.stack14 = QtWidgets.QMainWindow()
        self.stack15 = QtWidgets.QMainWindow()
        self.stack16 = QtWidgets.QMainWindow()
        self.stack17 = QtWidgets.QMainWindow()
        self.stack18 = QtWidgets.QMainWindow()
        self.stack19 = QtWidgets.QMainWindow()
        self.stack20 = QtWidgets.QMainWindow()
        self.stack21 = QtWidgets.QMainWindow()
        self.stack22 = QtWidgets.QMainWindow()
        self.stack23 = QtWidgets.QMainWindow()
        self.stack24 = QtWidgets.QMainWindow()
        self.stack25 = QtWidgets.QMainWindow()
        self.stack26 = QtWidgets.QMainWindow()
        self.stack27 = QtWidgets.QMainWindow()
        self.stack28 = QtWidgets.QMainWindow()
        self.stack29 = QtWidgets.QMainWindow()

        self.tela_login = TelaLogin()
        self.tela_login.setupUi(self.stack0)

        self.tela_login_medico = LoginMedico()
        self.tela_login_medico.setupUi(self.stack1)

        self.tela_login_recepcionista = LoginRecepcionista()
        self.tela_login_recepcionista.setupUi(self.stack2)

        self.tela_medico = TelaMedico()
        self.tela_medico.setupUi(self.stack3)

        self.tela_recepcionista = TelaRecepcionista()
        self.tela_recepcionista.setupUi(self.stack4)

        self.cadastrar_medico = CadastrarMedico()
        self.cadastrar_medico.setupUi(self.stack5)

        self.cadastrar_recepcionista = CadastrarRecep()
        self.cadastrar_recepcionista.setupUi(self.stack6)

        self.tela_cadastro = TelaCadastros()
        self.tela_cadastro.setupUi(self.stack7)

        self.cadastrar_recp = CadastroRecp()
        self.cadastrar_recp.setupUi(self.stack8)

        self.cadastrar_med = CadastroMed()
        self.cadastrar_med.setupUi(self.stack9)

        self.cadastrar_admin = CadastrarAdmin()
        self.cadastrar_admin.setupUi(self.stack10)

        self.tela_atendimento = TelaAtendimento()
        self.tela_atendimento.setupUi(self.stack11)

        self.adicionar_guiche = AddGuiche()
        self.adicionar_guiche.setupUi(self.stack12)

        #self.finalizar_atendimento = Finalizar()
        #self.finalizar_atendimento.setupUi(self.stack13)

        #self.ativar_guiche = AtivarGuiche()
        #self.ativar_guiche.setupUi(self.stack14)

        #self.desativa_guiche = DesativarGuiche()
        #self.desativa_guiche.setupUi(self.stack15) 

        self.imprimir_dados = ImpDados()
        self.imprimir_dados.setupUi(self.stack16)

        self.imprimir_recepcionista = ImpRecp()
        self.imprimir_recepcionista.setupUi(self.stack17)

        self.imprimir_medico = ImpMed()
        self.imprimir_medico.setupUi(self.stack18)

        self.tela_consulta = TelaConsulta()
        self.tela_consulta.setupUi(self.stack20)

        self.realizar_consulta = RealizarConsulta()
        self.realizar_consulta.setupUi(self.stack21)

        self.excluir_consulta = ExcluirConsulta()
        self.excluir_consulta.setupUi(self.stack22)

        self.verifica_tipo = VerificaTipo()
        self.verifica_tipo.setupUi(self.stack23)

        #self.imprimir_pacientes = ImprimirPacientes()
        #self.imprimir_pacientes.setupUi(self.stack24)

        #self.excluir_pacientes = ExcluirPacientes()
        #self.excluir_pacientes.setupUi(self.stack25)

        #self.excluir_guiche = ExcluirGuiche()
        #self.excluir_guiche.setupUi(self.stack26)

        self.atualizar_consulta = AtualizarConsulta()
        self.atualizar_consulta.setupUi(self.stack27)

        self.lista_pacientes = ListaPacientes()
        self.lista_pacientes.setupUi(self.stack28)

        self.login_admin = LoginAdmin()
        self.login_admin.setupUi(self.stack29)


        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)
        self.QtStack.addWidget(self.stack9)
        self.QtStack.addWidget(self.stack10)
        self.QtStack.addWidget(self.stack11)
        self.QtStack.addWidget(self.stack12)
        self.QtStack.addWidget(self.stack13)
        self.QtStack.addWidget(self.stack14)
        self.QtStack.addWidget(self.stack15)
        self.QtStack.addWidget(self.stack16)
        self.QtStack.addWidget(self.stack17)
        self.QtStack.addWidget(self.stack18)
        self.QtStack.addWidget(self.stack19)
        self.QtStack.addWidget(self.stack20)
        self.QtStack.addWidget(self.stack21)
        self.QtStack.addWidget(self.stack22)
        self.QtStack.addWidget(self.stack23)
        self.QtStack.addWidget(self.stack24)
        self.QtStack.addWidget(self.stack25)
        self.QtStack.addWidget(self.stack26)
        self.QtStack.addWidget(self.stack27)
        self.QtStack.addWidget(self.stack28)
        self.QtStack.addWidget(self.stack29)
        

class Main(QMainWindow, Ui_main):
    """
    Representa a janela principal do sistema.

    Esta classe e responsavel por gerenciar a interface grafica principal do sistema,
    incluindo a exibicao de widgets e a conexao de sinais e slots

    Attributes
    ---------
    tableWidget (QTableWidget)
        Widget de tabela central da janela

    Methods
    ------
    loginAdmin()
        Esse metodo representa o login do administrador
    loginMedico()
        Esse metodo representa o login do medico
    loginRecep()
        Esse metodo representa o login do recepcionista
    cadastroMedicoLogin()
        Esse metodo realiza o cadastro de um medico    
    cadastroMedico()
        Esse metodo realiza o cadastro de um medico
    cadastroRecepLogin()
        Esse metodo realiza o cadastro de um recepcionista
    cadastroRecep()
        Esse metodo realiza o cadastro de um recepcionista na tela de cadastro
    cadastroAdmin()
        Esse metodo realiza o cadastro de um administrador na tela de cadastro
    iniciarAtendimento()
        Esse metodo inicia o atendimento em um guiche
    finalizarAtendimento()
        Esse metodo finaliza o atendimento em um guiche
    addGuiche()
        Esse metodo adiciona um novo guiche
    excluirGuiche()
        Esse metodo exclui um guiche
    ativarGuiche()
        Esse metodo ativa um guiche
    desativar_Guiche()
        Esse metodo desativa um guiche
    imprimirRecep()
        Esse metodo imprime os dados de um recepcionista
    imprimirMed()
        Esse metodo imprime os dados de um medico
    realizarConsulta()
        Esse metodo realiza uma consulta medica
    enviarConsulta()
        Esse metodo envia a consulta para a lista de pacientes.
    buscCons()
        Esse metodo realiza a busca de uma consulta para exclui-la
    excluirConsulta()
        Esse metodo exclui uma consulta
    verificaTipo()
        Esse metodo verifica o tipo de consulta
    enviarCons()
        Esse metodo envia consulta para a lista de pacientes.
    buscConsult()
        Esse metodo busca informacoes de uma consulta para atualiza-la
    atualizarConsulta()
        Esse metodo atualiza o tipo de uma consulta
    excluiPacientes()
        Esse metodo exclui um paciente da lista de pacientes
    abrirTelaLoginMedico()
        Esse metodo abre a tela de login para medicos.
    abrirTelaLoginRecepcionista()
        Esse metodo abre a tela de login para recepcionistas.
    abrirTelaMedico()
        Esse metodo abre a tela principal do medico.
    abrirTelaRecepcionista()
        Esse metodo abre a tela principal do recepcionista.
    abrirCadastroMedico()
        Esse metodo abre a tela de cadastro de medico.
    abrirCadastroRecepcionista()
        Esse metodo abre a tela de cadastro de recepcionista.
    abrirTelaCadastros()
        Esse metodo abre a tela de cadastros.
    abrirCadastroRecep()
        Esse metodo abre a tela de cadastro de recepcionista.
    abrirCadastroMed()
        Esse metodo abre a tela de cadastro de medico.
    abrirCadastroAdmin()
        Esse metodo abre a tela de cadastro de administrador.
    abrirAtendimento()
        Esse metodo abre a tela de atendimento.
    abrirAddGuiche()
        Esse metodo abre a tela de adicionar guiche.
    abrirfinalizarAtendimento()
        Esse metodo abre a tela de finalizar atendimento.  
    abrirativarGuiche()
        Esse metodo abre a tela de ativar guiche.
    abrirdesativaGuiche()
        Esse metodo abre a tela de desativar guiche.
    abrirImpressao()
        Esse metodo abre a tela de impressao.
    abrirImpRecep()
        Esse metodo abre a tela de impressao para recepcionista.
    abrirImpMed()
        Esse metodo abre a tela de impressao para medico.
    abrirConsulta()
        Esse metodo abre a tela de consulta.
    abrirRealizarConsult()
        Esse metodo abre a tela de realizacao de consulta.
    realizarConsultaAA()
        Esse metodo realiza uma consulta ao selecionar um medico na lista suspensa.
    abrirExcluirConsult()
        Esse metodo abre a tela de exclusao de consulta.
    abrirTipoConsult()
        Esse metodo abre a tela de verificacao do tipo de consulta.
    abrirImpPac()
        Esse metodo abre a tela de impressao de informacoes do paciente.
    abrirExcluirPac()
        Esse metodo abre a tela de exclusao de paciente.
    abrirExcluirGuiche()
        Esse metodo abre a tela de exclusao de guiche.
    abrirAtualizarCons()
        Esse metodo abre a tela de atualizacao de consulta.
    abrirListaPaciente()
        Esse metodo abre a tela de lista de pacientes.
    abrirLoginAdmin()
        Esse metodo abre a tela de login do administrador.
    sair()
        Esse metodo fecha a aplicacao e encerra a conexao com o servidor. 
    voltarLogin()
        Esse metodo volta para a tela de login.
    voltarLoginMedico()
        Esse metodo volta para a tela de login do medico.
    voltarLoginRecep()
        Esse metodo volta para a tela de login do recepcionista.
    voltarCadastros()
        Volta para a tela de cadastros.
    """

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.tableWidget = QTableWidget(self)
        self.setCentralWidget(self.tableWidget)

        # tela principal "Login"
        self.tela_login.pushButton_4.clicked.connect(self.abrirLoginAdmin)
        self.tela_login.pushButton.clicked.connect(self.abrirTelaLoginMedico)
        self.tela_login.pushButton_2.clicked.connect(self.abrirTelaLoginRecepcionista)
        self.tela_login.pushButton_3.clicked.connect(self.sair)

        # botões da tela login admin
        self.login_admin.pushButton.clicked.connect(self.loginAdmin)
        self.login_admin.pushButton_2.clicked.connect(self.abrirCadastroAdmin)
        self.cadastrar_admin.pushButton.clicked.connect(self.cadastroAdmin)
        self.cadastrar_admin.pushButton_2.clicked.connect(self.abrirLoginAdmin)
        self.login_admin.pushButton_3.clicked.connect(self.voltarLogin)

        # botões da tela login médico
        self.tela_login_medico.pushButton.clicked.connect(self.loginMedico)
        self.tela_login_medico.pushButton_2.clicked.connect(self.abrirCadastroMedico)
        self.tela_login_medico.pushButton_3.clicked.connect(self.voltarLogin)

        # botões da tela login recepcionista
        self.tela_login_recepcionista.pushButton.clicked.connect(self.loginRecep)
        self.tela_login_recepcionista.pushButton_2.clicked.connect(self.abrirCadastroRecepcionista)
        self.tela_login_recepcionista.pushButton_3.clicked.connect(self.voltarLogin)

        # tela de cadastro do medico na tela login
        self.cadastrar_medico.pushButton.clicked.connect(self.cadastroMedicoLogin)
        self.cadastrar_medico.pushButton_2.clicked.connect(self.voltarLoginMedico)

        # tela de cadastro do recepcionista na tela login
        self.cadastrar_recepcionista.pushButton.clicked.connect(self.cadastroRecepLogin)
        self.cadastrar_recepcionista.pushButton_2.clicked.connect(self.voltarLoginRecep)

        # tela do admin
        self.tela_cadastro.pushButton.clicked.connect(self.abrirCadastroRecep)
        self.cadastrar_recp.pushButton.clicked.connect(self.cadastroRecep)
        self.cadastrar_recp.pushButton_2.clicked.connect(self.voltarCadastros)
        self.tela_cadastro.pushButton_2.clicked.connect(self.abrirCadastroMed)
        self.cadastrar_med.pushButton.clicked.connect(self.cadastroMedico)
        self.cadastrar_med.pushButton_2.clicked.connect(self.voltarCadastros)
        self.tela_cadastro.pushButton_3.clicked.connect(self.abrirImpressao)
        self.tela_cadastro.pushButton_4.clicked.connect(self.abrirLoginAdmin)

        # tela do admin = tela de impressão
        self.imprimir_dados.pushButton.clicked.connect(self.abrirImpRecep)
        self.imprimir_dados.pushButton_2.clicked.connect(self.abrirImpMed)
        self.imprimir_dados.pushButton_4.clicked.connect(self.voltarCadastros)

        # tela de impressão = recepcionista
        self.imprimir_recepcionista.pushButton.clicked.connect(self.imprimirRecep)
        self.imprimir_recepcionista.pushButton_2.clicked.connect(self.abrirImpressao)

        # tela de impressão = medico
        self.imprimir_medico.pushButton.clicked.connect(self.imprimirMed)
        self.imprimir_medico.pushButton_2.clicked.connect(self.abrirImpressao)


        # tela do recepcionista
        self.tela_recepcionista.pushButton_2.clicked.connect(self.abrirAtendimento)
        self.tela_recepcionista.pushButton_3.clicked.connect(self.abrirConsulta)
        self.tela_recepcionista.pushButton_5.clicked.connect(self.voltarLoginRecep)

        # tela do recepcionista = tela de atendimento
        self.tela_atendimento.pushButton.clicked.connect(self.iniciarAtendimento)
        self.tela_atendimento.pushButton_2.clicked.connect(self.finalizarAtendimento)
        #self.finalizar_atendimento.pushButton.clicked.connect(self.finalizarAtendimento)
        #self.finalizar_atendimento.pushButton_2.clicked.connect(self.abrirAtendimento)
        self.tela_atendimento.pushButton_3.clicked.connect(self.abrirAddGuiche)
        self.adicionar_guiche.pushButton.clicked.connect(self.addGuiche)
        self.tela_atendimento.pushButton_7.clicked.connect(self.excluirGuiche)
        self.adicionar_guiche.pushButton_2.clicked.connect(self.abrirAtendimento)
        self.tela_atendimento.pushButton_4.clicked.connect(self.ativarGuiche)
        self.tela_atendimento.pushButton_6.clicked.connect(self.desativar_Guiche)
        self.tela_atendimento.pushButton_5.clicked.connect(self.abrirTelaRecepcionista)

        # tela do recepcionista = tela de consulta
        self.tela_consulta.pushButton.clicked.connect(self.abrirRealizarConsult)
        self.realizar_consulta.pushButton.clicked.connect(self.realizarConsulta)
        self.realizar_consulta.pushButton_2.clicked.connect(self.abrirConsulta)
        self.tela_consulta.pushButton_2.clicked.connect(self.enviarConsulta)
        self.tela_consulta.pushButton_3.clicked.connect(self.abrirExcluirConsult)
        self.excluir_consulta.pushButton.clicked.connect(self.buscCons)
        self.excluir_consulta.pushButton_2.clicked.connect(self.excluirConsulta)
        self.excluir_consulta.pushButton_3.clicked.connect(self.abrirConsulta)
        self.tela_consulta.pushButton_4.clicked.connect(self.abrirTipoConsult)
        self.verifica_tipo.pushButton.clicked.connect(self.verificaTipo)
        self.verifica_tipo.pushButton_2.clicked.connect(self.abrirConsulta)
        self.verifica_tipo.pushButton_3.clicked.connect(self.enviarCons)
        self.tela_consulta.pushButton_5.clicked.connect(self.abrirTelaRecepcionista)

        # Tela do médico
        self.tela_medico.pushButton.clicked.connect(self.abrirListaPaciente)
        self.lista_pacientes.pushButton_2.clicked.connect(self.excluiPacientes)
        self.lista_pacientes.pushButton_3.clicked.connect(self.abrirTelaMedico)
        self.atualizar_consulta.pushButton_3.clicked.connect(self.buscConsult)
        self.atualizar_consulta.pushButton.clicked.connect(self.atualizarConsulta)
        self.atualizar_consulta.pushButton_2.clicked.connect(self.abrirTelaMedico)
        self.tela_medico.pushButton_4.clicked.connect(self.abrirAtualizarCons)
        self.tela_medico.pushButton_3.clicked.connect(self.voltarLoginMedico)

    def loginAdmin(self):
        """
        Realiza o login de um administrador.

        Este metodo obtem os dados de CPF e senha informados na interface de login do administrador, envia esses dados para o 
        servidor atraves de um socket e recebe uma resposta do servidor para autenticacao

        Returns
        -------
            None: A interface e atualizada com base na resposta do servidor. Em caso de sucesso, a tela de cadastros e aberta. 
            Caso contrario, exibe uma mensagem de erro na interface.
        """
        cpf = self.login_admin.lineEdit.text()
        password = self.login_admin.lineEdit_2.text()
        if not(cpf=='' or password==''):
            try:
                menssagem =  f'admin,{cpf},{password}'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                # servidor retorna 1 para verdadeiro e 0 para falso
                if recebida == '1':
                    self.abrirTelaCadastros()
                    #limpar os dados
                    self.login_admin.lineEdit.setText("")
                    self.login_admin.lineEdit_2.setText("")
                elif recebida == '0':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ou Senha inválidos! Nenhum Admin cadastrado com esses campos!')
                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
            except:
                cliente_socket.close()
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Informe todos os campos para fazer o Login')
            

    def loginMedico(self):
        """
        Realiza o login de um medico.

        Este metodo obtem os dados de CPF e senha informados na interface de login do medico, envia esses dados 
        para o servidor atraves de um socket e recebe uma resposta do servidor para autenticacao

        Returns
        -------
        None 
            A interface e atualizada com base na resposta do servidor. Em caso de sucesso, a tela do medico e aberta. 
            Caso contrario, exibe uma mensagem de erro na interface
        """
        cpf = self.tela_login_medico.lineEdit.text()
        password = self.tela_login_medico.lineEdit_2.text()
        if not(cpf=='' or password==''):
            try:
                menssagem =  f'medico,{cpf},{password}'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                # servidor retorna 1 para verdadeiro e 0 para falso
                if recebida == '1':
                    self.abrirTelaMedico()
                    #limpar os dados
                    self.tela_login_medico.lineEdit.setText("")
                    self.tela_login_medico.lineEdit_2.setText("")
                elif recebida == '0':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ou Senha inválidos! Nenhum Medico cadastrado com esses campos!')
                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
            except:
                cliente_socket.close()
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Informe todos os campos para fazer o Login')
    
    
    def loginRecep(self):
        """
        Realiza o login de um recepcionista

        Este metodo obtem os dados de CPF e senha informados na interface de login do recepcionista, envia esses dados para o servidor 
        atraves de um socket e recebe uma resposta do servidor para autenticacao

        Returns
        -------
        None 
            A interface e atualizada com base na resposta do servidor. Em caso de sucesso, a tela do recepcionista e aberta. 
            Caso contrario, exibe uma mensagem de erro na interface
        """
        cpf = self.tela_login_recepcionista.lineEdit.text()
        password = self.tela_login_recepcionista.lineEdit_2.text()
        if not(cpf=='' or password==''):
            try:
                menssagem =  f'recepcionista,{cpf},{password}'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                # servidor retorna 1 para verdadeiro e 0 para falso
                print('Recebida:',recebida)
                if recebida == '1':
                    self.abrirTelaRecepcionista()
                    #limpar os dados
                    self.tela_login_recepcionista.lineEdit.setText("")
                    self.tela_login_recepcionista.lineEdit_2.setText("")
                elif recebida == '0':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ou Senha inválidos! Nenhum Recepcionista cadastrado com esses campos!')
                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
            except:
                cliente_socket.close()
        else:
            # imprime uma menssagem de erro
            QtWidgets.QMessageBox.information(None, 'interface', 'Informe todos os campos para fazer o Login')

    def cadastroMedicoLogin(self):
        """
        Realiza o cadastro de um medico na interface de login.

        Este metodo obtem os dados de CPF, nome, telefone, data de nascimento, email, especialidade, horario de atendimento, CRM e senha informados 
        na interface de cadastro de medico na tela de login. Esses dados sao enviados para o servidor atraves de um socket para realizar o cadastro

        Returns
        -------
        None
            A interface e atualizada com base na resposta do servidor. Em caso de sucesso, exibe uma mensagem de confirmacao e limpa os campos de cadastro. 
            Caso contrario, exibe uma mensagem de erro na interface
        """
        cpf = self.cadastrar_medico.lineEdit.text()
        nome = self.cadastrar_medico.lineEdit_2.text()
        telefone = self.cadastrar_medico.lineEdit_3.text()
        dt_nasc = self.cadastrar_medico.lineEdit_4.text()
        email = self.cadastrar_medico.lineEdit_5.text()
        especialidade = self.cadastrar_medico.lineEdit_6.text()
        hr_atendimento = self.cadastrar_medico.lineEdit_7.text()
        crm = self.cadastrar_medico.lineEdit_8.text()
        senha = self.cadastrar_medico.lineEdit_10.text()
        if not(cpf=='' or nome=='' or telefone=='' or dt_nasc=='' or email=='' or especialidade=='' or hr_atendimento=='' or crm=='' or senha==''):
            try:
                menssagem =  f'cad_medicologin,{cpf},{nome},{telefone},{dt_nasc},{email},{especialidade},{hr_atendimento},{crm},{senha}'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                # servidor retorna 1 para verdadeiro e 0 para falso
                if recebida == '1':
                    QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro realizado com sucesso!')
                    #limpar os dados
                    self.cadastrar_medico.lineEdit.setText("")
                    self.cadastrar_medico.lineEdit_2.setText("")
                    self.cadastrar_medico.lineEdit_3.setText("")
                    self.cadastrar_medico.lineEdit_4.setText("")
                    self.cadastrar_medico.lineEdit_5.setText("")
                    self.cadastrar_medico.lineEdit_6.setText("")
                    self.cadastrar_medico.lineEdit_7.setText("")
                    self.cadastrar_medico.lineEdit_8.setText("")
                    self.cadastrar_medico.lineEdit_10.setText("")
                elif recebida == '0':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ja cadastrado!')    
                elif recebida == '3':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ja cadastrado!')
                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
            except:
                QtWidgets.QMessageBox.information(None, 'interface', 'Erro: CPF já cadastrado!')
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro não realizado! informe todos os campos.')

    def cadastroMedico(self):
        """
        Realiza o cadastro de um medico

        Este metodo obtem os dados de CPF, nome, telefone, data de nascimento, email, especialidade, horario de atendimento, CRM e senha informados na 
        tela de cadastro de medico na tela do recepcionista. Esses dados sao enviados para o servidor atraves de um socket para realizar o cadastro

        Returns
        -------
        None
            A interface e atualizada com base na resposta do servidor. Em caso de sucesso, exibe uma mensagem de confirmacao e limpa os campos de cadastro. 
            Caso contrario, exibe uma mensagem de erro na interface.
        """
        cpf = self.cadastrar_med.lineEdit.text()
        nome = self.cadastrar_med.lineEdit_2.text()
        telefone = self.cadastrar_med.lineEdit_3.text()
        dt_nasc = self.cadastrar_med.lineEdit_4.text()
        email = self.cadastrar_med.lineEdit_5.text()
        especialidade = self.cadastrar_med.lineEdit_6.text()
        hr_atendimento = self.cadastrar_med.lineEdit_7.text()
        crm = self.cadastrar_med.lineEdit_8.text()
        senha = self.cadastrar_med.lineEdit_10.text()
        if not(cpf=='' or nome=='' or telefone=='' or dt_nasc=='' or email=='' or especialidade=='' or hr_atendimento=='' or crm=='' or senha==''):
            try:
                menssagem =  f'cad_medico,{cpf},{nome},{telefone},{dt_nasc},{email},{especialidade},{hr_atendimento},{crm},{senha}'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                # servidor retorna 1 para verdadeiro e 0 para falso
                if recebida == '1':
                    QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro realizado com sucesso!')
                    #limpar os dados
                    self.cadastrar_med.lineEdit.setText("")
                    self.cadastrar_med.lineEdit_2.setText("")
                    self.cadastrar_med.lineEdit_3.setText("")
                    self.cadastrar_med.lineEdit_4.setText("")
                    self.cadastrar_med.lineEdit_5.setText("")
                    self.cadastrar_med.lineEdit_6.setText("")
                    self.cadastrar_med.lineEdit_7.setText("")
                    self.cadastrar_med.lineEdit_8.setText("")
                    self.cadastrar_med.lineEdit_10.setText("")
                elif recebida == '0':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ja cadastrado!')
                elif recebida == '3':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ja cadastrado!')
                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
            except:
                QtWidgets.QMessageBox.information(None, 'interface', 'Erro: CPF já cadastrado!')
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro não realizado! informe todos os campos.')
    
    def cadastroRecepLogin(self):
        """
        Realiza o cadastro de um recepcionista na tela de login

        Este metodo obtem os dados de CPF, nome, telefone, data de nascimento, email e senha informados na tela de cadastro 
        de recepcionista na tela de login. Esses dados sao enviados para o servidor atraves de um socket para realizar o cadastro

        Returns
        -------
        None
            A interface e atualizada com base na resposta do servidor. Em caso de sucesso, exibe uma mensagem de confirmacao e limpa os campos de cadastro. 
            Caso contrario, exibe uma mensagem de erro na interface
        """
        cpf = self.cadastrar_recepcionista.lineEdit.text()
        nome = self.cadastrar_recepcionista.lineEdit_2.text()
        telefone = self.cadastrar_recepcionista.lineEdit_3.text()
        dt_nasc = self.cadastrar_recepcionista.lineEdit_4.text()
        email = self.cadastrar_recepcionista.lineEdit_5.text()
        senha = self.cadastrar_recepcionista.lineEdit_6.text()
        # verifico se todos os dados foram preenchidos
        if not(cpf=='' or nome=='' or telefone=='' or dt_nasc=='' or email=='' or senha==''):
            try:
                menssagem =  f'cad_receplogin,{cpf},{nome},{telefone},{dt_nasc},{email},{senha}'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                # servidor retorna 1 para verdadeiro e 0 para falso
                if recebida == '1':
                    QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro realizado com sucesso!')
                    #limpar os dados
                    self.cadastrar_recepcionista.lineEdit.setText("")
                    self.cadastrar_recepcionista.lineEdit_2.setText("")
                    self.cadastrar_recepcionista.lineEdit_3.setText("")
                    self.cadastrar_recepcionista.lineEdit_4.setText("")
                    self.cadastrar_recepcionista.lineEdit_5.setText("")
                    self.cadastrar_recepcionista.lineEdit_6.setText("")
                elif recebida == '0':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ja cadastrado!')
                elif recebida == '3':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ja cadastrado!')
                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
            except:
                QtWidgets.QMessageBox.information(None, 'interface', 'Erro: CPF já cadastrado!')
        else:
            # imprime uma menssagem de erro
            QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro não realizado! informe todos os campos.')

    def cadastroRecep(self):
        """
        Realiza o cadastro de um recepcionista na tela de cadastro

        Este metodo obtem os dados de CPF, nome, telefone, data de nascimento, email e senha informados na tela de cadastro de recepcionista. 
        Esses dados sao enviados para o servidor atraves de um socket para realizar o cadastro

        Returns
        -------
        None
            A interface e atualizada com base na resposta do servidor. Em caso de sucesso, exibe uma mensagem de confirmacao e limpa os campos de cadastro. 
            Caso contrario, exibe uma mensagem de erro na interface.
        """
        cpf = self.cadastrar_recp.lineEdit.text()
        nome = self.cadastrar_recp.lineEdit_2.text()
        telefone = self.cadastrar_recp.lineEdit_3.text()
        dt_nasc = self.cadastrar_recp.lineEdit_4.text()
        email = self.cadastrar_recp.lineEdit_5.text()
        senha = self.cadastrar_recp.lineEdit_6.text()
        # verifico se todos os dados foram preenchidos
        if not(cpf=='' or nome=='' or telefone=='' or dt_nasc=='' or email=='' or senha==''):
            try: 
                menssagem =  f'cad_recep,{cpf},{nome},{telefone},{dt_nasc},{email},{senha}'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                # servidor retorna 1 para verdadeiro e 0 para falso
                if recebida == '1':
                    QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro realizado com sucesso!')
                    #limpar os dados
                    self.cadastrar_recp.lineEdit.setText("")
                    self.cadastrar_recp.lineEdit_2.setText("")
                    self.cadastrar_recp.lineEdit_3.setText("")
                    self.cadastrar_recp.lineEdit_4.setText("")
                    self.cadastrar_recp.lineEdit_5.setText("")
                    self.cadastrar_recp.lineEdit_6.setText("")
                elif recebida == '0':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ja cadastrado!')
                elif recebida == '3':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ja cadastrado!')
                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
            except:
                QtWidgets.QMessageBox.information(None, 'interface', 'Erro: CPF já cadastrado!')
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro não realizado! informe todos os campos.')

    def cadastroAdmin(self):
        """
        Realiza o cadastro de um administrador na tela de cadastro

        Este metodo obtem os dados de CPF, nome e senha informados na tela de cadastro de administrador. 
        Esses dados sao enviados para o servidor atraves de um socket para realizar o cadastro

        Returns
        -------
        None
            A interface e atualizada com base na resposta do servidor. Em caso de sucesso, exibe uma mensagem de confirmacao e limpa os campos de cadastro. 
            Caso contrario, exibe uma mensagem de erro na interface
        """
        cpf_admin = self.cadastrar_admin.lineEdit.text()
        nome = self.cadastrar_admin.lineEdit_2.text()
        senha = self.cadastrar_admin.lineEdit_3.text()
        if not(cpf_admin=='' or nome=='' or senha==''):
            try:
                menssagem =  f'cad_admin,{cpf_admin},{nome},{senha}'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                # servidor retorna 1 para verdadeiro e 0 para falso
                if recebida == '1':
                    QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro realizado com sucesso!')
                    #limpar os dados
                    self.cadastrar_admin.lineEdit.setText("")
                    self.cadastrar_admin.lineEdit_2.setText("")
                    self.cadastrar_admin.lineEdit_3.setText("")
                elif recebida == '0':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ja cadastrado!')
                elif recebida == '3':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ja cadastrado!')
                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
            except:
                QtWidgets.QMessageBox.information(None, 'interface', 'Erro: CPF já cadastrado!')
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro não realizado! informe todos os campos.')

    def iniciarAtendimento(self):
        """
        Inicia o atendimento em um guiche

        Este metodo envia uma mensagem ao servidor indicando a solicitação de iniciar o atendimento. O servidor processa a solicitacao e 
        retorna uma resposta que e tratada pela interface

        Returns
        -------
        None
            A interface e atualizada com base na resposta do servidor. Em caso de erro, exibe uma mensagem de erro na interface. 
            Em caso de sucesso, exibe a mensagem de confirmacao na interface
        """
        menssagem =  'atendimento'
        cliente_socket.send(menssagem.encode())
        print('menssagem enviada')
        recebida = cliente_socket.recv(1024).decode()
        if recebida == '0':
            QtWidgets.QMessageBox.critical(None, 'interface','Esse recepcionista não foi cadastrado em nenhum guiche.', QMessageBox.Ok)
        elif recebida == '3':
            QtWidgets.QMessageBox.critical(None, 'interface','guiche está ocupado.', QMessageBox.Ok)
        elif recebida == '2':
            QtWidgets.QMessageBox.critical(None, 'interface','guiche está Inativo.', QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(None, 'interface', str(recebida), QMessageBox.Ok)

    def finalizarAtendimento(self):
        """
        Finaliza o atendimento em um guiche

        Este metodo envia uma mensagem ao servidor indicando a solicitacao de finalizar o atendimento. O servidor processa a solicitacao e 
        retorna uma resposta que e tratada pela interface

        Returns
        -------
        None
            A interface exibe uma mensagem de sucesso ou erro com base na resposta do servidor
        """
        menssagem =  'finalizar_atendimento'
        cliente_socket.send(menssagem.encode())
        print('menssagem enviada')
        recebida = cliente_socket.recv(1024).decode()
        if recebida == '2':
            QtWidgets.QMessageBox.critical(None, 'interface','O guiche já está livre.', QMessageBox.Ok)
        elif recebida == '0':
            QtWidgets.QMessageBox.critical(None, 'interface','Esse recepcionista não foi cadastrado em nenhum guiche.', QMessageBox.Ok)
        elif recebida == '3':
            QtWidgets.QMessageBox.critical(None, 'interface','guiche está Inativo.', QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(None, 'interface', recebida, QMessageBox.Ok)

    def addGuiche(self):
        """
        Adiciona um novo guiche

        Este metodo obtem os dados de senha, status e modo informados na interface de adicionar guiche. Esses dados sao enviados 
        para o servidor atraves de um socket para adicionar o guiche. O servidor processa a solicitacao e retorna uma resposta que e tratada pela interface
       
        Returns
        -------
        None
            A interface exibe uma mensagem de sucesso ou erro com base na resposta do servidor
        """
        senha = self.adicionar_guiche.lineEdit.text()
        status = self.adicionar_guiche.lineEdit_2.text()
        modo = self.adicionar_guiche.lineEdit_3.text()
        if not(senha=='' or status=='' or modo==''):
            try:
                menssagem =  f'adicionaguiche,{status},{senha},{modo}'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                print('recebida:',recebida)
                # servidor retorna 1 para verdadeiro e 0 para falso
                if recebida == '1':
                    QtWidgets.QMessageBox.information(None, 'interface', 'Guiche adicionado!')
                    #limpar os dados
                    self.adicionar_guiche.lineEdit.setText("")
                    self.adicionar_guiche.lineEdit_2.setText("")
                    self.adicionar_guiche.lineEdit_3.setText("")
                elif recebida == '0':
                    QtWidgets.QMessageBox.information(None, 'interface', 'Recepcionista ja está cadastrado em um guiche')
                elif recebida == '2':
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro: Não foi possivel adicionar o guiche!')
                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
            except:
                QtWidgets.QMessageBox.information(None, 'interface', 'Erro: Não foi possivel adicionar o guiche!')
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Guiche não adicionado! informe todos os campos.')

    def excluirGuiche(self):
        """
        Exclui um guiche

        Este metodo exibe uma caixa de dialogo de confirmacao para verificar se o usuario realmente deseja excluir o guiche. 
        Caso ele queira, envia uma mensagem ao servidor indicando a solicitacao de exclusao do guiche. O servidor processa a solicitacao e 
        retorna uma resposta que é tratada pela interface. 

        Returns
        -------
        None 
            A interface exibe uma mensagem dependo da resposta do servidor,para cada caso e exibido uma caixa de dialogo
        """
        confirm = QMessageBox.question(self, 'Confirmação', 'Deseja realmente excluir?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            menssagem =  'excluiguiche'
            cliente_socket.send(menssagem.encode())
            print('menssagem enviada')
            recebida = cliente_socket.recv(1024).decode()
            if recebida == '1':
                QtWidgets.QMessageBox.information(None, 'interface', 'Guiche excluido')
            elif recebida == '0':
                QtWidgets.QMessageBox.information(None, 'interface', 'O Guiche já está ATIVO')
            elif recebida == '2':
                QtWidgets.QMessageBox.information(None, 'interface', 'Guiche não encontrado!')
            elif recebida == '3':
                QtWidgets.QMessageBox.critical(None, 'interface','Esse recepcionista não foi cadastrado em nenhum guiche.', QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Exclusão cancelada')
    
    def ativarGuiche(self):
        """
        Ativa um guiche

        Este metodo envia uma mensagem ao servidor indicando a solicitacao de ativar o guiche. O servidor processa a solicitacao 
        e retorna uma resposta que e tratada pela interface

        Returns
        -------
        None
            A interface exibe uma mensagem de sucesso ou erro com base na resposta do servidor
        """
        menssagem =  'ativarguiche'
        cliente_socket.send(menssagem.encode())
        print('menssagem enviada')
        recebida = cliente_socket.recv(1024).decode()
        if recebida == '1':
            QtWidgets.QMessageBox.information(None, 'interface', 'Guiche ATIVADO!')
        elif recebida == '0':
            QtWidgets.QMessageBox.information(None, 'interface', 'O Guiche já está ATIVO')
        elif recebida == '2':
            QtWidgets.QMessageBox.information(None, 'interface', 'Guiche não encontrado!')
        elif recebida == '3':
            QtWidgets.QMessageBox.critical(None, 'interface','Esse recepcionista não foi cadastrado em nenhum guiche.', QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
  
    def desativar_Guiche(self):
        """
        Desativa um guiche

        Este metodo envia uma mensagem ao servidor indicando a solicitacao de desativar o guiche. O servidor processa a solicitacao 
        e retorna uma resposta que e tratada pela interface

        Returns
        -------
        None
            A interface exibe uma mensagem de sucesso ou erro com base na resposta do servidor
        """
        menssagem =  'desativarguiche'
        cliente_socket.send(menssagem.encode())
        print('menssagem enviada')
        recebida = cliente_socket.recv(1024).decode()
        if recebida == '1':
            QtWidgets.QMessageBox.information(None, 'interface', 'Guiche DESATIVADO!')
        elif recebida == '0':
            QtWidgets.QMessageBox.information(None, 'interface', 'O Guiche já está INATIVO')
        elif recebida == '2':
            QtWidgets.QMessageBox.information(None, 'interface', 'Guiche não encontrado!')
        elif recebida == '3':
            QtWidgets.QMessageBox.critical(None, 'interface','Esse recepcionista não foi cadastrado em nenhum guiche.', QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')

    def imprimirRecep(self):
        """
        Imprime os dados de um recepcionista

        Este metodo envia uma mensagem ao servidor indicando a solicitacao de imprimir os dados de um recepcionista com base no CPF informado. 
        O servidor processa a solicitacao e retorna uma resposta que e tratada pela interface

        Returns
        -------
        None 
            A interface exibe os dados do recepcionista ou uma mensagem de aviso caso nenhum recepcionista seja encontrado com o CPF informado
        """            
        cpf = self.imprimir_recepcionista.lineEdit_5.text()
        if not(cpf==''):
            menssagem =  f'imprecep,{cpf}'
            cliente_socket.send(menssagem.encode())
            print('menssagem enviada')
            recebida = cliente_socket.recv(1024).decode().split(",")
            if recebida[0] == '1':
                self.imprimir_recepcionista.lineEdit_6.setText(recebida[1])
                self.imprimir_recepcionista.lineEdit_7.setText(recebida[2])
                self.imprimir_recepcionista.lineEdit_8.setText(recebida[3])
                self.imprimir_recepcionista.lineEdit_10.setText(recebida[4])
                self.imprimir_recepcionista.lineEdit_11.setText(recebida[5])
            else:
                QtWidgets.QMessageBox.warning(None, "interface_grafica", 'Nenhum recepcionista foi registrada com este CPF.')
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Campo CPF não foi preenchido! Informe um CPF.')

    def imprimirMed(self):
        """
        Imprime os dados de um medico

        Este metodo envia uma mensagem ao servidor indicando a solicitacao de imprimir os dados de um medico com base no CPF informado. 
        O servidor processa a solicitacao e retorna uma resposta que e tratada pela interface

        Returns
        -------
        None
            A interface exibe os dados do medico ou uma mensagem de aviso caso nenhum medico seja encontrado com o CPF informado.
        """
        cpf = self.imprimir_medico.lineEdit_5.text()
        if not(cpf==''):
            menssagem =  f'impmedico,{cpf}'
            cliente_socket.send(menssagem.encode())
            print('menssagem enviada')
            recebida = cliente_socket.recv(1024).decode().split(",")
            if recebida[0] == '1':
                self.imprimir_medico.lineEdit_16.setText(recebida[1])
                self.imprimir_medico.lineEdit_17.setText(recebida[2])
                self.imprimir_medico.lineEdit_18.setText(recebida[3])
                self.imprimir_medico.lineEdit_19.setText(recebida[4])
                self.imprimir_medico.lineEdit_20.setText(recebida[5])
                self.imprimir_medico.lineEdit_21.setText(recebida[6])
                self.imprimir_medico.lineEdit_22.setText(str(recebida[7]))
                self.imprimir_medico.lineEdit_24.setText(recebida[8])
            else:
                QtWidgets.QMessageBox.warning(None, "interface_grafica", 'Nenhum medico foi registrada com este CPF.')
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Campo CPF não foi preenchido! Informe um CPF.')
    
    def realizarConsulta(self):
        """
        Realiza uma consulta medica

        Este metodo obtem os dados do paciente, medico, recepcionista e tipo de consulta informados na interface e envia uma mensagem ao 
        servidor solicitando a realizacao da consulta. O servidor processa a solicitacao e retorna uma resposta que é tratada pela interface. 

        Returns
        -------
        None
            A interface exibe uma mensagem de confirmacao em caso de sucesso ou mensagens de aviso em caso de erro ou dados incorretos.
        """
        cpf_paciente = self.realizar_consulta.lineEdit.text()
        nome_paciente = self.realizar_consulta.lineEdit_2.text()
        telefone = self.realizar_consulta.lineEdit_3.text()
        dt_nasc = self.realizar_consulta.lineEdit_4.text()
        medico = self.realizar_consulta.comboBox.currentText()
        crm = self.realizar_consulta.lineEdit_6.text()
        tipo = self.realizar_consulta.lineEdit_7.text()
        cpf_medico = self.realizar_consulta.lineEdit_9.text()
        cpf_recepcionista = self.realizar_consulta.lineEdit_10.text()
        if not(cpf_paciente=='' or nome_paciente=='' or telefone=='' or dt_nasc=='' or medico=='' or crm=='' or tipo=='' or cpf_medico=='' or cpf_recepcionista==''):
            try:
                menssagem =  f'realizarconsult,{cpf_paciente},{nome_paciente},{telefone},{dt_nasc},{medico},{crm},{tipo},{cpf_medico},{cpf_recepcionista}'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                print('recebida',recebida)
                # servidor retorna 1 para verdadeiro e 0 para falso
                if recebida == '1':
                    QtWidgets.QMessageBox.information(None, 'interface', 'Consulta realizada com sucesso!')
                    #limpar os dados
                    self.realizar_consulta.lineEdit.setText("")
                    self.realizar_consulta.lineEdit_2.setText("")
                    self.realizar_consulta.lineEdit_3.setText("")
                    self.realizar_consulta.lineEdit_4.setText("")
                    #self.realizar_consulta.comboBox.setCurrentIndex(0)
                    self.realizar_consulta.lineEdit_6.setText("")
                    self.realizar_consulta.lineEdit_7.setText("")
                    self.realizar_consulta.lineEdit_9.setText("")
                    self.realizar_consulta.lineEdit_10.setText("")
                elif recebida == '2':
                    QtWidgets.QMessageBox.warning(None, "interface", 'Consulta não realizada')
                elif recebida == '3':
                    QtWidgets.QMessageBox.warning(None, "interface", 'Dados do MÉDICO e do RECEPCIONISTA estão errados! verifique os campos.')
                elif recebida == '4':
                    QtWidgets.QMessageBox.warning(None, "interface", 'Dados do MÉDICO estão errados! verifique os campos.')
                elif recebida == '5':
                    QtWidgets.QMessageBox.warning(None, "interface", 'Dados do RECEPCIONISTA estão errados! verifique os campos.')
                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
            except:
                QtWidgets.QMessageBox.information(None, 'interface', 'Erro: Impossivel de realizar consulta!')
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro não realizado! informe todos os campos.')
    
    def enviarConsulta(self):
        """
        Envia a consulta para a lista de pacientes.

        Este metodo envia uma mensagem ao servidor indicando a solicitaco de enviar a consulta para a lista de pacientes. 
        O servidor processa a solicitacao e retorna uma resposta que e tratada pela interface

        Returns
        -------
        None
            A interface exibe mensagens de confirmacao, aviso ou erro com base na resposta do servidor.
        """
        menssagem =  f'enviarconsult'
        cliente_socket.send(menssagem.encode())
        print('menssagem enviada')
        recebida = cliente_socket.recv(1024).decode()
        if recebida == '1':
            QtWidgets.QMessageBox.information(None, "interface", 'Paciente enviado para a lista de pacientes')
        elif recebida == '3':
            QtWidgets.QMessageBox.information(None, 'interface', 'Erro: Paciente não enviado!') 
        elif recebida == '4':
            QtWidgets.QMessageBox.warning(None, "interface", 'Dados do Médico estão errados! verifique os campos.') 
        elif recebida == '5':
            QtWidgets.QMessageBox.warning(None, "interface", 'O paciente já está na lista de pacientes do médico!')
        elif recebida == '6':
            QtWidgets.QMessageBox.warning(None, "interface", 'O recepcionista não cadastrou nenhuma consulta!')
        elif recebida == '0':
            QtWidgets.QMessageBox.warning(None, "interface", 'Erro: ao enviar uma consulta!')
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Erro: NÃO ENVIOU!')

    def buscCons(self):
        """
        Realiza a busca de uma consulta para exclui-la

        Este metodo realiza a busca de uma consulta no servidor com base no CPF informado. O CPF e enviado ao servidor por meio de uma mensagem.
        O servidor processa a busca e retorna uma resposta que e tratada pela interface. 

        Returns
        -------
        None
            A interface exibe os dados da consulta encontrada ou exibe uma mensagem informando que nenhum paciente foi encontrado com o CPF informado.
        """
        cpf = self.excluir_consulta.lineEdit.text()
        if not(cpf==''):
            menssagem =  f'busconsult,{cpf}'
            cliente_socket.send(menssagem.encode())
            print('menssagem enviada')
            recebida = cliente_socket.recv(1024).decode().split(",")
            if recebida[0] == '1':
                self.excluir_consulta.lineEdit_2.setText(recebida[1])
                self.excluir_consulta.lineEdit_3.setText(recebida[2])
                self.excluir_consulta.lineEdit_4.setText(recebida[3])
                self.excluir_consulta.lineEdit_5.setText(recebida[4])
                self.excluir_consulta.lineEdit_6.setText(str(recebida[5]))
                self.excluir_consulta.lineEdit_7.setText(recebida[6])
                self.excluir_consulta.lineEdit_9.setText(recebida[7])
                self.excluir_consulta.lineEdit_10.setText(recebida[8])
            else:
                QtWidgets.QMessageBox.warning(None, "interface_grafica", 'Nenhum paciente foi registrada com este CPF.')
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Busca não realizada! informe o CPF.')

    def excluirConsulta(self):
        """
        Exclui uma consulta

        Este metodo exibe uma caixa de dialogo de confirmacao para o usuario. Se o usuario confirmar a exclusao, o metodo envia uma mensagem ao servidor
        indicando a solicitacao de exclusao da consulta. O CPF da consulta e obtido a partir do campo de texto na interface. 

        Returns
        -------
        None
            A interface exibe uma mensagem de sucesso, de erro ou informa que o paciente nao foi encontrado com o CPF informado.
        """
        confirm = QMessageBox.question(self, 'Confirmação', 'Deseja realmente excluir?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            cpf = self.excluir_consulta.lineEdit.text()
            menssagem =  f'excluirconsult,{cpf}'
            cliente_socket.send(menssagem.encode())
            print('menssagem enviada')
            recebida = cliente_socket.recv(1024).decode().split(",")
            if recebida[0] == '1':
                QtWidgets.QMessageBox.information(None, 'interface', 'Dado excluido')
                self.excluir_consulta.lineEdit.setText('')
                self.excluir_consulta.lineEdit_2.setText('')
                self.excluir_consulta.lineEdit_3.setText('')
                self.excluir_consulta.lineEdit_4.setText('')
                self.excluir_consulta.lineEdit_5.setText('')
                self.excluir_consulta.lineEdit_6.setText('')
                self.excluir_consulta.lineEdit_7.setText('')
                self.excluir_consulta.lineEdit_9.setText('')
                self.excluir_consulta.lineEdit_10.setText('')
            elif recebida[0] == '0':
                QtWidgets.QMessageBox.information(None, 'interface','Paciente não encontrado!')
            else:
                QtWidgets.QMessageBox.information(None, 'interface', 'Eroo ao excluir um dado')
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Exclusão cancelada')

    def verificaTipo(self):
        """
        Verifica o tipo de consulta

        Este metodo verifica o tipo de consulta com base no CPF informado. O CPF e obtido a partir do campo de texto na interface. O metodo envia uma mensagem 
        ao servidor indicando a solicitacao de verificacao do tipo de consulta. O servidor processa a solicitacao e retorna uma resposta que e tratada pela interface. 

        Returns
        -------
        None
            A interface exibe uma mensagem com o tipo de consulta ou informa que o CPF nao foi encontrado.
        """
        cpf = self.verifica_tipo.lineEdit.text()
        if not(cpf==''):
            menssagem =  f'verificartipo,{cpf}'
            cliente_socket.send(menssagem.encode())
            print('menssagem enviada')
            recebida = cliente_socket.recv(1024).decode()
            if recebida == '1':
                QtWidgets.QMessageBox.information(None, 'interface', 'Nova Consulta! Valor = R$:300,00')
            elif recebida == '0':
                QtWidgets.QMessageBox.information(None, 'interface', 'Retorno! Valor = Gratuito.')
            else:
                QtWidgets.QMessageBox.information(None, 'interface', 'CPF não encontrado')
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Campo não preenchido! Imforme um CPF.')

    def enviarCons(self):
        """
        Envia consulta para a lista de pacientes.

        Este metodo envia uma consulta para a lista de pacientes com base no CPF informado. O CPF e obtido a partir do campo de texto na interface. 
        O metodo envia uma mensagem ao servidor indicando a solicitação de enviar a consulta para a lista de pacientes. O servidor processa a solicitacao e 
        retorna uma resposta que e tratada pela interface. 

        Returns
        -------
        None
            A interface exibe uma mensagem com o resultado da operacao
        """
        cpf = self.verifica_tipo.lineEdit.text()
        if not(cpf==''):
            menssagem =  f'enviarcon,{cpf}'
            cliente_socket.send(menssagem.encode())
            print('menssagem enviada')
            recebida = cliente_socket.recv(1024).decode()
            if recebida == '1':
                QtWidgets.QMessageBox.information(None, "interface", 'Paciente enviado para a lista de pacientes')
            elif recebida == '3':
                QtWidgets.QMessageBox.information(None, 'interface', 'Erro: Paciente não enviado!') 
            elif recebida == '4':
                QtWidgets.QMessageBox.warning(None, "interface", 'Dados do Médico estão errados! verifique os campos.') 
            elif recebida == '5':
                QtWidgets.QMessageBox.warning(None, "interface", 'O paciente já está na lista de pacientes do médico!')
            elif recebida == '6':
                QtWidgets.QMessageBox.warning(None, "interface", 'O recepcionista não cadastrou nenhuma consulta!')
            elif recebida == '0':
                QtWidgets.QMessageBox.warning(None, "interface", 'Erro: ao enviar uma consulta!')
            else:
                QtWidgets.QMessageBox.information(None, 'interface', 'Erro: NÃO ENVIOU!')
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Campo não preenchido! Imforme um CPF.')
    
    def buscConsult(self):
        """
        Busca informacoes de uma consulta para atualiza-la

        Este metodo realiza uma busca por informacoes de uma consulta com base no CPF do paciente. O CPF e obtido a partir do campo de texto na interface. 
        O metodo envia uma mensagem ao servidor indicando a solicitacao de busca da consulta. O servidor processa a solicitacao e retorna uma resposta que e tratada pela interface. 

        Returns
        -------
        None 
            A interface exibe as informacoes da consulta encontrada ou uma mensagem de aviso caso nenhum paciente seja registrado com o CPF informado.
        """
        cpf = self.atualizar_consulta.lineEdit_11.text()
        if not(cpf==''):
            menssagem =  f'bconsult,{cpf}'
            cliente_socket.send(menssagem.encode())
            print('menssagem enviada')
            recebida = cliente_socket.recv(1024).decode().split(",")
            self.atualizar_consulta.lineEdit_2.setText('')
            self.atualizar_consulta.lineEdit_3.setText('')
            self.atualizar_consulta.lineEdit_4.setText('')
            self.atualizar_consulta.lineEdit_5.setText('')
            self.atualizar_consulta.lineEdit_6.setText('')
            self.atualizar_consulta.lineEdit_7.setText('')
            self.atualizar_consulta.lineEdit_9.setText('')
            self.atualizar_consulta.lineEdit_10.setText('')
            if recebida[0] == '1':
                self.atualizar_consulta.lineEdit_2.setText(recebida[1])
                self.atualizar_consulta.lineEdit_3.setText(recebida[2])
                self.atualizar_consulta.lineEdit_4.setText(recebida[3])
                self.atualizar_consulta.lineEdit_5.setText(recebida[4])
                self.atualizar_consulta.lineEdit_6.setText(str(recebida[5]))
                self.atualizar_consulta.lineEdit_7.setText(recebida[6])
                self.atualizar_consulta.lineEdit_9.setText(recebida[7])
                self.atualizar_consulta.lineEdit_10.setText(recebida[8])
            else:
                QtWidgets.QMessageBox.warning(None, "interface_grafica", 'Nenhum paciente foi registrada com este CPF.')
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Busca não realizada! informe o CPF.')

    def atualizarConsulta(self):
        """
        Atualiza o tipo de uma consulta

        Este metodo atualiza o tipo de uma consulta para Retorno ou Nova consulta. O CPF do paciente e obtido a partir do campo de texto na interface. O metodo envia 
        uma mensagem ao servidor indicando a solicitacao de atualizacao da consulta. O servidor processa a solicitacao e retorna uma resposta que e tratada pela interface. 

        Returns
        -------
        None 
            A interface exibe uma mensagem de confirmacao ou aviso com base na resposta do servidor.
        """
        cpf = self.atualizar_consulta.lineEdit_11.text()
        if not(cpf==''):
            menssagem =  f'atualizaconsult,{cpf}'
            cliente_socket.send(menssagem.encode())
            print('menssagem enviada')
            recebida = cliente_socket.recv(1024).decode().split(",")
            if recebida[0] == '1':
                QtWidgets.QMessageBox.information(None, 'interface', f"A consulta foi atualizada para o RETORNO")
            elif recebida[0] == '0':
                QtWidgets.QMessageBox.information(None, 'interface', f"A consulta foi atualizada para NOVA consulta")
            else:
                QtWidgets.QMessageBox.information(None, 'interface', f"A consulta não foi encontrada!")
           
            self.atualizar_consulta.lineEdit_11.setText('')
            self.atualizar_consulta.lineEdit_2.setText('')
            self.atualizar_consulta.lineEdit_3.setText('')
            self.atualizar_consulta.lineEdit_4.setText('')
            self.atualizar_consulta.lineEdit_5.setText('')
            self.atualizar_consulta.lineEdit_6.setText('')
            self.atualizar_consulta.lineEdit_7.setText('')
            self.atualizar_consulta.lineEdit_9.setText('')
            self.atualizar_consulta.lineEdit_10.setText('')
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Busca não realizada! informe o CPF.')

    def excluiPacientes(self):
        """
        Exclui um paciente da lista de pacientes

        Este metodo exclui um paciente da lista de pacientes. O paciente selecionado e obtido a partir do item atualmente selecionado na interface. O metodo exibe uma 
        mensagem de confirmacao para garantir a exclusao e envia uma mensagem ao servidor indicando a solicitacao de exclusao do paciente. O servidor processa a solicitacao 
        e retorna uma resposta que e tratada pela interface. 

        Returns
        -------
        None
            A interface exibe uma mensagem de confirmacao ou aviso com base na resposta do servidor.
        """
        item_selecionado = self.lista_pacientes.listWidget.currentItem()
        if item_selecionado is not None:
            self.lista_pacientes.listWidget.takeItem(self.lista_pacientes.listWidget.row(item_selecionado))
            confirm = QMessageBox.question(self, 'Confirmação', 'Deseja realmente excluir?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if confirm == QMessageBox.Yes:
                menssagem = 'excluipaciente'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode().split(",")
                if recebida[0] == '1':
                    QtWidgets.QMessageBox.warning(None, "interface_grafica", "O paciente foi excluído com sucesso.")
                elif recebida[0] =='0':
                    QtWidgets.QMessageBox.warning(None, "interface_grafica", "A tabela está vazia ou não há registros para excluir.")
                elif recebida[0] =='2':
                    QtWidgets.QMessageBox.warning(None, "interface_grafica", "Erro no banco de dados")
                else:
                    QtWidgets.QMessageBox.warning(None, "interface_grafica", "Erro ao excluir.")
            else:
                QtWidgets.QMessageBox.information(None, 'interface', 'Exclusão cancelada')
        else:
            QtWidgets.QMessageBox.warning(None, "interface_grafica", "Selecione um paciente para podelo exclui-lo")
        

    def abrirTelaLoginMedico(self):
        """
        Abre a tela de login para medicos.

        Este metodo altera o endice da pilha de widgets para exibir a tela de login para medicos na interface.
        """
        self.QtStack.setCurrentIndex(1)
            
    def abrirTelaLoginRecepcionista(self):
        """
        Abre a tela de login para recepcionistas.

        Este metodo altera o endice da pilha de widgets para exibir a tela de login para recepcionistas na interface.
        """
        self.QtStack.setCurrentIndex(2)

    def abrirTelaMedico(self):
        """
        Abre a tela principal do medico.

        Este metodo altera o endice da pilha de widgets para exibir a tela principal do medico na interface.
        """
        self.QtStack.setCurrentIndex(3)
    
    def abrirTelaRecepcionista(self):
        """
        Abre a tela principal do recepcionista.

        Este metodo altera o endice da pilha de widgets para exibir a tela principal do recepcionista na interface.
        """
        self.QtStack.setCurrentIndex(4)

    def abrirCadastroMedico(self):
        """
        Abre a tela de cadastro de medico.

        Este metodo altera o indice da pilha de widgets para exibir a tela de cadastro de medico na interface.
        """
        self.QtStack.setCurrentIndex(5)

    def abrirCadastroRecepcionista(self):
        """
        Abre a tela de cadastro de recepcionista.

        Este metodo altera o indice da pilha de widgets para exibir a tela de cadastro de recepcionista na interface.
        """
        self.QtStack.setCurrentIndex(6)
    
    def abrirTelaCadastros(self):
        """
        Abre a tela de cadastros.

        Este metodo altera o indice da pilha de widgets para exibir a tela de cadastros na interface.
        """
        self.QtStack.setCurrentIndex(7)
    
    def abrirCadastroRecep(self):
        """
        Abre a tela de cadastro de recepcionista.

        Este metodo altera o indice da pilha de widgets para exibir a tela de cadastro de recepcionista na interface.
        """
        self.QtStack.setCurrentIndex(8)
    
    def abrirCadastroMed(self):
        """
        Abre a tela de cadastro de medico.

        Este metodo altera o indice da pilha de widgets para exibir a tela de cadastro de medico na interface.
        """
        self.QtStack.setCurrentIndex(9)
    
    def abrirCadastroAdmin(self):
        """
        Abre a tela de cadastro de administrador.

        Este metodo altera o indice da pilha de widgets para exibir a tela de cadastro de administrador na interface.
        """
        self.QtStack.setCurrentIndex(10)
    
    def abrirAtendimento(self):
        """
        Abre a tela de atendimento.

        Este metodo altera o indice da pilha de widgets para exibir a tela de atendimento na interface.
        """
        self.QtStack.setCurrentIndex(11)
    
    def abrirAddGuiche(self):
        """
        Abre a tela de adicionar guiche.

        Este metodo altera o indice do widget stack para exibir a tela de adicionar guiche na interface.
        """
        self.QtStack.setCurrentIndex(12)
    
    def abrirfinalizarAtendimento(self):  
        """
        Abre a tela de finalizar atendimento.

        Este metodo altera o indice do widget stack para exibir a tela de finalizar atendimento na interface.
        """
        self.QtStack.setCurrentIndex(13)
    
    def abrirativarGuiche(self):
        """
        Abre a tela de ativar guiche.

        Este metodo altera o indice do widget stack para exibir a tela de ativar guiche na interface.
        """
        self.QtStack.setCurrentIndex(14)
    
    def abrirdesativaGuiche(self):
        """
        Abre a tela de desativar guiche.

        Este metodo altera o indice do widget stack para exibir a tela de desativar guiche na interface.
        """
        self.QtStack.setCurrentIndex(15)

    def abrirImpressao(self):
        """
        Abre a tela de impressao.

        Este metodo altera o indice do widget stack para exibir a tela de impressao na interface.
        """
        self.QtStack.setCurrentIndex(16)

    def abrirImpRecep(self):
        """
        Abre a tela de impressao para recepcionista.

        Este metodo altera o indice do widget stack para exibir a tela de impressao para recepcionista na interface.
        """
        self.QtStack.setCurrentIndex(17)
    
    def abrirImpMed(self):
        """
        Abre a tela de impressao para medico.

        Este metodo altera o indice do widget stack para exibir a tela de impressao para medico na interface.
        """
        self.QtStack.setCurrentIndex(18)
    
    def abrirConsulta(self):
        """
        Abre a tela de consulta.

        Este metodo altera o indice do widget stack para exibir a tela de consulta na interface.
        """
        self.QtStack.setCurrentIndex(20)

    
    def abrirRealizarConsult(self):
        """
        Abre a tela de realizacao de consulta.

        Este metodo altera o indice do widget stack para exibir a tela de realizacao de consulta na interface.
        Alem disso, envia uma mensagem ao servidor solicitando os dados necessarios para preencher os campos da tela.
        Os dados recebidos do servidor sao utilizados para preencher o campo Recepcionista e a lista suspensa de Medico.
        """
        self.QtStack.setCurrentIndex(21)
        menssagem =  f'logrecp'
        cliente_socket.send(menssagem.encode())
        print('menssagem enviada')
        recebida = cliente_socket.recv(1024).decode().split(",")
        print('recebida:',recebida)
        self.realizar_consulta.lineEdit_10.setText(recebida[0])

        #self.realizar_consulta.comboBox.setCurrentText("Escolha uma Opção")
        if self.realizar_consulta.comboBox.findText("Escolha uma Opção") == -1:
            self.realizar_consulta.comboBox.insertItem(0, "Escolha uma Opção")
            self.realizar_consulta.comboBox.setItemText(0, "Escolha uma Opção")
            self.realizar_consulta.comboBox.setItemData(0, QtGui.QColor(QtCore.Qt.gray), QtCore.Qt.TextColorRole)  # Opcional: Definir cor cinza para o texto informativo
            for dado in recebida[1:]:
                if self.realizar_consulta.comboBox.findText(dado) == -1:
                    self.realizar_consulta.comboBox.addItem(dado)  
            self.realizar_consulta.comboBox.currentIndexChanged.connect(self.realizarConsultaAA) 

    def realizarConsultaAA(self):
        """
        Realiza uma consulta ao selecionar um medico na lista suspensa.

        Este metodo e acionado quando uma opcao de medico e selecionada na lista suspensa da tela de realizacao de consulta.
        Ele envia uma mensagem ao servidor solicitando os dados relacionados ao medico selecionado.
        Os dados recebidos do servidor sao utilizados para preencher os campos "CRM" e "CPF do Medico" na interface.
        """
        medico = self.realizar_consulta.comboBox.currentText()
        if self.realizar_consulta.comboBox.currentIndex() == 0:
             QtWidgets.QMessageBox.warning(None, "interface_grafica", "Selecione um medico para concluir o cadastro da consulta")
        else:
            print("Opção selecionada:", medico)
            menssagem =  f'rconsult,{medico}'
            cliente_socket.send(menssagem.encode())
            print('menssagem enviada')
            recebida = cliente_socket.recv(1024).decode().split(",")
            print('recebida:',recebida)
            if recebida[0] == '1':
                crm = self.realizar_consulta.lineEdit_6.setText(recebida[2])
                cpf_medico = self.realizar_consulta.lineEdit_9.setText(recebida[1])


    def abrirExcluirConsult(self):
        """
        Abre a tela de exclusao de consulta.

        Este metodo altera o indice do widget stack para exibir a tela de exclusao de consulta na interface.
        """
        self.QtStack.setCurrentIndex(22)
        
    def abrirTipoConsult(self):
        """
        Abre a tela de verificacao do tipo de consulta.

        Este metodo altera o indice do widget stack para exibir a tela de verificacao do tipo de consulta na interface.
        """
        self.QtStack.setCurrentIndex(23)

    def abrirImpPac(self):
        """
        Abre a tela de impressao de informacoes do paciente.

        Este metodo altera o indice do widget stack para exibir a tela de impressao de informacoes do paciente na interface.
        """
        self.QtStack.setCurrentIndex(24)

    def abrirExcluirPac(self):
        """
        Abre a tela de exclusao de paciente.

        Este metodo altera o indice do widget stack para exibir a tela de exclusao de paciente na interface.
        """
        self.QtStack.setCurrentIndex(25)

    def abrirExcluirGuiche(self):
        """
        Abre a tela de exclusao de guiche.

        Este metodo altera o indice do widget stack para exibir a tela de exclusao de guiche na interface.
        """
        self.QtStack.setCurrentIndex(26)
    
    def abrirAtualizarCons(self):
        """
        Abre a tela de atualizacao de consulta.

        Este metodo altera o indice do widget stack para exibir a tela de atualizacao de consulta na interface.
        """
        self.QtStack.setCurrentIndex(27)

    def abrirListaPaciente(self):
        """
        Abre a tela de lista de pacientes.

        Este metodo altera o indice do widget stack para exibir a tela de lista de pacientes na interface.
        Limpa a lista de pacientes existente e solicita ao servidor a lista atualizada de pacientes.
        Os pacientes recebidos sao adicionados a lista de pacientes da interface.
        """
        self.QtStack.setCurrentIndex(28)
        self.lista_pacientes.listWidget.clear()
        menssagem =  f'listapacientes'
        cliente_socket.send(menssagem.encode())
        print('menssagem enviada')
        recebida = cliente_socket.recv(1024).decode().split("\n")    
        for item in recebida:
            self.lista_pacientes.listWidget.addItem(str(item))
        
    def abrirLoginAdmin(self):
        """
        Abre a tela de login do administrador.

        Este metodo altera o indice do widget stack para exibir a tela de login do administrador na interface.
        """
        self.QtStack.setCurrentIndex(29)

    def sair(self): 
        """
        Fecha a aplicacao e encerra a conexao com o servidor.

        Este metodo envia uma mensagem ao servidor indicando o encerramento da aplicacao.
        Em seguida, fecha a conexao com o servidor e finaliza a execucao do programa.
        """
        menssagem =  f'sair'
        cliente_socket.send(menssagem.encode())
        print('menssagem enviada')
        if menssagem == 'sair':
            cliente_socket.close()
            print('Conexão com o cliente FECHADA')
            return exit()

    def voltarLogin(self):
        """
        Volta para a tela de login.

        Este metodo altera o indice do widget stack para exibir a tela de login na interface.
        """
        self.QtStack.setCurrentIndex(0)

    def voltarLoginMedico(self):
        """
        Volta para a tela de login do medico.

        Este metodo altera o indice do widget stack para exibir a tela de login do medico na interface.
        """
        self.QtStack.setCurrentIndex(1)

    def voltarLoginRecep(self):
        """
        Volta para a tela de login do recepcionista.

        Este metodo altera o indice do widget stack para exibir a tela de login do recepcionista na interface.
        """
        self.QtStack.setCurrentIndex(2)
    
    def voltarCadastros(self):
        """
        Volta para a tela de cadastros.

        Este metodo altera o indice do widget stack para exibir a tela de cadastros na interface.
        """
        self.QtStack.setCurrentIndex(7)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
