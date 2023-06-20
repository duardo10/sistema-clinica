import mysql.connector
from consulta_BD import Consulta
from guiche_BD import Guiche
from medico_BD import Medico

# configurações da conexão com o banco de dados 
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'mydb',
    'raise_on_warnings': True
}

# Menu de opções para a realização de um cadastro!
def menu_cadastro():
        print('-'*30)
        print('1 - Cadastrar Recepcionista')
        print('2 - cadastrar Médico')
        print('3 - Cadastrar outros funcionarios')
        print('4 - Encerrar cadastro')
        print('-'*30)
        opc = int(input('Opcao:'))
        return opc

try:
    # conectar com o banco de dados
    conexao = mysql.connector.connect(**config)
    print('Conexão realizada com sucesso!')

    # criando cursor para executar consultas
    cursor = conexao.cursor()
    def cadastro():
        while True:
            opc = menu_cadastro()
            # a opção 1 tem como objetivo cadastrar um recepcionista
            if opc == 1:
                try:
                    cpf = input('CPF: ')
                    nome = input('Nome: ')
                    telefone = input('Telefone: ')
                    dt_nasc = input('Data de nascimento: ')
                    email = input('Email: ')
                except:
                    print('Dados invalidos')
                # utilizando comandos SQL para realizar as inserções no banco de dados
                query = "INSERT INTO recepcionista(cpf,nome,telefone,dt_nasc,email,guiche_id_guiche) VALUES(%s,%s,%s,%s,%s,%s)"
                values = (cpf,nome,telefone,dt_nasc,email,1)

                # utilizando o cursor para executar a inserção no banco de dados
                cursor.execute(query, values)

                #confirmar a inserção
                conexao.commit()
                print('Recepcionista Cadastrado com sucesso!')
                # SELEÇÃO DE TODOS OS DADOS 
                """
                query = "SELECT * FROM recepcionista"

                cursor.execute(query)
                # pega todos os resultados da consulta
                result = cursor.fetchall()
                # exibe os resultados
                for x in result:
                    print(x)
                # fechar o cursor e a conexão
                cursor.close()
                conexao.close()
                """
            
            elif opc == 2:
                try:
                    cpf = input('CPF: ')
                    nome = input('Nome: ')
                    telefone = input('Telefone: ')
                    dt_nasc = input('Data de nascimento: ')
                    email = input('Email: ')
                    especialidade = input('Especialidade: ')
                    hr_atendimento = input('Hora de atendimento: ')
                    crm = input('CRM: ')
                    qtd_vagas = int(input('Quantidade de vagas: '))
                except:
                    print('Dados invalidos')
                # utilizando comandos SQL para realizar as inserções no banco de dados
                query = "INSERT INTO medico(cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,qtd_vagas,lista_pacientes_cpf) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                values = (cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,qtd_vagas,'sempaciente')

                # utilizando o cursor para executar a inserção no banco de dados            
                cursor.execute(query, values)

                #confirmar a inserção
                conexao.commit()
                print('Medico Cadastrado com sucesso!')
            
            elif opc == 3:
                try:
                    cpf = input('CPF: ')
                    nome = input('Nome: ')
                    telefone = input('Telefone: ')
                    dt_nasc = input('Data de nascimento: ')
                    email = input('Email: ')
                except:
                    print('Dados invalidos')
                query = "INSERT INTO funcionarios(cpf_funcionario,nome,telefone,dt_nasc,email) VALUES(%s,%s,%s,%s,%s)"
                values = (cpf,nome,telefone,dt_nasc,email)

                # utilizando o cursor para executar a inserção no banco de dados            
                cursor.execute(query, values)

                #confirmar a inserção
                conexao.commit()
                print('Funcionario Cadastrado com sucesso!')
            elif opc == 4:
                print('Encerrando etapa de cadastro!\n')
                break

            else:
                print('Escolha uma opção do menu!')
    def menu_atendimento():
        print('-'*30)
        print('1 - iniciar antendimento')
        print('2 - finalizar atendimento')
        print('3 - adicionar guiche')
        print('4 - ativar um guiche')
        print('5 - desativar um guiche')
        print('6 - Encerrar expediente')
        print('-'*30)

    def atendimento():
        while True:
            gui = Guiche()
            menu_atendimento()
            op = int(input('Opcao:'))
            if op == 1:
                gui.iniciar_atendimento()

            elif op == 2:
                gui.finalizar_atendimento()
            
            elif op == 3:
                guiche = "INSERT INTO guiche(senha,status,modo) VALUES(%s,%s,%s)"
                values = (0,'livre','inativo')

                # utilizando o cursor para executar a inserção no banco de dados            
                cursor.execute(guiche, values)

                #confirmar a inserção
                conexao.commit()
                print('Guiche adicionado!')
            
            elif op == 4:
                ident_guiche = int(input('Numero do Guiche: '))
                retorno = gui.ativarGuiche(ident_guiche)
                if retorno == False:
                    print('O Guiche já está ATIVO')
                elif retorno == True:
                    ativar = "UPDATE guiche SET modo = 'ativo' WHERE id_guiche = %s"
                    cursor.execute(ativar,(ident_guiche,))

                    #confirmar a inserção
                    conexao.commit()
                    print('Guiche ATIVADO!')
                else:
                    print('Guiche não encontrado!')

            elif op == 5:           
                ident_guiche = int(input('Numero do Guiche: '))
                retorno = gui.desativarGuiche(ident_guiche)
                if retorno == False:
                    print('O Guiche já está INATIVO')
                elif retorno == True:
                    desativar = "UPDATE guiche SET modo = 'inativo' WHERE id_guiche = %s"
                    cursor.execute(desativar,(ident_guiche,))

                    #confirmar a inserção
                    conexao.commit()
                    print('Guiche DESATIVADO!')
                else:
                    print('Guiche não encontrado!')

            elif op == 6:
                print('Encerrando expediente!\n')
                break
            else:
                print('Escolha uma opção do menu!')

    # Menu de opções para a realização de uma consulta
    def menu_consulta():
        print('-'*30)
        print('1 - Realizar uma consulta')
        print('2 - Enviar consulta para o medico')
        print('3 - Excluir a consulta')
        print('4 - verificar tipo de consulta')
        print('5 - imprimir todas as consultas')
        print('6 - finalizar consulta')
        print('-'*30)

    def consulta():
        while True:
            menu_consulta()
            opc = int(input('Opcao: '))
            consulta = Consulta()
            if opc == 1:
                # pega os dados de um paciente para que se possa ser realizada a consulta!
                try:
                    cpf = input('CPF: ')
                    nome = input('Nome: ')
                    dt_nasc = input('Data de nascimento: ')
                    medico = input('Medico: ')
                    crm = int(input('CRM: '))
                    tipo_consulta = input('Tipo de consulta: ')
                    hr_consulta = input('Hora da consulta: ')
                except:
                    print('Dados invalidos')

                query = "INSERT INTO consulta(cpf_paciente,nome_paciente,dt_nasc,medico,crm,tipo_consulta,hr_consulta) VALUES(%s,%s,%s,%s,%s,%s,%s)"
                values = (cpf,nome,dt_nasc,medico,crm,tipo_consulta,hr_consulta)

                # utilizando o cursor para executar a inserção no banco de dados            
                cursor.execute(query, values)

                #confirmar a inserção
                conexao.commit()
                print('Consulta realizada com sucesso!')

            elif opc == 2:
                consulta.enviar_consulta()

            elif opc == 3:
                cpf_paciente = input('CPF: ')
                consulta.excluir_consulta(cpf_paciente)
                
            elif opc == 4:
                cpf = input('CPF do paciente: ')
                retorno = consulta.verificar_tipo(cpf)
                if retorno == True:
                    print('Nova Consulta')
                    print('valor: R$300 reais')
                elif retorno == False:
                    print('Retorno')
                    print('valor: gratis')
                

            elif opc == 5:
                query = "SELECT * FROM consulta"
                cursor.execute(query)
                consultas = cursor.fetchall()
                print('Estabelecendo conexão')
                conexao.commit()
                for consult in consultas:
                    print(consult)
            
            elif opc == 6:
                print('Encerrando etapa de consulta')
                break
            else:
                print('Opcao incorreta! digite uma das opcoes do menu.')

    # Menu de opções para a impressão de dados
    def menu_imprimir():
        print('='*30)
        print('   || Menu de impressões||')
        print('='*30)
        print('-'*30)
        print('1 - imprimir Recepcionistas')
        print('2 - imprimir Médicos')
        print('3 - imprimir outros funcionarios')
        print('4 - imprimir todos os recepcionistas')
        print('5 - imprimir todos os médicos')
        print('6 - imprimir todos os outros funcionarios')
        print('7 - encerrar impressão')
        print('-'*30)

    def imprimir_dados():
        while True:
            menu_imprimir()
            op = int(input('Opcao: '))
            # A opção 1 tem como objetivo buscar e imprimir os dados de um recepcionista 
            if op == 1:
                cpf = input('Digite o CPF do recepcionista: ')
                sql = "SELECT * FROM recepcionista WHERE cpf = %s"
                cursor.execute(sql,(cpf,))
                imprimir_recep = cursor.fetchall()
                
                conexao.commit()
                for recep in imprimir_recep:
                    print(recep)
                if len(imprimir_recep) == 0:
                    print('CPF não encontrado!')
            elif op == 2:
                cpf = input('Digite o CPF do medico: ')
                sql = "SELECT * FROM medico WHERE cpf = %s"
                cursor.execute(sql,(cpf,))
                imprimir_medico = cursor.fetchall()
                
                conexao.commit()
                for med in imprimir_medico:
                    print(med)
                if len(imprimir_medico) == 0:
                    print('CPF não encontrado!')
            elif op == 3:
                cpf = input('Digite o CPF do funcionario: ')
                sql = "SELECT * FROM funcionarios WHERE cpf_funcionario = %s"
                cursor.execute(sql,(cpf,))
                imprimir_func = cursor.fetchall()
                
                conexao.commit()
                for func in imprimir_func:
                    print(func)
                if len(imprimir_func) == 0:
                    print('CPF não encontrado!')
            elif op == 4:
                sql = "SELECT * FROM recepcionista"
                cursor.execute(sql)
                imprimir_recepcionista = cursor.fetchall()
                
                conexao.commit()
                for recep in imprimir_recepcionista:
                    print(recep)
            elif op == 5:
                sql = "SELECT * FROM medico"
                cursor.execute(sql)
                imprimir_med = cursor.fetchall()
                
                conexao.commit()
                for med in imprimir_med:
                    print(med)
            elif op == 6:
                sql = "SELECT * FROM funcionarios"
                cursor.execute(sql)
                imprimir_funcionario = cursor.fetchall()
                
                conexao.commit()
                for funcionario in imprimir_funcionario:
                    print(funcionario)
            elif op == 7:
                print('Encerrando impressão.')
                break
            else:
                print('Escolha uma das opções do menu!')
                
    """
    FUNÇÕES DO MÉDICO
    """
    medico = Medico()
    def imprimir_lista_pacientes():
        medic = input('Nome do medico: ')
        sql = "SELECT nome FROM medico"
        cursor.execute(sql)
        result = cursor.fetchone()
        if medic == result[0]:        
            resultado = medico.imprimir_pacientes(result[0])
            if len(resultado) == 0:
                print('Não há pacientes para este médico')
            else:
                for dado in resultado:
                    print(dado)
        else:
            print('medico errado')
    
    def excluir_paciente_lista():
        medico.excluir()

    

except mysql.connector.Error as erro:
    print(f'Eroo ao conectar o Banco de Dados: {erro}')
