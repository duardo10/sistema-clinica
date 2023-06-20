#importação das classes
from cadastro import Cadastro
from pessoa import Pessoa
from paciente import Paciente
from recepcionista import Recepcionista
from login import Login
from medico import Medico
from funcionario import Funcionario
from admin import Admin
from atendimento import Guiche
from consulta import Consulta
from medico_BDmysql import MedicoFunc
from impressao import Imprimir

import socket
host = 'localhost'
port = 8006
addr = (host, port)

serv_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serv_socket.bind(addr)
serv_socket.listen(10)
print("Aguardando conexão...")
conexao_servidor, cliente = serv_socket.accept()
print("Conectado")


#importação do banco de dados
import mysql.connector

# configurações da conexão com o banco de dados 
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'clinica',
    'raise_on_warnings': True
}

login_atual = ''
senha_atual = ''
login_atual_Recep = ''
senha_atual_Recep = ''

try:
    # conectar com o banco de dados
    conexao = mysql.connector.connect(**config)
    print('Conexão realizada com sucesso!')

    # criando cursor para executar consultas
    cursor = conexao.cursor()


    class BancoDeDados:
        def __init__(self):
            # configurações da conexão com o banco de dados 
            self.connection = mysql.connector.connect(
                user = 'root',
                password = '',
                host = 'localhost',
                database = 'mydb',
        )
            self.cad = Cadastro()
            self.log = Login()
            self.gui = Guiche()
            self.imp = Imprimir()
            self.consult = Consulta()
            self.med = MedicoFunc()
            
        def processarDados(self, recebe):
            self.connection.commit()
            dados = recebe.decode().split(",")
            if len(dados) >= 1:
                acao = dados[0]
                if acao.lower() == 'admin':
                    self.loginAdmin(dados[1],dados[2])
                elif acao.lower() == 'medico':
                    self.loginMedico(dados[1],dados[2])
                elif acao.lower() == 'recepcionista':
                    self.loginMedico(dados[1],dados[2])
                elif acao.lower() == 'cad_medicologin':
                    self.cadastroMedicoLogin(dados[1],dados[2],dados[3],dados[4],dados[5],dados[6],dados[7],dados[8],dados[9])
                elif acao.lower() == 'cad_medico':
                    self.cadastroMedico(dados[1],dados[2],dados[3],dados[4],dados[5],dados[6],dados[7],dados[8],dados[9])
                elif acao.lower() == 'cad_receplogin':
                    self.cadastroRecepLogin(dados[1],dados[2],dados[3],dados[4],dados[5],dados[6])
                elif acao.lower() == 'cad_recep':
                    self.cadastroRecep(dados[1],dados[2],dados[3],dados[4],dados[5],dados[6])

        def loginAdmin(self,cpf,password):
            try:
                result = self.log.fazerLoginAdmin(cpf, password)
                print(result)
                conexao.commit()
                if self.log.fazerLoginAdmin(cpf,password):
                    # abre a tela de médico
                    enviar = '1'
                    conexao_servidor.send(enviar.encode())
                else:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
            except:
                print('Erro do servidor durante o login')
                serv_socket.close()
        
        def loginMedico(self,cpf,password):
            try:
                result = self.log.fazerLoginMed(cpf, password)
                print(result)
                conexao.commit()
                if self.log.fazerLoginMed(cpf,password):
                    global login_atual 
                    login_atual= cpf
                    global senha_atual
                    senha_atual = password
                    enviar = '1'
                    conexao_servidor.send(enviar.encode())
                else:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
            except:
                print('Erro do servidor durante o login')
                serv_socket.close()
        
        def loginRecep(self,cpf,password):
            try:
                result = self.log.fazerLoginRecep(cpf, password)
                print(result)
                conexao.commit()
                if self.log.fazerLoginRecep(cpf,password):
                    global login_atual_Recep
                    login_atual_Recep = cpf
                    global senha_atual_Recep
                    senha_atual_Recep = password
                    enviar = '1'
                    conexao_servidor.send(enviar.encode())
                else:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
            except:
                print('Erro do servidor durante o login')
                serv_socket.close()
        
        def cadastroMedicoLogin(self,cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,senha):
            try:
                result = self.cad.cadastroMedico(cpf)
                #print(retorno)
                print(result)
                if self.cad.cadastroMedico(cpf):
                    # utilizando comandos SQL para realizar as inserções no banco de dados
                    query = "INSERT INTO medico(cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,senha) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    values = (cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,senha)
                    try:
                        # utilizando o cursor para executar a inserção no banco de dados
                        cursor.execute(query, values)
                        #confirmar a inserção
                        conexao.commit()
                        enviar = '1'
                        conexao_servidor.send(enviar.encode())
                    except mysql.connector.errors.IntegrityError:
                        enviar = '3'
                        conexao_servidor.send(enviar.encode())
                else:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()

        def cadastroMedico(self,cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,senha):
            try:
                result = self.cad.cadastroMedico(cpf)
                #print(retorno)
                print(result)
                if self.cad.cadastroMedico(cpf):
                    # utilizando comandos SQL para realizar as inserções no banco de dados
                    query = "INSERT INTO medico(cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,senha) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    values = (cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,senha)
                    try:
                        # utilizando o cursor para executar a inserção no banco de dados
                        cursor.execute(query, values)
                        #confirmar a inserção
                        conexao.commit()
                        enviar = '1'
                        conexao_servidor.send(enviar.encode())
                    except mysql.connector.errors.IntegrityError:
                        enviar = '3'
                        conexao_servidor.send(enviar.encode())
                else:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()
        
        def cadastroRecepLogin(self,cpf,nome,telefone,dt_nasc,email,senha):
            try:
                result = self.cad.cadastroRecep(cpf)
                #print(retorno)
                print(result)
                if self.cad.cadastroRecep(cpf):
                    # utilizando comandos SQL para realizar as inserções no banco de dados
                    query = "INSERT INTO recepcionista(cpf,nome,telefone,dt_nasc,email,senha) VALUES(%s,%s,%s,%s,%s,%s)"
                    values = (cpf,nome,telefone,dt_nasc,email,senha)
                    try:
                        # utilizando o cursor para executar a inserção no banco de dados
                        cursor.execute(query, values)
                        #confirmar a inserção
                        conexao.commit()
                        enviar = '1'
                        conexao_servidor.send(enviar.encode())
                    except mysql.connector.errors.IntegrityError:
                        enviar = '3'
                        conexao_servidor.send(enviar.encode())
                else:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()
        
        def cadastroRecep(self,cpf,nome,telefone,dt_nasc,email,senha):
            try:
                result = self.cad.cadastroRecep(cpf)
                #print(retorno)
                print(result)
                if self.cad.cadastroRecep(cpf):
                    # utilizando comandos SQL para realizar as inserções no banco de dados
                    query = "INSERT INTO recepcionista(cpf,nome,telefone,dt_nasc,email,senha) VALUES(%s,%s,%s,%s,%s,%s)"
                    values = (cpf,nome,telefone,dt_nasc,email,senha)
                    try:
                        # utilizando o cursor para executar a inserção no banco de dados
                        cursor.execute(query, values)
                        #confirmar a inserção
                        conexao.commit()
                        enviar = '1'
                        conexao_servidor.send(enviar.encode())
                    except mysql.connector.errors.IntegrityError:
                        enviar = '3'
                        conexao_servidor.send(enviar.encode())
                else:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()
            


except mysql.connector.Error as erro:
    print(f'Eroo ao conectar o Banco de Dados: {erro}')

if __name__ == "__main__":
    bd = BancoDeDados()
    while True:
        recebe = conexao_servidor.recv(1024)
        if not recebe:
            break  # Encerra o loop se não houver mais mensagens
        
        print("Mensagem recebida: " + recebe.decode())
        bd.processarDados(recebe)
    conexao_servidor.close()
    