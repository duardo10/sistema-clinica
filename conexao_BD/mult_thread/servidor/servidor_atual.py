import threading
import socket
from banco_Dado import BancoDeDados
   
class usuario(threading.Thread):
    def __init__(self,addr,con_cliente):
        threading.Thread.__init__(self)
        self.conec = con_cliente
        self.adress = addr
        self.banco = BancoDeDados()
        self.lock = threading.Lock()

    def run(self):
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
            # Libera o acesso à seção crítica
            self.lock.release()
    
    def addGuiche(self,status,senha,modo):
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
            print('Erro do servidor durante o cadastro do medico')
        finally:
            # Libera o acesso à seção crítica
            self.lock.release()
    
    def excluirGuiche(self):
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
        pessoa = self.banco.buscConsulta(cpf)
        if (pessoa != None):
            buscar = self.banco.buscConsult(cpf)
            enviar = f'1,{buscar[0]},{buscar[1]},{buscar[2]},{buscar[3]},{buscar[4]},{buscar[5]},{buscar[6]},{buscar[7]}'
            self.conec.send(enviar.encode())
        else:
            enviar = '0'
            self.conec.send(enviar.encode())

    def excluirConsult(self,cpf):
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
            print('Erro do servidor durante o cadastro do medico')
        finally:
            self.lock.release()
    
    def buscCons(self,cpf):
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
        self.conec.close()     
        print(f'Conexão {self.conec} ENCERRADA')
    

if __name__ == '__main__':
    host = '10.0.0.111'
    port = 8020
    addr = ((host, port))
    serv_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv_socket.bind(addr)
    while True:
        serv_socket.listen(10)
        print("Aguardando conexão...")
        conexao_servidor, cliente = serv_socket.accept()
        newthread = usuario(cliente, conexao_servidor)
        newthread.start()
        print("Conectado")