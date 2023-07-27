#importação do banco de dados
import mysql.connector
from recepcionista import Recepcionista
from medico import Medico
from admin import Admin

class BancoDeDados:
    """
    A classe BancoDeDados representa o banco de dados

    A classe BancoDeDados e responsavel por fazer as consultas, insercoes, atualizacoes e delecoes no banco de dados do sistema

    Attributes
    ---------
    connection : mysql.connector.connection_cext.CMySQLConnection
        A conexao com o banco de dados
    cursor : mysql.connector.cursor_cext.CMySQLCursor
        O cursor do banco de dados
    recepcionista : NoneType>
        O recepcionista da clinica
    medico : NoneType
        O medico da clinica
    admin : NoneType
        O administrador da clinica

    Methods
    ------
    fazerLoginRecep(cpf,password) : str, str
        Esse metodo representa o login do recepcionista
    fazerLoginMed(cpf,password) : str, str
        Esse metodo representa o login do medico
    fazerLoginAdmin(cpf,password) : str, str
        Esse metodo representa o login do administrador
    cadastroMedico(pessoa) : str
        Esse metodo realiza o cadastro de um medico
    inserirMedico(cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,senha) : str, str, str, str, str, str, str, int, str
        Esse metodo realiza a insercao de um medico no banco de dados
    cadastroRecep(pessoa) : str
        Esse metodo realiza o cadastro de um recepcionista
    inserirRecep(cpf,nome,telefone,dt_nasc,email,senha) : str, str, str, str, str, str 
        Esse metodo realiza a insercao de um recepcionista
    cadastroAdmin(pessoa) : str
        Esse metodo realiza o cadastro de um administrador
    inserirAdmin(cpf_admin, nome, senha) : str, str, str
        Esse metodo realiza a insercao de um administrador
    buscarMedico(cpf) : str
        Esse metodo realiza a busca por um medico pelo cpf
    buscarRecep(cpf) : str
        Esse metodo realiza a busca por um recepcionista pelo cpf
    buscarAdmin(cpf) : str
        Esse meto realiza a busca por um administrador pelo cpf
    atualizar_senha()
        Esse metodo atualiza a senha dos guiches
    iniciar_atendimento()
        Esse metodo inicia o atendimento em um guiche especifico
    finalizar_atendimento()
        Esse metodo finaliza o atendimento em um guiche especifico 
    buscRecep()
        Esse metodo busca pelo recepcionista responsavel por um determinado guiche
    inserirGuiche(status,senha,modo) : str, str, str
        Esse metodo realiza a insercao de um guiche
    buscGuicheRecep()
        Esse metodo busca o ID de um guiche com base no recepcionista
    excluir_guiche(id_guiche) : int 
        Esse metodo realiza a exclusao de um guiche com base no ID desse guiche
    buscGuiche(id_guiche) : int
        Esse metodo busca um guiche com base no ID do mesmo
    ativarGuiche(ident_guiche) : int
        Esse metodo e responsavel por ativar um guiche
    desativarGuiche(idt_guiche) : int
        Esse metodo e responsavel por desativar um guiche
    atualizarModo(id_guiche) : int
        Esse metodo atualiza o modo do guiche para ativo
    atualizarModoInativo(id_guiche) : int
        Esse metodo atualiza o modo do guiche para inativo
    buscRecepcionista(cpf) : str
        Esse metodo busca um recepcionista de um guiche com base no cpf
    buscMed(cpf) : str
        Esse metodo busca o cpf de um determinado medico
    imprimirRecep(pessoa) : str
        Esse metodo busca todos os dados de um recepcionista para impressao
    imprimirMed(pessoa) : str
        Esse metodo busca todos os dados de um medico para impressao
    verificar_tipo(cpf) : str
        Esse metodo verifica o tipo da consulta de um determinado paciente
    enviar_cons(cpf) : str
        Esse metodo envia uma consulta para um medico de acordo com o cpf do paciente
    excluir_consulta(cpf_paciente) : str
        Essse metodo exclui uma consulta do banco de dados
    inseirConsulta(cpf_paciente,nome_paciente,telefone,dt_nasc,medico,crm,tipo,cpf_medico,cpf_recepcionista) : str,str,str,str,str,int,str,str,str
        Esse metodo insere uma consulta no banco de dados
    enviar_consulta()
        Esse metodo envia uma consulta para o medico
    verificaMedico(medico,crm,cpf_medico) : str, int, str
        Esse metodo vai verificar os dados do medico em uma consula
    verificaRecep(cpf_recepcionista) : str
        Esse metodo vai verificar o cpf do recepcionista em uma consulta
    buscarPaciente(cpf) : str
        Esse metodo busca um paciente com base no cpf do mesmo
    buscMedico(cpf) : str
        Esse metodo busca um medico com base no cpf do mesmo
    buscConsulta(cpf) : str
        Esse metodo busca o cpf de um paciente atraves da consulta dele
    buscPaciente(cpf) : str
        Esse metodo busca o cpf de um paciente com base na consulta
    nomeMed()
        Esse metodo busca todos os nomes dos medicos que atendem na clinica
    realizarConsultaAA(medico) : str
        Esse metodo busca pelo cpf e o crm de um determinado medico com base no seu nome
    buscConsult(pessoa) : str
        Esse metodo busca pelos dados de uma consulta para imprimir na tela
    buscPacientes(pessoa) : str
        Esse metodo busca os dados de um paciente para ser feita a atualizacao da consulta do mesmo
    listaPacientes()
        Esse metodo vai listar os pacientes de um determinado medico
    buscarPacientes(cpf_paciente) : str
        Esse metodo vai buscar os pacientes de acordo com o cof e medico responsavel por aquele paciente
    atualizaConsulta(cpf) : str
        Esse metodo atualiza uma consulta de um determinado paciente
    excluiPaci()
        Esse metodo vai verificar se há pacientes para ser excluidos
    deletarPaci(id_paciente) : int 
        Esse metodo vai realizar a exclusao de um paciente
    fecharConexao()
        Esse metodo vai fechar a conexao do cursor e do banco de dados
    """
    
    def __init__(self):
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
        """
        Realiza o login do recepcionista

        Seleciona todos os dados do recepcionista cujo o cpf e a senha sejam iguais aos passados por parametro e cria 
        um usuario recepcionista

        Parameters
        ----------
        cpf : str
            O cpf do recepcionista
        password : str
            Senha do recepcionista
        
        Returns
        -------
        True
            Caso tenha algum recepcionista cadastrado com o cpf e a senha passados por parametro
        False
            Caso nao encontre algum recepcionista com o cpf e a senha passados por parametro
        """

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
        """
        Realiza o login do medico

        Seleciona todos os dados do medico cujo o cpf e a senha sejam iguais aos passados por parametro e cria 
        um usuario medico

        Parameters
        ----------
        cpf : str
            O cpf do medico
        password : str
            Senha do medico
        
        Returns
        -------
        True
            Caso tenha algum medico cadastrado com o cpf e a senha passados por parametro
        False
            Caso nao encontre algum medico com o cpf e a senha passados por parametro
        """
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
        """
        Realiza o login do administrador

        Seleciona todos os dados do administrador cujo o cpf e a senha sejam iguais aos passados por parametro e cria 
        um usuario administrador

        Parameters
        ----------
        cpf : str
            O cpf do administrador
        password : str
            Senha do administrador
        
        Returns
        -------
        True
            Caso tenha algum administrador cadastrado com o cpf e a senha passados por parametro
        False
            Caso nao encontre algum administrador com o cpf e a senha passados por parametro
        """
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
        """
        Realiza o cadastro do medico

        Chama a funcao de buscar os dados do medico para cadastrar um medico

        Parameters
        ----------
        pessoa : str
            O cpf do medico
        
        Returns
        -------
        True
            Caso o retorno da funcao buscarMedico seja None, e porque nao encontrou o medico
        False
            Caso o retorno da funcao buscarMedico nao seja None, e porque encontrou o medico
        """
        verifica = self.buscarMedico(pessoa)     
        if verifica == None:  
            return True
        else:
            return False
    
    def inserirMedico(self, cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,senha): 
        """
        Realiza a insercao de um medico no banco de dados

        O metodo insere todos os dados de um medico no banco de dados 

        Parameters
        ----------
        cpf : str
            O cpf do medico
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
            A hora de atendimento do medico
        crm : int
            O crm do medico
        senha : str
            A senha do medico
        
        Returns
        -------
        True
            Caso a insercao seja realizada com sucesso
        """ 
        self.connection.commit()
        query = "INSERT INTO medico(cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,senha) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,senha)
        self.cursor.execute(query, values)
        self.connection.commit()     
        return True
          
    def cadastroRecep(self, pessoa):
        """
        Realiza o cadastro do recepcionista

        Chama a funcao de buscar os dados do recepcionista para cadastrar um recepcionista

        Parameters
        ----------
        pessoa : str
            O cpf do recepcionista
        
        Returns
        -------
        True
            Caso o retorno da funcao buscarRecep seja None, e porque nao encontrou o recepcionista
        False
            Caso o retorno da funcao buscarRecep nao seja None, e porque encontrou o recepcionista 
        """
        verifica = self.buscarRecep(pessoa)    
        if verifica == None:  
            return True
        else:
            return False
    
    def inserirRecep(self, cpf,nome,telefone,dt_nasc,email,senha):  
        """
        Realiza a insercao de um recepcionista no banco de dados

        O metodo insere todos os dados de um recepcionista no banco de dados 

        Parameters
        ----------
        cpf : str
            O cpf do recepcionista
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
        
        Returns
        -------
        True
            Caso a insercao seja realizada com sucesso
        """ 
        query = "INSERT INTO recepcionista(cpf,nome,telefone,dt_nasc,email,senha) VALUES(%s,%s,%s,%s,%s,%s)"
        values = (cpf,nome,telefone,dt_nasc,email,senha)
        self.cursor.execute(query, values)
        self.connection.commit()     
        return True
        
    def cadastroAdmin(self, pessoa):
        """
        Realiza o cadastro do administrador

        Chama a funcao de buscar os dados do administrador para cadastrar um administrador

        Parameters
        ----------
        pessoa : str
            O cpf do admnistrador
        
        Returns
        -------
        True
            Caso o retorno da funcao buscarAdmin seja None, e porque nao encontrou o administrador
        False
            Caso o retorno da funcao buscarRecep nao seja None, e porque encontrou o administrador
        """
        verifica = self.buscarAdmin(pessoa)    
        if verifica == None:  
            return True
        else:
            return False
    
    def inserirAdmin(self,cpf_admin, nome, senha):
        """
        Realiza a insercao de um administrador no banco de dados

        O metodo insere todos os dados de um administrador no banco de dados 

        Parameters
        ----------
        cpf_admin : str
            O cpf do administrador
        nome : str
            O nome do administrador
        senha : str
            A senha do administrador
        
        Returns
        -------
        True
            Caso a insercao seja realizada com sucesso
        """ 
        query = "INSERT INTO admin(cpf_admin,nome,senha) VALUES(%s,%s,%s)"
        values = (cpf_admin,nome,senha)
        self.cursor.execute(query, values)
        self.connection.commit()
        return True

    def buscarMedico(self, cpf):
        """
        Realiza a busca de um medico no banco de dados

        O metodo busca pelo cpf do medico que e passado como parametro

        Parameters
        ----------
        cpf : str
            O cpf do medico
        
        Returns
        -------
        cpf
            Caso ele encontre um medico cadastrado com o cpf que foi buscado, ele retorna o cpf do medico 
        None
            Caso ele nao encontre um medico cadastrado para aquele cpf 
        """ 
        sql = "SELECT cpf FROM medico WHERE cpf = %s"
        self.cursor.execute(sql,(cpf,))
        selecionar = self.cursor.fetchone()
        if selecionar:
            return cpf
        else:
            return None
    
    def buscarRecep(self, cpf):
        """
        Realiza a busca de um recepcionista no banco de dados

        O metodo busca pelo cpf do recepcionista que e passado como parametro

        Parameters
        ----------
        cpf : str
            O cpf do recepcionista
        
        Returns
        -------
        cpf
            Caso ele encontre um recepcionista cadastrado com o cpf que foi buscado, ele retorna o cpf do recepcionista
        None
            Caso ele nao encontre um recepcionista cadastrado para aquele cpf 
        """
        sql = "SELECT cpf FROM recepcionista WHERE cpf = %s"
        self.cursor.execute(sql,(cpf,))
        selecionar = self.cursor.fetchone()
        if selecionar:
            return cpf
        else:
            return None
    
    def buscarAdmin(self, cpf):
        """
        Realiza a busca de um administrador no banco de dados

        O metodo busca pelo cpf do administrador que e passado como parametro

        Parameters
        ----------
        cpf : str
            O cpf do administrador
        
        Returns
        -------
        cpf
            Caso ele encontre um administrador cadastrado com o cpf que foi buscado, ele retorna o cpf do administrador
        None
            Caso ele nao encontre um administrador cadastrado para aquele cpf 
        """
        sql = "SELECT cpf_admin FROM admin WHERE cpf_admin = %s"
        self.cursor.execute(sql,(cpf,))
        selecionar = self.cursor.fetchone()
        if selecionar:
            return cpf
        else:
            return None
    
    def atualizar_senha(self):
        """
        Realiza a atualizacao da senha dos guiches no banco de dados

        O metodo seleciona todos os guiches e verifica se o guiche e ativo se for e atualizado a senha
        """
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
        """
        Inicia o atendimento em um guiche

        O metodo seleciona todos os dados de um guiche verifica se ele e ativo ou nao, se esta livreou nao, e atualiza a senha e 
        O status desse determinado guiche caso esteja ativo e livre
        
        Returns
        -------
        menssagem1
            Quando o guiche e encontrado, esta ativo e livre entao e retornado uma string com a nova senha a ser chamada pelo guiche
        False
            Quando o guiche e encontrado e esta ativo, porem ele esta ocupado
        True
            Quando o guiche foi encontrado porem ele esta inativo 
        None
            Quando o guiche nao e encontrado 
        """     
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
        """
        Finaliza o atendimento em um guiche

        O metodo seleciona todos os dados de um guiche verifica se ele e ativo, se esta livre ou nao , e atualiza o status desse determinado guiche
        
        Returns
        -------
        menssagem
            Quando o guiche e encontrado, esta ativo e esta ocupado entao e atualizado o status desse guiche
        True
            Quando o guiche foi encontrado porem ele esta livre 
        None
            Quando o guiche e encontrado mais esta inativo
        False
            Quando o guiche nao e encontrado
        """     
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
        """
        Realiza a busca o cpf de um recepcionista

        O metodo busca o cpf do recepcionista que e responsavel por um determinado guiche, 
        
        Returns
        -------
        resultado
            Caso ele encontre um recepcionista cadastrado para aquele determinado guiche
        True
            Caso ele nao encontre um recepcionista cadastrado para aquele guiche 
        """
        consulta = "SELECT recepcionista_cpf FROM guiche WHERE recepcionista_cpf = %s"
        self.cursor.execute(consulta,(self.recepcionista.cpf,))
        resultado = self.cursor.fetchone()
        if resultado != None:
            return resultado
        else:
            return True
        
    def inserirGuiche(self,status,senha,modo):
        """
        Realiza a insercao de um guiche no banco de dados

        O metodo insere todos os dados de um guiche no banco de dados 

        Parameters
        ----------
        status : str
            O status do guiche (livre | ocupado)
        senha : int
            A senha do guiche
        modo : str
            O modo do guiche (ativo | inativo)
        
        Returns
        -------
        True
            Caso a insercao seja realizada com sucesso
        """ 
        guiche = "INSERT INTO guiche(status,senha,modo,recepcionista_cpf) VALUES(%s,%s,%s,%s)"
        values = (status,senha,modo,self.recepcionista.cpf)
        self.cursor.execute(guiche, values,)
        self.connection.commit()
        return True
    
    def buscGuicheRecep(self):
        """
        Realiza a busca de um guiche 

        O metodo busca o ID do guiche com base no recepcionista que e responsavel por esse guiche
        
        Returns
        -------
        resultado
            Representa o ID do guiche que um determinado recepcionista e responsavel
        """
        self.connection.commit()
        consulta = "SELECT id_guiche FROM guiche WHERE recepcionista_cpf = %s"
        self.cursor.execute(consulta,(self.recepcionista.cpf,))
        resultado = self.cursor.fetchone()
        return resultado
    
    def excluir_guiche(self, id_guiche):
        """
        Realiza a exclusao de um guiche no banco de dados

        O metodo exclui um determinado guiche do banco de dados, com base no ID desse guiche

        Parameters
        ----------
        id_guiche : int
            O ID do guiche
        
        Returns
        -------
        True
            Caso o guiche seja encontrado e a exclusao seja realizada com sucesso
        False
            Quando o guiche nao for encontrado
        None
            Quando ocorre um problema com o banco de dados ao excluir um guiche
        """ 
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
        """
        Realiza a busca de um guiche 

        O metodo busca o ID do guiche com base no id_guiche que e passado por parametro 

        Parameters
        ----------
        id_guiche : int
            O ID do guiche
        
        Returns
        -------
        True
            Quando o guiche e encontrado
        False
            Quando o guiche nao e encontrado
        """
        self.cursor.execute("SELECT id_guiche FROM guiche WHERE id_guiche = %s",(id_guiche,))
        dado = self.cursor.fetchone()
        if dado:
            return True
        else:
            return None
    
    def ativarGuiche(self, ident_guiche):
        """
        Ativa um determinado guiche 

        O metodo busca o ID e o modo do guiche com base no ident_guiche que e passado por parametro 

        Parameters
        ----------
        id_guiche : int
            O ID do guiche
        
        Returns
        -------
        False
            Quando o guiche foi encontrado e esta ativo, pois nao podemos ativar um guiche ja ativo
        True
            Quando o guiche e encontrado e esta inativo, nessa situacao podendo ativar esse guiche
        None
            Quando o guiche nao e encontrado
        """
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
        """
        Destiva um determinado guiche 

        O metodo busca o ID e o modo do guiche com base no idt_guiche que e passado por parametro 

        Parameters
        ----------
        id_guiche : int
            O ID do guiche
        
        Returns
        -------
        True
            Quando o guiche e encontrado e esta ativo, nessa situacao podendo desativar esse guiche
        False
            Quando o guiche foi encontrado e esta inativo, pois nao podemos desativar um guiche ja desativado
        None
            Quando o guiche nao e encontrado
        """
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
        """
        Atualiza o modo de um determinado guiche 

        O metodo atualiza o modo do guiche para ativo com base no id_guiche que e passado por parametro 

        Parameters
        ----------
        id_guiche : int
            O ID do guiche
        
        Returns
        -------
        True
            Quando o guiche e atualizado com sucesso
        """
        ativar = "UPDATE guiche SET modo = 'ativo' WHERE id_guiche = %s"
        self.cursor.execute(ativar,(id_guiche,))
        self.connection.commit()
        return True
    
    def atualizarModoInativo(self,id_guiche):
        """
        Atualiza o modo de um determinado guiche 

        O metodo atualiza o modo do guiche para inativo com base no id_guiche que e passado por parametro 

        Parameters
        ----------
        id_guiche : int
            O ID do guiche
        
        Returns
        -------
        True
            Quando o guiche e atualizado com sucesso
        """
        desativar = "UPDATE guiche SET modo = 'inativo' WHERE id_guiche = %s"
        self.cursor.execute(desativar,(id_guiche,))
        self.connection.commit()
        return True
    
    def buscRecepcionista(self, cpf):
        """
        Busca um recepcionista em um guiche 

        O metodo seleciona o cpf do recepcionista que e representante daquele guiche de acordo com o cpf que e passado por parametro

        Parameters
        ----------
        cpf : str
            O cpf do recepcionista
        
        Returns
        -------
        resultado
            Quando o recepcionista e encontrado entao e retornado o cpf dele
        True
            Quando o recepcionista nao foi encontrado
        """
        consulta = "SELECT recepcionista_cpf FROM guiche WHERE recepcionista_cpf = %s"
        self.cursor.execute(consulta,(cpf,))
        resultado = self.cursor.fetchone()
        if resultado != None:
            return resultado
        else:
            return True

    def buscMed(self, cpf):
        """
        Busca um medico 

        O metodo seleciona o cpf do medico de acordo com o cpf que e passado por parametro

        Parameters
        ----------
        cpf : str
            O cpf do medico
        
        Returns
        -------
        cpf
            Quando o medico e encontrado entao e retornado o cpf dele
        None
            Quando o medico nao foi encontrado
        """
        sql = "SELECT cpf FROM medico WHERE cpf = %s"
        self.cursor.execute(sql,(cpf,))
        dado = self.cursor.fetchone()
        if dado:
            return cpf
        else:
            return None


    def imprimirRecep(self,pessoa):
        """
        Busca os dados de um recepcionista para impressao

        O metodo seleciona cada dado de um recepcionista com base no cpf passado por parametro e 
        esses dados sao armazenados em uma lista

        Parameters
        ----------
        pessoa : str
            O cpf do recepcionista
        
        Returns
        -------
        lista
            E retornado uma lista contendo os dados de um recepcionista
        """
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
        """
        Busca os dados de um medico para impressao

        O metodo seleciona cada dado de um medico com base no cpf passado por parametro e 
        esses dados sao armazenados em uma lista

        Parameters
        ----------
        pessoa : str
            O cpf do medico
        
        Returns
        -------
        lista
            E retornado uma lista contendo os dados de um medico
        """
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
        """
        Verifica o tipo de uma consulta 

        O metodo vai chamar a funcao buscConsulta passando o cpf como parametro, que ira buscar uma consulta
        de um determinado paciente, se ela encontrar, vai selecionar o tipo da ultima consulta do paciente

        Parameters
        ----------
        cpf : str
            O cpf do paciente
        
        Returns
        -------
        False
            Quando o tipo da consulta e de retorno a clinica
        True 
            Quando o tipo da consulta e uma nova consulta
        None 
            Quando nao encontra nenhuma consulta cadastrada para aquele paciente
        """
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
        """
        Envia uma consulta ao medico 

        O metodo vai selecionar todos os dados de uma consulta com base no cpf do paciente que e passado como parametro,
        vai fazer as verificacoes se o medico realmente e cadastrado no banco de dados e se o paciente nao esta na lista
        de pacientes entao manda o paciente para a lista de paciente de um medico

        Parameters
        ----------
        cpf : str
            O cpf do paciente
        
        Returns
        -------
        2
            Quando o medico nao for cadastrado 
        3
            Quando o paciente ja estiver na lista de pacientes de um medico
        True
            Quando o paciente e inserido na lista de pacientes de um medico
        False
            Quando nao foi possivel inserir o paciente devido a problemas no bando de dados
        5
            Quando a consulta daquele paciente nao foi encontrada
        0 
            Quando o banco de dados apresenta algum erro
        """
        try:
            self.cursor.execute("SELECT * FROM consulta WHERE cpf_paciente = %s ORDER BY id_consulta DESC LIMIT 1",(cpf,))
            ultimo_elemento = self.cursor.fetchone()
            print('selecao',ultimo_elemento)
            if ultimo_elemento is not None:    
                cpf = ultimo_elemento[1]
                nome = ultimo_elemento[2]
                medico = ultimo_elemento[8]
                print('cpf',cpf)
                print('nome',nome)
                print('medico',medico)
                result = self.buscMedico(medico)
                if result == None:
                    return 2  
                else:
                    result = self.buscarPaciente(cpf)
                    if result != None:
                        return 3
                    else:
                        self.cursor.execute("INSERT INTO lista_pacientes (cpf,nome,medico_cpf) VALUES (%s,%s,%s)",(cpf,nome,medico,))
                        #try:
                        self.connection.commit()
                        print('nao inseriu')
                        return True
                        #except mysql.connector.errors.IntegrityError:
                            #return False
            else:
                return 5
    
        except mysql.connector.Error as error:
            return 0
        
    def excluir_consulta(self, cpf_paciente):
        """
        Exclui uma consulta do banco de dados

        O metodo vai chamar a funcao buscConsulta para buscar a consulta que deseja excluir, e exclui essa consulta

        Parameters
        ----------
        cpf_paciente : str
            O cpf do paciente
        
        Returns
        -------
        True
            Quando a consulta foi excluida com sucesso
        None
            Quando ha um problema no banco de dados ao tentar excluir uma consulta
        False
            Quando a consulta nao foi encontrada
        """
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
        """
        Realiza a insercao de uma consulta no banco de dados

        O metodo insere todos os dados de uma consulta no banco de dados 

        Parameters
        ----------
        cpf_paciente : str
            O cpf do paciente
        nome_paciente : str
            O nome do paciente
        telefone : str
            O telefone do paciente
        dt_nasc : str
            A data de nascimento do paciente
        medico : str
            O nome do medico
        crm : int
            O crm do medico
        tipo : str
            O tipo da consulta 
        cpf_medico : str
            O cpf do medico
        cpf_recepcionista : str
            O cpf do recepcionista
        
        Returns
        -------
        True
            Caso a insercao seja realizada com sucesso
        """ 
        query = "INSERT INTO consulta(cpf_paciente,nome_paciente,telefone,dt_nasc,medico,crm,tipo_consulta,medico_cpf,recepcionista_cpf) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (cpf_paciente,nome_paciente,telefone,dt_nasc,medico,crm,tipo,cpf_medico,cpf_recepcionista)
        self.cursor.execute(query, values)
        self.connection.commit()
        return True
    
    def enviar_consulta(self):
        """
        Envia uma consulta ao medico 

        O metodo vai selecionar todos os dados de uma consulta com base no cpf do recepcionista que e passado como parametro,
        vai fazer as verificacoes se o medico realmente e cadastrado no banco de dados e se o paciente nao esta na lista
        de pacientes entao manda o paciente para a lista de paciente de um medico

        Parameters
        ----------
        cpf : str
            O cpf do paciente
        
        Returns
        -------
        2
            Quando o medico nao for cadastrado 
        3
            Quando o paciente ja estiver na lista de pacientes de um medico
        True
            Quando o paciente e inserido na lista de pacientes de um medico
        False
            Quando nao foi possivel inserir o paciente devido a problemas no bando de dados
        5
            Quando a consulta daquele paciente nao foi encontrada
        0 
            Quando o banco de dados apresenta algum erro
        """
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
        """
        Verifica se os dados do medico estao cadastrados 

        O metodo vai selecionar o nome, crm, cpf_medico que sao passados como parametros

        Parameters
        ----------
        medico : str
            O nome do medico
        crm : int
            O crm do medico
        cpf_medico : str
            O cpf do medico
        
        Returns
        -------
        True 
            Quando o os dados do medico estao cadastrados
        False
            Quando os dados do medico nao estao cadastrados
        """
        self.cursor.execute("SELECT nome,crm,cpf FROM medico WHERE nome = %s AND crm = %s AND cpf = %s",(medico,crm,cpf_medico,))
        dado = self.cursor.fetchone()
        if dado:
            return True
        else:
            return None
    
    def verificaRecep(self,cpf_recepcionista):
        """
        Verifica se o cpf do recepcionista esta cadastrado 

        O metodo vai selecionar o cpf que e passado como parametro

        Parameters
        ----------
        cpf_recepcionista : str
            O cpf do recepcionista
        
        Returns
        -------
        True 
            Quando o os dados do recepcionista estao cadastrados
        None
            Quando os dados do recepcionista nao estao cadastrados
        """
        self.cursor.execute("SELECT cpf FROM recepcionista WHERE cpf = %s",(cpf_recepcionista,))
        dado = self.cursor.fetchone()
        if dado:
            return True
        else:
            return None
    
    def buscarPaciente(self,cpf):
        """
        Busca os pacientes 

        O metodo seleciona o cpf do paciente na lista de pacientes de acordo com o cpf que e passado por parametro

        Parameters
        ----------
        cpf : str
            O cpf do paciente
        
        Returns
        -------
        cpf
            Quando o paciente e encontrado entao e retornado o cpf dele
        None
            Quando o paciente nao foi encontrado
        """
        self.cursor.execute("SELECT cpf FROM lista_pacientes WHERE cpf = %s",(cpf,))
        dado = self.cursor.fetchone()
        if dado:
            return cpf
        else:
            return None

    def buscMedico(self,cpf):
        """
        Busca o medico 

        O metodo seleciona o cpf do medico de acordo com o cpf que e passado por parametro

        Parameters
        ----------
        cpf : str
            O cpf do medico
        
        Returns
        -------
        True
            Quando o medico e encontrado
        None
            Quando o medico nao foi encontrado
        """
        print('entrou')
        self.cursor.execute("SELECT cpf FROM medico WHERE cpf = %s",(cpf,))
        dado = self.cursor.fetchone()
        print('busc consulta',dado)
        if dado:
            return True
        else:
            return None
 
    def buscConsulta(self,cpf):
        """
        Busca uma consulta

        O metodo seleciona o cpf do paciente de acordo com o cpf que e passado por parametro

        Parameters
        ----------
        cpf : str
            O cpf do paciente
        
        Returns
        -------
        cpf
            Quando o paciente e encontrado entao e retornado o cpf dele
        None
            Quando o paciente nao foi encontrado
        """
        self.cursor.execute("SELECT cpf_paciente FROM consulta WHERE cpf_paciente = %s ORDER BY id_consulta DESC LIMIT 1",(cpf,))
        dado = self.cursor.fetchone()
        if dado:
            return cpf
        else:
            return None
    
    def buscPaciente(self, cpf):
        """
        Busca os pacientes 

        O metodo seleciona o cpf do paciente na consulta de acordo com o cpf que e passado por parametro 

        Parameters
        ----------
        cpf : str
            O cpf do paciente
        
        Returns
        -------
        cpf
            Quando o paciente e encontrado entao e retornado o cpf dele
        None
            Quando o paciente nao foi encontrado
        """
        self.cursor.execute("SELECT cpf_paciente FROM consulta WHERE cpf_paciente = %s",(cpf,))
        dado = self.cursor.fetchone()
        if dado:
            return cpf
        else:
            return None

    def nomeMed(self):
        """
        Busca o nome dos medicos

        O metodo seleciona todos os nomes dos medicos que trabalham na clinica e amazena em uma lista
        
        Returns
        -------
        self.recepcionista.cpf
            Representa o cpf do recepcionista 
        dados
            Representa a lista com os nomes dos medicos
        """
        self.cursor.execute("SELECT nome FROM medico")
        listaMed = self.cursor.fetchall()
        dados = ','.join([item[0] for item in listaMed])
        return self.recepcionista.cpf, dados
    
    def realizarConsultaAA(self, medico):
        """
        Busca os dados de um medico

        O metodo seleciona o cpf e o crm de um medico de acordo com o nome que e passado por parametro 

        Parameters
        ----------
        medico : str
            O nome do medico
        
        Returns
        -------
        lisaMed
            Vai retorna uma lista com o cpf e o crm de um medico especifico
        """
        self.cursor.execute("SELECT cpf, crm FROM medico WHERE nome = %s",(medico,))
        listaMed = self.cursor.fetchall()
        return listaMed
    
    def buscConsult(self,pessoa):
        """
        Busca os dados de um paciente

        O metodo seleciona cada dado de uma consulta de um paciente com base no cpf passado por parametro e 
        esses dados sao armazenados em uma lista

        Parameters
        ----------
        pessoa : str
            O cpf do paciente
        
        Returns
        -------
        lista
            E retornado uma lista contendo os dados de um paciente
        """
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
        """
        Busca os dados de um paciente

        O metodo seleciona cada dado de uma consulta de um paciente com base no cpf do paciente passado por parametro e
        no cpf do medico, esses dados sao armazenados em uma lista

        Parameters
        ----------
        pessoa : str
            O cpf do paciente
        
        Returns
        -------
        lista
            E retornado uma lista contendo os dados de um paciente
        """
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
        """
        Lista os pacientes de um determinado medico

        O metodo seleciona o cpf e o nome do paciente de acordo com o cfp do medico responsavel por 
        realizar a consulta
        
        Returns
        -------
        lista
            E retornado uma lista contendo o cpf e o nome de um paciente
        """
        self.connection.commit()
        self.cursor.execute("SELECT cpf, nome FROM lista_pacientes WHERE medico_cpf = %s",(self.medico.cpf,))
        lista = self.cursor.fetchall()
        return lista
    
    """
    def imprimir_pacientes(self, medico):
        lista = "SELECT * FROM lista_pacientes WHERE medico = %s"
        self.cursor.execute(lista,(medico,))
        resultado = self.cursor.fetchall()
        self.connection.commit()
        if len(lista) != 0:
            return resultado
        else:
            return False 
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
        """
        Busca os dados de um paciente

        O metodo seleciona o cpf do paciente de uma consulta de um paciente com base no cpf passado por parametro e no cpf do medico

        Parameters
        ----------
        cpf_paciente : str
            O cpf do paciente
        
        Returns
        -------
        cpf_paciente
            Quando o cpf do pacciente foi encontrado nas consultas
        None
            Quando o cpf do paciente nao foi encontrado
        """
        self.cursor.execute("SELECT cpf_paciente FROM consulta WHERE cpf_paciente = %s AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1",(cpf_paciente, self.medico.cpf,))
        dado = self.cursor.fetchone()
        if dado:
            return cpf_paciente
        else:
            return None

    def atualizaConsulta(self,cpf):
        """
        Atualiza o tipo da consulta

        O metodo seleciona o tipo de uma consulta com base no cpf do paciente passado por parâmetro e no cpf do medico,
        vai ser atualizado para retorno caso a consulta esteja como nova, e vice versa

        Parameters
        ----------
        cpf_paciente : str
            O cpf do paciente
        
        Returns
        -------
        True
            Quando e encontrado o tipo de uma consulta e esse tipo e diferente de retorno, fazendo com que o tipo 
            da consulta seja atualizada para retorno
        False
            Quando e encontrado o tipo da consulta e ela e igual a retorno, fazendo com que o tipo da consulta
            seja atualizada para nova
        None
            Quando nao e encontrado um tipo de consulta para o cpf epecificado
        """
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
        """
        Seleciona todos os pacientes da lista de ppacientes

        O metodo seleciona todos os pacientes da lista de pacientes de forma ordenada para garantir a fila de atendimento

        Returns
        -------
        resultado
            Retorna os dados dos pacientes da lissta de pacientes de um medico
        """
        selecione = "SELECT * FROM lista_pacientes ORDER BY id_paciente LIMIT 1"
        self.cursor.execute(selecione)
        resultado = self.cursor.fetchone() 
        return resultado 
    
    def deletarPaci(self,id_paciente):
        """
        Exclui um paciente da lista de pacientes de um medico

        O metodo vai deletar o paciente com baseno id_paciente que e fornecido por parametro

        Parameters
        ----------
        id_paciente : int
            O ID do paciente
        
        Returns
        -------
        True
            Quando o paciente foi excluido com sucesso
        """
        excluido = "DELETE FROM lista_pacientes WHERE id_paciente = %s"
        self.cursor.execute(excluido, (id_paciente,))
        self.connection.commit()
        return True


    def fecharConexao(self):
        """
        Fecha a conexao com o cursor e com o banco de dados

        """
        self.cursor.close()
        self.connection.close()
        print('Conexão com Banco de dados FECHADA')
