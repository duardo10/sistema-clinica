import threading
import socket
from banco_Dado import BancoDeDados
   
class Usuario(threading.Thread):
    """
    A classe Usuario representa um usuario do sistema

    A classe Usuario e responsavel por fazer as consultas, insercoes, atualizacoes e delecoes no banco de dados do sistema

    Attributes
    ---------
    conec : socket.socket
        O objeto de conexão do cliente.
    adress : tuple
        A tupla que contem o endereço IP e a porta do cliente.
    banco : banco_Dado.BancoDeDados
        O objeto que representa o banco de dados do sistema.
    lock : _thread.Lock
        O objeto lock para sincronizacao de threads.

    Methods
    ------
    run()
        O metodo principal que define o comportamento do usuario quando a thread e iniciada, e processa as solicitacoes
        do cliente chamando as funcoes adequadas para cada necessidade

    """
    def __init__(self,addr,con_cliente):
        threading.Thread.__init__(self)
        self.conec = con_cliente
        self.adress = addr
        self.banco = BancoDeDados()
        self.lock = threading.Lock()
        print(type(con_cliente))
        """
        Parameters
        ----------
        addr : tuple
            A tupla que contem o endereco IP e a porta do cliente.
        con_cliente : socket.socket
            O objeto de conexao do cliente.

        """

    def run(self):
        """
        O metodo principal que define o comportamento do usuario quando a thread e iniciada.

        Esse metodo e executado quando a thread do usuario e iniciada. Ele define o comportamento do usuario, recebe solicitacoes do cliente, processa as solicitacoes e responde ao cliente.

        """
        while (True): 
            memnssagem_cliente = self.conec.recv(1024).decode()
            dados = memnssagem_cliente.split(",")
            if len(dados) >= 1:
                acao = dados[0]
                if acao.lower() == 'admin':
                    self.loginAdmin(dados[1],dados[2])
                elif acao.lower() == 'medico':
                    self.loginMedico(dados[1],dados[2])
                elif acao.lower() == 'recepcionista':
                    self.loginRecep(dados[1],dados[2])
                elif acao.lower() == 'cad_medicologin':
                    self.cadastroMedicoLogin(dados[1],dados[2],dados[3],dados[4],dados[5],dados[6],dados[7],dados[8],dados[9])
                elif acao.lower() == 'cad_medico':
                    self.cadastroMedico(dados[1],dados[2],dados[3],dados[4],dados[5],dados[6],dados[7],dados[8],dados[9])
                elif acao.lower() == 'cad_receplogin':
                    self.cadastroRecepLogin(dados[1],dados[2],dados[3],dados[4],dados[5],dados[6])
                elif acao.lower() == 'cad_recep':
                    self.cadastroRecep(dados[1],dados[2],dados[3],dados[4],dados[5],dados[6])
                elif acao.lower() == 'cad_admin':
                    self.cadastroAdmin(dados[1],dados[2],dados[3])
                elif acao.lower() == 'atendimento':
                    self.iniciarAtendimento()
                elif acao.lower() == 'finalizar_atendimento':
                    self.FinalizarAtendimento()
                elif acao.lower() == 'adicionaguiche':
                    self.addGuiche(dados[1],dados[2],dados[3])
                elif acao.lower() == 'excluiguiche':
                    self.excluirGuiche()
                elif acao.lower() == 'ativarguiche':
                    self.ativarGuiche()
                elif acao.lower() == 'desativarguiche':
                    self.desativarGuiche()
                elif acao.lower() == 'imprecep':
                    self.imprimirRecep(dados[1])
                elif acao.lower() == 'impmedico':
                    self.imprimirMedico(dados[1])
                elif acao.lower() == 'realizarconsult':
                    self.realizarConsulta(dados[1],dados[2],dados[3],dados[4],dados[5],dados[6],dados[7],dados[8],dados[9])
                elif acao.lower() == 'enviarconsult':
                    self.enviarConsulta() 
                elif acao.lower() == 'busconsult':
                    self.buscConsult(dados[1])  
                elif acao.lower() == 'excluirconsult':
                    self.excluirConsult(dados[1])
                elif acao.lower() == 'verificartipo':
                    self.verificarTipo(dados[1])
                elif acao.lower() == 'enviarcon':
                    self.enviarCons(dados[1]) 
                elif acao.lower() == 'bconsult':
                    self.buscCons(dados[1])
                elif acao.lower() == 'atualizaconsult':
                    self.atualizarConsult(dados[1])
                elif acao.lower() == 'listapacientes':
                    self.listaPacientes()
                elif acao.lower() == 'excluipaciente':
                    self.excluiPacientes()        
                elif acao.lower() == 'logrecp':
                    self.realCons()
                elif acao.lower() == 'rconsult':
                    self.realizarConsultaAA(dados[1])
                elif acao.lower() == 'sair':
                    self.fecharConexao()
                    break
                

    def loginAdmin(self,cpf,password):
        """
        Realiza o login de um usuario como administrador

        O metodo verifica se as credenciais correspondem a um administrador registrado

        Parameters
        ----------
        cpf : str
            O CPF do usuario
        password : str
            A senha do usuario.

        Raises
        ------
        Exception
            Se ocorrer um erro durante o login, uma excecao e lançada.

        Returns
        -------
        None
            O resultado do login e enviado de volta ao cliente atraves do socket.
        """
        try:
            result = self.banco.fazerLoginAdmin(cpf, password)
            if result:
                enviar = '1'
                self.conec.send(enviar.encode())
            else:
                enviar = '0'
                self.conec.send(enviar.encode())
        except:
            print('Erro do servidor durante o login')
    
    def loginMedico(self,cpf,password):
        """
        Realiza o login de um usuario como medico

        O metodo verifica se as credenciais correspondem a um medico registrado

        Parameters
        ----------
        cpf : str
            O CPF do usuario
        password : str
            A senha do usuario.

        Raises
        ------
        Exception
            Se ocorrer um erro durante o login, uma excecao e lançada.

        Returns
        -------
        None
            O resultado do login e enviado de volta ao cliente atraves do socket.
        """
        try:
            result = self.banco.fazerLoginMed(cpf, password)
            print('login', result)
            if result:
                enviar = '1'
                self.conec.send(enviar.encode())
            else:
                enviar = '0'
                self.conec.send(enviar.encode())
        except:
            print('Erro do servidor durante o login')
    
    def loginRecep(self,cpf,password):
        """
        Realiza o login de um usuario como recepcionista

        O metodo verifica se as credenciais correspondem a um recepcionista registrado

        Parameters
        ----------
        cpf : str
            O CPF do usuario
        password : str
            A senha do usuario

        Raises
        ------
        Exception
            Se ocorrer um erro durante o login, uma excecao e lancada

        Returns
        -------
        None
            O resultado do login e enviado de volta ao cliente atraves do socket
        """
        try:
            result = self.banco.fazerLoginRecep(cpf, password)
            if result:
                enviar = '1'
                self.conec.send(enviar.encode())
            else:
                enviar = '0'
                self.conec.send(enviar.encode())
        except:
            print('Erro do servidor durante o login')
    
    def cadastroMedicoLogin(self,cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,senha):
        """
        Realiza o cadastro de um medico 

        O metodo realiza o cadastro de um medico. O resultado desse cadastro e enviado de volta ao cliente pelo socket

        Parameters
        ----------
        cpf : str
            O CPF do medico
        nome : str
            O nome do medico
        telefone : str
            O telefone do medico
        dt_nasc : str
            A data de nascimento do medico
        email : str
            O email do medico
        especialidade : str
            A especialidade do medico
        hr_atendimento : str
            O horario de atendimento do medico
        crm : int
            O CRM do medico
        senha : str
            A senha do medico
        
        Raises
        ------
        Exception
            Se ocorrer um erro durante o cadastro do medico, uma excecao e lancada

        Returns
        -------
        None
            O resultado do cadastro e enviado de volta ao cliente atraves do socket
        """
        self.lock.acquire()
        try:
            result = self.banco.cadastroMedico(cpf)
            if result:
                inserir = self.banco.inserirMedico(cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,senha)
                if inserir == True:
                    enviar = '1'
                    self.conec.send(enviar.encode())
                else:
                    enviar = '3'
                    self.conec.send(enviar.encode())
            else:
                enviar = '0'
                self.conec.send(enviar.encode())
        except:
            print('Erro do servidor durante o login do medico')
        finally:
            # Libera o acesso à seção crítica
            self.lock.release()
    
    def cadastroMedico(self,cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,senha):
        """
        Realiza um cadastro de um medico

        O metodo realiza o cadastro de um medico. O resultado desse cadastro e enviado de volta ao cliente pelo socket

        Parameters
        ----------
        cpf : str
            O CPF do medico
        nome : str
            O nome do medico
        telefone : str
            O telefone do medico
        dt_nasc : str
            A data de nascimento do medico
        email : str
            O email do medico
        especialidade : str
            A especialidade do medico
        hr_atendimento : str
            O horario de atendimento do medico
        crm : int
            O CRM do medico
        senha : str
            A senha do medico
        
        Raises
        ------
        Exception
            Se ocorrer um erro durante o cadastro do medico, uma excecao e lancada

        Returns
        -------
        None
            O resultado do cadastro e enviado de volta ao cliente atraves do socket
        """
        self.lock.acquire()
        try:
            result = self.banco.cadastroMedico(cpf)
            if result:
                inserir = self.banco.inserirMedico(cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,senha)
                if inserir == True:
                    enviar = '1'
                    self.conec.send(enviar.encode())
                else:
                    enviar = '3'
                    self.conec.send(enviar.encode())
            else:
                enviar = '0'
                self.conec.send(enviar.encode())
        except:
            print('Erro do servidor durante o cadastro do medico')
        finally:
            # Libera o acesso à seção crítica
            self.lock.release()
    
    def cadastroRecepLogin(self,cpf,nome,telefone,dt_nasc,email,senha):
        """
        Realiza um cadastro de um recepcionista

        O metodo realiza o cadastro de um recepcionista. O resultado desse cadastro e enviado de volta ao cliente atraves do socket.

        Parameters
        ----------
        cpf : str
            O CPF do recepcionista
        nome : str
            O nome do recepcionista
        telefone : str
            O telefone do recepcionista
        dt_nasc : str
            A data de nascimento do recepcionista
        email : str
            O email do recepcionista
        senha : str
            A senha do recepcionista
         
        Raises
        ------
        Exception
            Se ocorrer um erro durante o cadastro do medico, uma excecao e lancada

        Returns
        -------
        None
            O resultado do cadastro e enviado de volta ao cliente atraves do socket
        """
        self.lock.acquire()
        try:
            result = self.banco.cadastroRecep(cpf)
            if result:
                inserir = self.banco.inserirRecep(cpf,nome,telefone,dt_nasc,email,senha)
                if inserir == True:
                    enviar = '1'
                    self.conec.send(enviar.encode())
                else:
                    enviar = '3'
                    self.conec.send(enviar.encode())
            else:
                enviar = '0'
                self.conec.send(enviar.encode())
        except:
            print('Erro do servidor durante o cadastro do medico')
        finally:
            # Libera o acesso à seção crítica
            self.lock.release()
    
    def cadastroRecep(self,cpf,nome,telefone,dt_nasc,email,senha):
        """
        Realiza um cadastro de um recepcionista

        O metodo realiza o cadastro de um recepcionista. O resultado desse cadastro e enviado de volta ao cliente atraves do socket.

        Parameters
        ----------
        cpf : str
            O CPF do recepcionista
        nome : str
            O nome do recepcionista
        telefone : str
            O telefone do recepcionista
        dt_nasc : str
            A data de nascimento do recepcionista
        email : str
            O email do recepcionista
        senha : str
            A senha do recepcionista
         
        Raises
        ------
        Exception
            Se ocorrer um erro durante o cadastro do medico, uma excecao e lancada

        Returns
        -------
        None
            O resultado do cadastro e enviado de volta ao cliente atraves do socket
        """
        self.lock.acquire()
        try:
            result = self.banco.cadastroRecep(cpf)
            if result:
                inserir = self.banco.inserirRecep(cpf,nome,telefone,dt_nasc,email,senha)
                if inserir == True:
                    enviar = '1'
                    self.conec.send(enviar.encode())
                else:
                    enviar = '3'
                    self.conec.send(enviar.encode())
            else:
                enviar = '0'
                self.conec.send(enviar.encode())
        except:
            print('Erro do servidor durante o cadastro do medico')
        finally:
            # Libera o acesso à seção crítica
            self.lock.release()

    def cadastroAdmin(self,cpf_admin, nome, senha):
        """
        Realiza um cadastro de um administrador

        O metodo realiza o cadastro de um administrador. O resultado desse cadastro e enviado de volta ao cliente atraves do socket.

        Parameters
        ----------
        cpf_admin : str
            O CPF do administrador
        nome : str
            O nome do administrador
        senha : str
            A senha do administrador
         
        Raises
        ------
        Exception
            Se ocorrer um erro durante o cadastro do medico, uma excecao e lancada

        Returns
        -------
        None
            O resultado do cadastro e enviado de volta ao cliente atraves do socket
        """
        self.lock.acquire()
        try:
            result = self.banco.cadastroAdmin(cpf_admin)
            if result:
                inserir = self.banco.inserirAdmin(cpf_admin, nome, senha)
                if inserir == True:
                    enviar = '1'
                    self.conec.send(enviar.encode())
                else:
                    enviar = '3'
                    self.conec.send(enviar.encode())
            else:
                enviar = '0'
                self.conec.send(enviar.encode())
        except:
            print('Erro do servidor durante o cadastro do medico')
        finally:
            # Libera o acesso à seção crítica
            self.lock.release()

    def iniciarAtendimento(self):
        """
        Inicia o atendimento no guiche

        O metodo inicia o atendimento no guiche. O resultado desse inicio de atendimento e enviado de volta ao cliente atraves do socket.
         
        Raises
        ------
        Exception
            Se ocorrer um erro durante o inicio de um atendimento, uma excecao e lancada

        Returns
        -------
        None
            O resultado do inicio do atendimento e enviado de volta ao cliente atraves do socket
        """
        self.lock.acquire()
        result = self.banco.iniciar_atendimento()
        print('resultado',result)
        if result == None:
            enviar = '0'
            self.conec.send(enviar.encode())
        elif result == False:
            enviar = '3' 
            self.conec.send(enviar.encode())
        elif result == True:
            enviar = '2'
            self.conec.send(enviar.encode())
        else:
            enviar = f'{result}'
            self.conec.send(enviar.encode())

        self.lock.release()
           
    def FinalizarAtendimento(self):
        """
        Finaliza o atendimento no guiche

        O metodo finaliza o atendimento no guiche. O resultado desse finalizacao de atendimento e enviado de volta ao cliente atraves do socket.
         
        Raises
        ------
        Exception
            Se ocorrer um erro durante o finalizamento de um atendimento, uma excecao e lancada

        Returns
        -------
        None
            O resultado da finalizacao do atendimento e enviado de volta ao cliente atraves do socket
        """
        self.lock.acquire()
        try:
            result = self.banco.finalizar_atendimento()
            if result == None:
                enviar = '3'
                self.conec.send(enviar.encode())
            if result == False:
                enviar = '0'
                self.conec.send(enviar.encode())
            elif result == True:
                enviar = '2'
                self.conec.send(enviar.encode())
            else:
                enviar = f'{result}'
                self.conec.send(enviar.encode())
        except:
            print('Erro do servidor durante o cadastro do medico')
        finally:
            # Libera o acesso a secao critica
            self.lock.release()
    
    def addGuiche(self,status,senha,modo):
        """
        Adiciona um guiche ao sistema

        O metodo adiciona um guiche ao sistema. O resultado desse cadastro de guiche e enviado de volta ao cliente atraves do socket.

        Parameters
        ----------
        status : str
            O status do guiche
        senha : str
            A senha do guiche
        modo : str
            O modo do guiche
        
        Raises
        ------
        Exception
            Se ocorrer um erro durante o cadastro de um guiche, uma excecao e lancada

        Returns
        -------
        None
            O resultado do cadastro do guiche e enviado de volta ao cliente atraves do socket
        """
        self.lock.acquire()
        try:
            selecionar = self.banco.buscRecep()
            if selecionar != True:
                enviar = '0'
                self.conec.send(enviar.encode())
            else:
                inserir = self.banco.inserirGuiche(status,senha,modo)
                if inserir == True:
                    enviar = '1'
                    self.conec.send(enviar.encode())
                else:
                    enviar = '2'
                    self.conec.send(enviar.encode())
        except:
            print('Erro do servidor durante o cadastro do guiche')
        finally:
            # Libera o acesso à seção crítica
            self.lock.release()
    
    def excluirGuiche(self):
        """
        Exclui o guiche do sistema

        Exclui o guiche atualmente selecionado, removendo-o do sistema. O resultado da exclusao e enviado de volta ao cliente pelo socket

        Raises
        ------
        Exception
            Se ocorrer um erro durante a exclusao de um guiche, uma excecao e lancada

        Returns
        -------
        None
            O resultado da exclusao do guiche e enviado de volta ao cliente atraves do socket
        """
        self.lock.acquire()
        try:
            selecionar = self.banco.buscGuicheRecep()
            if selecionar is not None:
                result = self.banco.excluir_guiche(selecionar[0])
                if result == True:
                    enviar = '1'
                    self.conec.send(enviar.encode())
                elif result == False:
                    enviar = '0'
                    self.conec.send(enviar.encode())
                else:
                    enviar = '2'
                    self.conec.send(enviar.encode())
            else:
                enviar = '3'
                self.conec.send(enviar.encode())

        except:
            print('Erro do servidor durante o cadastro do medico')
        finally:
            # Libera o acesso à seção crítica
            self.lock.release()

    def ativarGuiche(self):
        """
        Ativa o guiche no sistema

        Ativa o guiche atualmente inativo, atualizando seu status para ativo. O resultado da ativacao e enviado de volta ao cliente pelo socket

        Raises
        ------
        Exception
            Se ocorrer um erro durante a ativacao de um guiche, uma excecao e lancada

        Returns
        -------
        None
            O resultado da ativacao do guiche e enviado de volta ao cliente atraves do socket
        """
        self.lock.acquire()
        try:
            resultado = self.banco.buscGuicheRecep()
            if resultado is not None:
                result = self.banco.ativarGuiche(resultado[0])
                if result == True:
                    atualizar = self.banco.atualizarModo(resultado[0])
                    if atualizar == True:
                        enviar = '1'
                        self.conec.send(enviar.encode())
                    else:
                        print('erro no banco de dados')
                elif result == False:
                    enviar = '0'
                    self.conec.send(enviar.encode())
                elif result == None:
                    enviar = '2'
                    self.conec.send(enviar.encode())
            else:
                enviar = '3'
                self.conec.send(enviar.encode())

        except:
            print('Erro do servidor durante o ativar guiche')
        finally:
            # Libera o acesso à seção crítica
            self.lock.release()

    def desativarGuiche(self):
        """
        Desativa o guiche no sistema

        Desativa o guiche, atualizando seu status para inativo. O resultado da desativacao e enviado de volta ao cliente pelo socket.

        Raises
        ------
        Exception
            Se ocorrer um erro durante a desativacao de um guiche, uma excecao e lancada

        Returns
        -------
        None
            O resultado da desativacao do guiche e enviado de volta ao cliente atraves do socket
        """
        self.lock.acquire()
        try:
            resultado = self.banco.buscGuicheRecep()
            if resultado is not None:
                result = self.banco.desativarGuiche(resultado[0])
                if result == True:
                    atualizar = self.banco.atualizarModoInativo(resultado[0])
                    if atualizar == True:
                        enviar = '1'
                        self.conec.send(enviar.encode())
                    else:
                        print('Erro do banco de dados')
                elif result == False:
                    enviar = '0'
                    self.conec.send(enviar.encode())
                elif result == None:
                    enviar = '2'
                    self.conec.send(enviar.encode())
            else:
                enviar = '3'
                self.conec.send(enviar.encode())
        except:
            print('Erro do servidor durante desativar guiche')
        finally:
            self.lock.release()

    def imprimirRecep(self,cpf):
        """
        Imprime os dados do recepcionista

        Este metodo recebe o CPF de um recepcionista e retorna os dados correspondentes ao recepcionista, que sao enviados de volta ao cliente atraves do socket

        Parameters
        ----------
        cpf : str
            O CPF do recepcionista
        
        Raises
        ------
        Exception
            Se ocorrer um erro durante a impressao de um recepcionista, uma excecao e lancada


        Returns
        -------
        None
            Os dados do recepcionista sao enviados de volta ao cliente atraves do socket.
        """
        try:
            pessoa = self.banco.buscarRecep(cpf)
            print('pessoa',pessoa)
            if (pessoa != None):
                imprimir = self.banco.imprimirRecep(pessoa)
                enviar = f'1,{imprimir[0]},{imprimir[1]},{imprimir[2]},{imprimir[3]},{imprimir[4]}'
                self.conec.send(enviar.encode())
            else:
                enviar = '0'
                self.conec.send(enviar.encode())
        except:
            print('Erro do servidor durante o cadastro do medico')
    
    def imprimirMedico(self, cpf):
        """
        Imprime os dados do medico

        Este metodo recebe o CPF de um medico e retorna os dados correspondentes ao medico, que sao enviados de volta ao cliente atraves do socket.

        Parameters
        ----------
        cpf : str 
            O CPF do medico
        
        Raises
        ------
        Exception
            Se ocorrer um erro durante a impressao de um medico, uma excecao e lancada

        Returns
        -------
        None 
            Os dados do medico sao enviados de volta ao cliente atraves do socket.
        """
        try:
            pessoa = self.banco.buscMed(cpf)
            if (pessoa != None):
                imprimir = self.banco.imprimirMed(pessoa)
                enviar = f'1,{imprimir[0]},{imprimir[1]},{imprimir[2]},{imprimir[3]},{imprimir[4]},{imprimir[5]},{imprimir[6]},{imprimir[7]}'
                self.conec.send(enviar.encode())
            else:
                enviar = '0'
                self.conec.send(enviar.encode())
        except:
            print('Erro do servidor durante o cadastro do medico')

    def realizarConsulta(self,cpf_paciente,nome_paciente,telefone,dt_nasc,medico,crm,tipo,cpf_medico,cpf_recepcionista):
        """
        Realiza uma consulta medica

        Este metodo realiza uma consulta medica, registrando os dados do paciente, medico e recepcionista envolvidos. O resultado da consulta e enviado de volta ao cliente atraves do socket

        Parameters
        ----------
        cpf_paciente : str
            O CPF do paciente
        nome_paciente : str 
            O nome do paciente
        telefone : str 
            O telefone do paciente
        dt_nasc : str
            A data de nascimento do paciente
        medico : str
            O nome do medico responsavel pela consulta
        crm : int
            O CRM do medico
        tipo : srt 
            O tipo de consulta
        cpf_medico : str
            O CPF do medico responsavel pela consulta
        cpf_recepcionista : str
            O CPF do recepcionista que registrou a consulta

        Returns
        -------
        None
            O resultado da consulta e enviado de volta ao cliente atraves do socket
        """
        self.lock.acquire()
        try:
            result = self.banco.verificaMedico(medico,crm,cpf_medico)
            resultado = self.banco.verificaRecep(cpf_recepcionista)
            if result == None and resultado == None:
                enviar = '3'
                self.conec.send(enviar.encode())
            elif result == None:
                enviar = '4'
                self.conec.send(enviar.encode())
            elif resultado == None:
                enviar = '5'
                self.conec.send(enviar.encode())
            else:
                inserir = self.banco.inserirConsulta(cpf_paciente,nome_paciente,telefone,dt_nasc,medico,crm,tipo,cpf_medico,cpf_recepcionista)
                if inserir == True:
                    enviar = '1'
                    self.conec.send(enviar.encode())
                else:
                    enviar = '2'
                    self.conec.send(enviar.encode())
        finally:
            self.lock.release()
    
    def realCons(self):
        """
        Busca o nome dos medicos

        O metodo seleciona todos os nomes dos medicos. O resultado da busca e enviado de volta ao cliente atraves do socket

        Raises
        ------
        Exception
            Se ocorrer um erro durante a busca dos medicos, uma excecao e lancada
        
        Returns
        -------
        None
            O resultado da busca e enviado de volta ao cliente atraves do socket.
        """
        try:
            dados = self.banco.nomeMed()
            enviar = f'{dados[0]},{dados[1]}'
            self.conec.send(enviar.encode())
        except:
            print('Erro do servidor na realizar consulta')
     
    def realizarConsultaAA(self, medico):
        try:
            listaMed = self.banco.realizarConsultaAA(medico)
            enviar = f'1,{listaMed[0][0]},{str(listaMed[0][1])}'
            self.conec.send(enviar.encode())
        except:
            print('Erro do servidor na realizar consulta')
    
    def enviarConsulta(self):
        """
        Envia uma consulta ao medico

        O metodo envia os dados de um paciente para um medico. O resultado dessa operacao e enviado de volta ao cliente atraves do socket

        Raises
        ------
        Exception
            Se ocorrer um erro durante o envio dos dados de um paciente, uma excecao e lancada
        
        Returns
        -------
        None 
            O resultado da operacao e enviado de volta ao cliente atraves do socket.
        """
        self.lock.acquire()
        try:
            result = self.banco.enviar_consulta()
            if result == False:
                enviar = '3'
                self.conec.send(enviar.encode())
            elif result == 2:
                enviar = '4'
                self.conec.send(enviar.encode())
            elif result == 3:
                enviar = '5'
                self.conec.send(enviar.encode())
            elif result == 5:
                enviar = '6'
                self.conec.send(enviar.encode())
            elif result == True:
                enviar = '1'
                self.conec.send(enviar.encode())
            elif result == 0:
                enviar = '0'
                self.conec.send(enviar.encode())
            else:
                enviar = result
                self.conec.send(enviar.encode())
        except:
            print('Erro do servidor durante o cadastro do medico')
        finally:
            self.lock.release()

    def buscConsult(self,cpf):
        """
        Busca os dados de uma consulta

        O metodo seleciona todos os dados de uma consulta. O resultado da busca e enviado de volta ao cliente atraves do socket

        Parameters
        ----------
        cpf : str 
            O CPF do paciente

        Raises
        ------
        Exception
            Se ocorrer um erro durante a busca dos dados, uma excecao e lancada
        
        Returns
        -------
        None 
            O resultado da busca dos dados e enviado de volta ao cliente atraves do socket.
        """
        pessoa = self.banco.buscConsulta(cpf)
        if (pessoa != None):
            buscar = self.banco.buscConsult(cpf)
            enviar = f'1,{buscar[0]},{buscar[1]},{buscar[2]},{buscar[3]},{buscar[4]},{buscar[5]},{buscar[6]},{buscar[7]}'
            self.conec.send(enviar.encode())
        else:
            enviar = '0'
            self.conec.send(enviar.encode())

    def excluirConsult(self,cpf):
        """
        Exclui uma consulta

        O metodo exclui uma consulta de um paciente. O resultado da exclusao e enviado de volta ao cliente pelo socket

        Raises
        ------
        Exception
            Se ocorrer um erro durante a exclusao de uma consulta, uma excecao e lancada

        Returns
        -------
        None
            O resultado da exclusao da consulta e enviado de volta ao cliente atraves do socket
        """
        self.lock.acquire()
        result = self.banco.excluir_consulta(cpf) 
        if result == True:
            enviar = '1'
            self.conec.send(enviar.encode())
        elif result == False:
            enviar = '0'
            self.conec.send(enviar.encode())
        elif result == None:
            enviar = '2'
            self.conec.send(enviar.encode())
        self.lock.release()

    
    def verificarTipo(self,cpf):
        """
        Verifica o tipo de uma consulta

        O metodo verifica o tipo de uma consulta de um paciente. O resultado da verificacao e enviado de volta ao cliente pelo socket

        Raises
        ------
        Exception
            Se ocorrer um erro durante a verificacao de uma consulta, uma excecao e lancada

        Returns
        -------
        None
            O resultado da verificacao da consulta e enviado de volta ao cliente atraves do socket
        """
        try:
            retorno = self.banco.verificar_tipo(cpf)
            if retorno == True:
                enviar = '1'
                self.conec.send(enviar.encode())
            elif retorno == False:
                enviar = '0'
                self.conec.send(enviar.encode())
            elif retorno == None:
                enviar = '3'
                self.conec.send(enviar.encode())     
        except:
            print('Erro do servidor durante o cadastro do medico')

    def enviarCons(self,cpf):
        """
        Envia uma consulta ao medico

        O metodo envia os dados de um paciente para um medico. O resultado dessa operacao e enviado de volta ao cliente atraves do socket

        Parameters
        ----------
        cpf : str 
            O CPF do paciente

        Raises
        ------
        Exception
            Se ocorrer um erro durante o envio dos dados de um paciente, uma excecao e lancada
        
        Returns
        -------
        None
            O resultado da operacao e enviado de volta ao cliente atraves do socket.
        """
        self.lock.acquire()
        try:
            result = self.banco.enviar_cons(cpf)
            if result == False:
                enviar = '3'
                self.conec.send(enviar.encode())
            elif result == 2:
                enviar = '4'
                self.conec.send(enviar.encode())
            elif result == 3:
                enviar = '5'
                self.conec.send(enviar.encode())
            elif result == 5:
                enviar = '6'
                self.conec.send(enviar.encode())
            elif result == True:
                enviar = '1'
                self.conec.send(enviar.encode())
            elif result == 0:
                enviar = '0'
                self.conec.send(enviar.encode())
            else:
                enviar = result
                self.conec.send(enviar.encode())
        except:
            print('Erro do servidor ao enviar a consulta')
        finally:
            self.lock.release()
    
    def buscCons(self,cpf):
        """
        Busca os dados dos pacientes

        O metodo seleciona todos os dados de um paciente. O resultado da busca e enviado de volta ao cliente atraves do socket

        Parameters
        ----------
        cpf : str 
            O CPF do paciente

        Raises
        ------
        Exception
            Se ocorrer um erro durante a busca dos dados, uma excecao e lancada
        
        Returns
        -------
        None
            O resultado da busca dos dados e enviado de volta ao cliente atraves do socket.
        """
        try:
            pessoa = self.banco.buscarPacientes(cpf)
            if (pessoa != None): 
                buscar = self.banco.buscPacientes(pessoa)             
                enviar = f'1,{buscar[0]},{buscar[1]},{buscar[2]},{buscar[3]},{buscar[4]},{buscar[5]},{buscar[6]},{buscar[7]}'
                self.conec.send(enviar.encode())
            else:
                enviar = '0'
                self.conec.send(enviar.encode())
        except:
            print('Erro do servidor durante o cadastro do medico')

    def atualizarConsult(self, cpf):
        """
        Atualiza uma consulta

        O metodo atualiza o tipo da consulta de um paciente. O resultado da atualizacao e enviado de volta ao cliente atraves do socket

        Parameters
        ----------
        cpf : str 
            O CPF do paciente

        Raises
        ------
        Exception
            Se ocorrer um erro durante a atualizacao, uma excecao e lancada
        
        Returns
        -------
        None 
            O resultado da atualizacao e enviado de volta ao cliente atraves do socket.
        """
        self.lock.acquire()
        try:
            result = self.banco.atualizaConsulta(cpf)
            if result == True:
                enviar = '1'
                self.conec.send(enviar.encode())
            elif result == False:
                enviar = '0'
                self.conec.send(enviar.encode())
            elif result == None:
                enviar = '2'
                self.conec.send(enviar.encode())
        except:
            print('Erro do servidor durante o cadastro do medico')
        finally:
            self.lock.release()

    def listaPacientes(self):
        """
        Lista os pacientes

        O metodo lista os pacientes de um medico. O resultado da listagem e enviado de volta ao cliente atraves do socket

        Raises
        ------
        Exception
            Se ocorrer um erro durante a listagem, uma excecao e lancada
        
        Returns
        -------
        None 
            O resultado da listagem e enviado de volta ao cliente atraves do socket.
        """
        try:
            lista = self.banco.listaPacientes()
            if len(lista) != 0:
                dados = ''
                for item in lista:
                    cpf, nome = item
                    dados += f'CPF: {cpf}, Nome: {nome}\n'
                self.conec.send(dados.encode())
            else:
                enviar = 'Sem pacientes'
                self.conec.send(enviar.encode())
        except:
            print('Erro do servidor')
    
    def excluiPacientes(self):
        """
        Exclui os pacientes

        O metodo exclui os pacientes de um medico. O resultado da exclusao e enviado de volta ao cliente atraves do socket

        Raises
        ------
        Exception
            Se ocorrer um erro durante a exclusao, uma excecao e lancada
        
        Returns
        -------
        None 
            O resultado da exclusao e enviado de volta ao cliente atraves do socket.
        """
        self.lock.acquire()
        try:
            resultado = self.banco.excluiPaci() 
            if resultado is not None:
                excluido = self.banco.deletarPaci(resultado[0])
                if excluido == True:
                    enviar = '1'
                    self.conec.send(enviar.encode())
                else:
                    enviar = '2'
                    self.conec.send(enviar.encode())
            else:
                enviar = '0'
                self.conec.send(enviar.encode())
                    
        except:
            print('Erro do servidor ')
        finally:
            self.lock.release()

    def fecharConexao(self):
        """
        Fecha a conexao de um cliente

        """
        self.conec.close()     
        print(f'Conexão {self.conec} ENCERRADA')
    

if __name__ == '__main__':
    host = '10.180.44.224'
    port = 8020
    addr = ((host, port))
    serv_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv_socket.bind(addr)
    while True:
        serv_socket.listen(10)
        print("Aguardando conexão...")
        conexao_servidor, cliente = serv_socket.accept()
        newthread = Usuario(cliente, conexao_servidor)
        newthread.start()
        print("Conectado")