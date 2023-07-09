#importação do banco de dados
import mysql.connector
from recepcionista import Recepcionista
from medico import Medico
from admin import Admin

class BancoDeDados:
    def __init__(self):
        # configurações da conexão com o banco de dados 
        self.connection = mysql.connector.connect(
            user = 'root',
            password = '',
            host = 'localhost',
            database = 'clinica',
        )
        self.cursor = self.connection.cursor()
        self.recepcionista = None
        self.medico = None
        self.admin = None
        print('Conexão realizada com sucesso!')
    
    def fazerLoginRecep(self, cpf, password):
        sql = "SELECT * FROM recepcionista WHERE cpf = %s AND senha = %s"
        values = (cpf,password)
        self.cursor.execute(sql,values)
        dado = self.cursor.fetchone()
        if dado:
            self.recepcionista = Recepcionista(dado[0],dado[1],dado[2],dado[3],dado[4],dado[5])
            return True 
        else: 
            return False
    
    def fazerLoginMed(self, cpf, password):
        sql = "SELECT * FROM medico WHERE cpf = %s AND senha = %s"
        values = (cpf, password)
        self.cursor.execute(sql, values)
        dado = self.cursor.fetchone()
        print('dadologin:',dado)
        if dado:
            self.medico = Medico(dado[0],dado[1],dado[2],dado[3],dado[4],dado[5],dado[6],dado[7],dado[8])
            return True
        else:
            return False
    
    def fazerLoginAdmin(self, cpf, password):
        sql = "SELECT * FROM admin WHERE cpf_admin = %s AND senha = %s"
        values = (cpf, password)
        self.cursor.execute(sql, values)
        dado = self.cursor.fetchone()
        if dado:
            self.admin = Admin(dado[0],dado[1],dado[2])
            return True
        else:
            return False

    def cadastroMedico(self, pessoa):  
        verifica = self.buscarMedico(pessoa)    
        if verifica == None:  
            return True
        else:
            return False
    
    def inserirMedico(self, cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,senha):  
        query = "INSERT INTO medico(cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,senha) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,senha)
        self.cursor.execute(query, values)
        self.connection.commit()     
        return True
          
    def cadastroRecep(self, pessoa):
        verifica = self.buscarRecep(pessoa)    
        if verifica == None:  
            return True
        else:
            return False
    
    def inserirRecep(self, cpf,nome,telefone,dt_nasc,email,senha):  
        query = "INSERT INTO recepcionista(cpf,nome,telefone,dt_nasc,email,senha) VALUES(%s,%s,%s,%s,%s,%s)"
        values = (cpf,nome,telefone,dt_nasc,email,senha)
        self.cursor.execute(query, values)
        self.connection.commit()     
        return True
        
    def cadastroAdmin(self, pessoa):
        verifica = self.buscarAdmin(pessoa)    
        if verifica == None:  
            return True
        else:
            return False
    
    def inserirAdmin(self,cpf_admin, nome, senha):
        query = "INSERT INTO admin(cpf_admin,nome,senha) VALUES(%s,%s,%s)"
        values = (cpf_admin,nome,senha)
        self.cursor.execute(query, values)
        self.connection.commit()
        return True

    def buscarMedico(self, cpf):
        sql = "SELECT cpf FROM medico WHERE cpf = %s"
        self.cursor.execute(sql,(cpf,))
        selecionar = self.cursor.fetchone()
        if selecionar:
            return cpf
        else:
            return None
    
    def buscarRecep(self, cpf):
        sql = "SELECT cpf FROM recepcionista WHERE cpf = %s"
        self.cursor.execute(sql,(cpf,))
        selecionar = self.cursor.fetchone()
        if selecionar:
            return cpf
        else:
            return None
    
    def buscarAdmin(self, cpf):
        sql = "SELECT cpf_admin FROM admin WHERE cpf_admin = %s"
        self.cursor.execute(sql,(cpf,))
        selecionar = self.cursor.fetchone()
        if selecionar:
            return cpf
        else:
            return None
    
    def atualizar_senha(self):
        selecionar =  "SELECT * FROM guiche"
        self.cursor.execute(selecionar)
        selecionar = self.cursor.fetchall()
        for dado in selecionar:
            if dado[3] == 'ativo':
                senha = dado[2]
                senha += 1
                atualiza = "UPDATE guiche SET senha = %s"
                self.cursor.execute(atualiza,(senha,))
                self.connection.commit()
    
    def iniciar_atendimento(self):     
        self.connection.commit()
        consulta = "SELECT * FROM guiche WHERE recepcionista_cpf = %s"
        self.cursor.execute(consulta,(self.recepcionista.cpf,))
        resultado = self.cursor.fetchone()
        print('banco de dados:',resultado)
        if resultado:
            if resultado[3] == 'ativo':
                if resultado[1] == 'livre':
                    id_guiche_livre = resultado[0]
                    self.atualizar_senha()
                    chamada = "SELECT senha FROM guiche WHERE id_guiche = %s"
                    self.cursor.execute(chamada,(id_guiche_livre,))
                    resultado = self.cursor.fetchone()
                    menssagem1 = 'Senha: {}, se dirija ao Guiche {}'.format(resultado[0], id_guiche_livre)
                    atualizacao = "UPDATE guiche SET status = 'ocupado' WHERE id_guiche = %s"
                    self.cursor.execute(atualizacao, (id_guiche_livre,))
                    self.connection.commit()    
                    return menssagem1
                else:
                    return False
            else:
                return True
        else:
            return None

    def finalizar_atendimento(self):
        consulta = "SELECT * FROM guiche WHERE recepcionista_cpf = %s"
        self.cursor.execute(consulta,(self.recepcionista.cpf,))
        result = self.cursor.fetchone()
        if result:
            if result[3] == 'ativo':
                if result[1] == 'livre':
                    return True
                    
                else:
                    atualiza = "UPDATE guiche SET status = 'livre' WHERE id_guiche = %s"
                    self.cursor.execute(atualiza,(result[0],))
                    self.connection.commit()
                    menssagem = 'Guiche {} agora está liberado!'.format(result[0])
                    return menssagem
            else:
                return None
        else:
            return False
    
    def buscRecep(self):
        consulta = "SELECT recepcionista_cpf FROM guiche WHERE recepcionista_cpf = %s"
        self.cursor.execute(consulta,(self.recepcionista.cpf,))
        resultado = self.cursor.fetchone()
        if resultado != None:
            return resultado
        else:
            return True
        
    def inserirGuiche(self,status,senha,modo):
        guiche = "INSERT INTO guiche(status,senha,modo,recepcionista_cpf) VALUES(%s,%s,%s,%s)"
        values = (status,senha,modo,self.recepcionista.cpf)
        self.cursor.execute(guiche, values,)
        self.connection.commit()
        return True
    
    def buscGuicheRecep(self):
        self.connection.commit()
        consulta = "SELECT id_guiche FROM guiche WHERE recepcionista_cpf = %s"
        self.cursor.execute(consulta,(self.recepcionista.cpf,))
        resultado = self.cursor.fetchone()
        return resultado
    
    def excluir_guiche(self, id_guiche):
        retorno = self.buscGuiche(id_guiche)
        print(retorno)
        if retorno:
            try:
                sql = "DELETE FROM guiche WHERE id_guiche = %s"
                self.cursor.execute(sql,(id_guiche,))
                self.connection.commit()
                return True
            except mysql.connector.Error as error:
                return None
        else:
            return False  
    
    def buscGuiche(self, id_guiche):
        self.cursor.execute("SELECT id_guiche FROM guiche WHERE id_guiche = %s",(id_guiche,))
        dado = self.cursor.fetchone()
        if dado:
            return True
        else:
            return None
    
    def ativarGuiche(self, ident_guiche):
        sql = "SELECT id_guiche,modo FROM guiche WHERE id_guiche = %s"
        self.cursor.execute(sql,(ident_guiche,))
        dado = self.cursor.fetchone()
        if dado:
            if dado[1] == 'ativo':
                return False
            else:
                return True
        else:
            return None      
    
    def desativarGuiche(self, idt_guiche):
        sql = "SELECT id_guiche,modo FROM guiche WHERE id_guiche = %s"
        self.cursor.execute(sql, (idt_guiche,))
        dado = self.cursor.fetchone()
        if dado:
            if dado[1] == 'ativo':
                return True
            else:
                return False
        else:
            return None

    def atualizarModo(self,id_guiche):
        ativar = "UPDATE guiche SET modo = 'ativo' WHERE id_guiche = %s"
        self.cursor.execute(ativar,(id_guiche,))
        self.connection.commit()
        return True
    
    def atualizarModoInativo(self,id_guiche):
        desativar = "UPDATE guiche SET modo = 'inativo' WHERE id_guiche = %s"
        self.cursor.execute(desativar,(id_guiche,))
        self.connection.commit()
        return True
    
    def buscRecepcionista(self, cpf): 
        consulta = "SELECT recepcionista_cpf FROM guiche WHERE recepcionista_cpf = %s"
        self.cursor.execute(consulta,(cpf,))
        resultado = self.cursor.fetchone()
        if resultado != None:
            return resultado
        else:
            return True

    def buscMed(self, cpf):
        sql = "SELECT cpf FROM medico WHERE cpf = %s"
        self.cursor.execute(sql,(cpf,))
        dado = self.cursor.fetchone()
        if dado:
            return cpf
        else:
            return None


    def imprimirRecep(self,pessoa):
        lista = []
        self.cursor.execute('SELECT nome FROM recepcionista WHERE cpf = %s', (pessoa,))
        nome = self.cursor.fetchone()[0]
        lista.append(nome)
        self.cursor.execute('SELECT telefone FROM recepcionista WHERE cpf = %s', (pessoa,))
        telefone = self.cursor.fetchone()[0]
        lista.append(telefone)
        self.cursor.execute('SELECT dt_nasc FROM recepcionista WHERE cpf = %s', (pessoa,))
        dt_nasc = self.cursor.fetchone()[0]
        lista.append(dt_nasc)
        self.cursor.execute('SELECT email FROM recepcionista WHERE cpf = %s', (pessoa,))
        email = self.cursor.fetchone()[0]
        lista.append(email)
        self.cursor.execute('SELECT senha FROM recepcionista WHERE cpf = %s', (pessoa,))
        senha = self.cursor.fetchone()[0]
        lista.append(senha)
        return lista
    
    def imprimirMed(self,pessoa):
        lista1 = []
        self.cursor.execute('SELECT nome FROM medico WHERE cpf = %s', (pessoa,))
        nome = self.cursor.fetchone()[0]
        lista1.append(nome)
        self.cursor.execute('SELECT telefone FROM medico WHERE cpf = %s', (pessoa,))
        telefone = self.cursor.fetchone()[0]
        lista1.append(telefone)
        self.cursor.execute('SELECT dt_nasc FROM medico WHERE cpf = %s', (pessoa,))
        dt_nasc = self.cursor.fetchone()[0]
        lista1.append(dt_nasc)
        self.cursor.execute('SELECT email FROM medico WHERE cpf = %s', (pessoa,))
        email = self.cursor.fetchone()[0]
        lista1.append(email)
        self.cursor.execute('SELECT especialidade FROM medico WHERE cpf = %s', (pessoa,))
        especialidade = self.cursor.fetchone()[0]
        lista1.append(especialidade)
        self.cursor.execute('SELECT hr_atendimento FROM medico WHERE cpf = %s', (pessoa,))
        hr_atendimento = self.cursor.fetchone()[0]
        lista1.append(hr_atendimento)
        self.cursor.execute('SELECT crm FROM medico WHERE cpf = %s', (pessoa,))
        crm = self.cursor.fetchone()[0]
        lista1.append(crm)
        self.cursor.execute('SELECT senha FROM medico WHERE cpf = %s', (pessoa,))
        senha = self.cursor.fetchone()[0]
        lista1.append(senha)
        return lista1
    
    def verificar_tipo(self,cpf):
        retorno = self.buscConsulta(cpf)
        if retorno:
            sql = "SELECT tipo_consulta FROM consulta WHERE cpf_paciente = %s ORDER BY id_consulta DESC LIMIT 1"
            self.cursor.execute(sql,(cpf,))
            tipo_consulta = self.cursor.fetchone()
            if tipo_consulta[0] == 'retorno':
                return False
            else:
                return True
        else:
            return None
    
    def enviar_cons(self,cpf):
        try:
            self.cursor.execute("SELECT * FROM consulta WHERE cpf_paciente = %s",(cpf,))
            ultimo_elemento = self.cursor.fetchone()
            print(ultimo_elemento)
            if ultimo_elemento is not None:    
                cpf = ultimo_elemento[1]
                nome = ultimo_elemento[2]
                medico = ultimo_elemento[8]
                result = self.buscMedico(medico)
                if result == None:
                    return 2  
                else:
                    result = self.buscarPaciente(cpf)
                    if result != None:
                        return 3
                    else:
                        sql = "INSERT INTO lista_pacientes (cpf,nome,medico_cpf) VALUES (%s,%s,%s)"
                        try:
                            self.cursor.execute(sql,(cpf,nome,medico,))
                            self.connection.commit()
                            return True
                        except mysql.connector.errors.IntegrityError:
                            return False
            else:
                return 5
    
        except mysql.connector.Error as error:
            return 0
        
    def excluir_consulta(self, cpf_paciente):
        retorno = self.buscConsulta(cpf_paciente)
        if retorno:
            try:
                sql = "DELETE FROM consulta WHERE cpf_paciente = %s ORDER BY id_consulta DESC LIMIT 1"
                self.cursor.execute(sql,(cpf_paciente,))
                self.connection.commit()
                return True
                
            except mysql.connector.Error as error:
                return None
        else:
            return False
    
    def inserirConsulta(self, cpf_paciente,nome_paciente,telefone,dt_nasc,medico,crm,tipo,cpf_medico,cpf_recepcionista):
        query = "INSERT INTO consulta(cpf_paciente,nome_paciente,telefone,dt_nasc,medico,crm,tipo_consulta,medico_cpf,recepcionista_cpf) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (cpf_paciente,nome_paciente,telefone,dt_nasc,medico,crm,tipo,cpf_medico,cpf_recepcionista)
        self.cursor.execute(query, values)
        self.connection.commit()
        return True
    
    def enviar_consulta(self):
        try:
            self.cursor.execute("SELECT * FROM consulta WHERE recepcionista_cpf = %s ORDER BY id_consulta DESC LIMIT 1",(self.recepcionista.cpf,))
            ultimo_elemento = self.cursor.fetchone()
            print('ultimo elemento',ultimo_elemento)
            if ultimo_elemento is not None:    
                cpf = ultimo_elemento[1]
                nome = ultimo_elemento[2]
                medico = ultimo_elemento[8]
                result = self.buscMedico(medico)
                print(result)
                if result == None:
                    return 2  
                else:
                    result = self.buscarPaciente(cpf)
                    if result != None:
                        return 3
                    else:
                        sql = "INSERT INTO lista_pacientes (cpf,nome,medico_cpf) VALUES (%s,%s,%s)"
                        try:
                            self.cursor.execute(sql,(cpf,nome,medico,))
                            self.connection.commit()
                            return True
                        except mysql.connector.errors.IntegrityError:
                            return False
            else:
                return 5
        except mysql.connector.Error as error:
            return 0
    
    def verificaMedico(self,medico,crm,cpf_medico):
        self.cursor.execute("SELECT nome,crm,cpf FROM medico WHERE nome = %s AND crm = %s AND cpf = %s",(medico,crm,cpf_medico,))
        dado = self.cursor.fetchone()
        if dado:
            return True
        else:
            return None
    
    def verificaRecep(self,cpf_recepcionista):
        self.cursor.execute("SELECT cpf FROM recepcionista WHERE cpf = %s",(cpf_recepcionista,))
        dado = self.cursor.fetchone()
        if dado:
            return True
        else:
            return None
    
    def buscarPaciente(self,cpf):
        self.cursor.execute("SELECT cpf FROM lista_pacientes WHERE cpf = %s",(cpf,))
        dado = self.cursor.fetchone()
        if dado:
            return cpf
        else:
            return None
        
    def buscMedico(self,cpf):
        self.cursor.execute("SELECT cpf FROM medico WHERE cpf = %s",(cpf,))
        dado = self.cursor.fetchone()
        print('busc consulta',dado)
        if dado:
            return True
        else:
            return None

    def buscConsulta(self,cpf):
        self.cursor.execute("SELECT cpf_paciente FROM consulta WHERE cpf_paciente = %s ORDER BY id_consulta DESC LIMIT 1",(cpf,))
        dado = self.cursor.fetchone()
        if dado:
            return cpf
        else:
            return None
    
    def buscPaciente(self, cpf):
        self.cursor.execute("SELECT cpf_paciente FROM consulta WHERE cpf_paciente = %s",(cpf,))
        dado = self.cursor.fetchone()
        if dado:
            return cpf
        else:
            return None

    def nomeMed(self):
        self.cursor.execute("SELECT nome FROM medico")
        listaMed = self.cursor.fetchall()
        dados = ','.join([item[0] for item in listaMed])
        return self.recepcionista.cpf, dados
    
    def realizarConsultaAA(self, medico):
        self.cursor.execute("SELECT cpf, crm FROM medico WHERE nome = %s",(medico,))
        listaMed = self.cursor.fetchall()
        return listaMed
    
    def buscConsult(self,pessoa):
        lista2 = []
        self.cursor.execute('SELECT nome_paciente FROM consulta WHERE cpf_paciente = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,))
        nome = self.cursor.fetchone()[0]
        lista2.append(nome)
        self.cursor.execute('SELECT telefone FROM consulta WHERE cpf_paciente = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,))
        telefone = self.cursor.fetchone()[0]
        lista2.append(telefone)
        self.cursor.execute('SELECT dt_nasc FROM consulta WHERE cpf_paciente = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,))
        dt_nasc = self.cursor.fetchone()[0]
        lista2.append(dt_nasc)
        self.cursor.execute('SELECT medico FROM consulta WHERE cpf_paciente = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,))
        medico = self.cursor.fetchone()[0]
        lista2.append(medico)
        self.cursor.execute('SELECT crm FROM consulta WHERE cpf_paciente = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,))
        crm = self.cursor.fetchone()[0]
        lista2.append(crm)
        self.cursor.execute('SELECT tipo_consulta FROM consulta WHERE cpf_paciente = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,))
        tipo_consulta = self.cursor.fetchone()[0]
        lista2.append(tipo_consulta)
        self.cursor.execute('SELECT medico_cpf FROM consulta WHERE cpf_paciente = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,))
        cpf_medico = self.cursor.fetchone()[0]
        lista2.append(cpf_medico)
        self.cursor.execute('SELECT recepcionista_cpf FROM consulta WHERE cpf_paciente = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,))
        cpf_recepcionista = self.cursor.fetchone()[0]
        lista2.append(cpf_recepcionista)
        return lista2
    

    def buscPacientes(self, pessoa):
        lista3 = []
        self.cursor.execute('SELECT nome_paciente FROM consulta WHERE cpf_paciente = %s AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1 ', (pessoa,self.medico.cpf,))
        nome = self.cursor.fetchone()[0]
        lista3.append(nome)
        self.cursor.execute('SELECT telefone FROM consulta WHERE cpf_paciente = %s AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,self.medico.cpf,))
        telefone = self.cursor.fetchone()[0]
        lista3.append(telefone)
        self.cursor.execute('SELECT dt_nasc FROM consulta WHERE cpf_paciente = %s AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,self.medico.cpf,))
        dt_nasc = self.cursor.fetchone()[0]
        lista3.append(dt_nasc)
        self.cursor.execute('SELECT medico FROM consulta WHERE cpf_paciente = %s AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,self.medico.cpf,))
        medico = self.cursor.fetchone()[0]
        lista3.append(medico)
        self.cursor.execute('SELECT crm FROM consulta WHERE cpf_paciente = %s AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,self.medico.cpf,))
        crm = self.cursor.fetchone()[0]
        lista3.append(crm)
        self.cursor.execute('SELECT tipo_consulta FROM consulta WHERE cpf_paciente = %s AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,self.medico.cpf,))
        tipo_consulta = self.cursor.fetchone()[0]
        lista3.append(tipo_consulta)
        self.cursor.execute('SELECT medico_cpf FROM consulta WHERE cpf_paciente = %s AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,self.medico.cpf,))
        cpf_medico = self.cursor.fetchone()[0]
        lista3.append(cpf_medico)
        self.cursor.execute('SELECT recepcionista_cpf FROM consulta WHERE cpf_paciente = %s AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,self.medico.cpf,))
        cpf_recepcionista = self.cursor.fetchone()[0]
        lista3.append(cpf_recepcionista)
        return lista3


    def listaPacientes(self):
        self.connection.commit()
        self.cursor.execute("SELECT cpf, nome FROM lista_pacientes WHERE medico_cpf = %s",(self.medico.cpf,))
        lista = self.cursor.fetchall()
        return lista

    def imprimir_pacientes(self, medico):
        lista = "SELECT * FROM lista_pacientes WHERE medico = %s"
        self.cursor.execute(lista,(medico,))
        resultado = self.cursor.fetchall()
        self.connection.commit()
        if len(lista) != 0:
            return resultado
        else:
            return False 
    """
    def excluir(self, cpf):
        selecione = "SELECT * FROM lista_pacientes WHERE medico_cpf = %s ORDER BY id_paciente LIMIT 1"
        self.cursor.execute(selecione,(cpf,))
        resultado = self.cursor.fetchone()
        if resultado is not None:
            excluido = "DELETE FROM lista_pacientes WHERE id_paciente = %s"
            self.cursor.execute(excluido,(resultado[0],)) 
            pacientes = self.cursor.fetchone()
            self.connection.commit()
            print(pacientes)
            #QtWidgets.QMessageBox.information(None, 'interface', f"O registro com ID {resultado[0]} foi excluído com sucesso.")
        else:
            pass
            #QtWidgets.QMessageBox.information(None, 'interface', "A tabela está vazia ou não há registros para excluir.")
       """
    def buscarPacientes(self,cpf_paciente):
        self.cursor.execute("SELECT cpf_paciente FROM consulta WHERE cpf_paciente = %s AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1",(cpf_paciente, self.medico.cpf,))
        dado = self.cursor.fetchone()
        if dado:
            return cpf_paciente
        else:
            return None

    def atualizaConsulta(self,cpf):
        selecione = "SELECT tipo_consulta FROM consulta WHERE cpf_paciente = %s AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1"
        self.cursor.execute(selecione,(cpf,self.medico.cpf,))
        resultado = self.cursor.fetchone()
        if resultado is not None:       
            if resultado[0] != 'retorno':
                atualiza = "UPDATE consulta SET tipo_consulta = 'retorno' WHERE cpf_paciente = %s  AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1"
                self.cursor.execute(atualiza,(cpf,self.medico.cpf,))
                self.connection.commit()
                return True
            elif resultado[0] == 'retorno':
                atualiza = "UPDATE consulta SET tipo_consulta = 'nova' WHERE cpf_paciente = %s  AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1"
                self.cursor.execute(atualiza,(cpf,self.medico.cpf,))
                self.connection.commit()
                return False
            else:
                print('ERRO')       
        else:
            return None
    
    def excluiPaci(self):
        selecione = "SELECT * FROM lista_pacientes ORDER BY id_paciente LIMIT 1"
        self.cursor.execute(selecione)
        resultado = self.cursor.fetchone() 
        return resultado 
    
    def deletarPaci(self,id_paciente):
        excluido = "DELETE FROM lista_pacientes WHERE id_paciente = %s"
        self.cursor.execute(excluido, (id_paciente,))
        self.connection.commit()
        return True


    def fecharConexao(self):
        self.cursor.close()
        self.connection.close()
        print('Conexão com Banco de dados FECHADA')
