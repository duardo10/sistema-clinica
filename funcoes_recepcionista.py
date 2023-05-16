from guiche import Guiche
from recepcionista import Recepcionista
from medico import Medico
from funcionario import Funcionario
from consulta import Consulta


dc_recepcionista = {}
dc_medico = {}
dc_funcionarios = {}
dc_consulta = {}
dc_pacientes = {}
lista_pacientes = []


def menu_atendimento():
        print('-'*30)
        print('1 - iniciar antendimento')
        print('2 - finalizar atendimento')
        print('3 - Encerrar expediente')
        print('-'*30)

def atendimento():
    status = 'livre'
    paciente = 'Luis'
    senha = 0
    ident = int(input('Numero do Guichê: '))
    gui = Guiche(ident, status, paciente, senha)

    while True:
        menu_atendimento()
        op = int(input('Opcao:'))
        if op == 1:
            retorno = gui.iniciar_atendimento(paciente, ident)
            if retorno == True:
                print('Senha: {}'.format(gui._senha))
                print('Atendimento iniciado no Guichê {} \n'.format(gui._id_guiche))
            elif retorno == False:
                print('Este Guichê já está em uso\n')

        elif op == 2:
            retorno = gui.finalizar_atendimento()
            if retorno == True:
                print('Guichê liberado!\n')
            else:
                print('Este Guichê não foi utilizado\n')
        
        elif op == 3:
            print('Encerrando expediente!\n')
            break
        else:
            print('Escolha uma opção do menu!')

def menu_cadastro():
    print('-'*30)
    print('1 - Cadastrar Recepcionista')
    print('2 - cadastrar Médico')
    print('3 - Cadastrar outros funcionarios')
    print('4 - Encerrar cadastro')
    print('-'*30)
    opc = int(input('Opcao:'))
    return opc

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

            recepcionista = Recepcionista(cpf, nome, telefone, dt_nasc, email)
            dc_recepcionista[cpf] = recepcionista
            print('Recepcionista Cadastrado com sucesso!')

        # A opção 2 tem como objetivo cadastrar um médico 
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
            medico = Medico(cpf, nome, telefone, dt_nasc, email, especialidade, hr_atendimento, crm, qtd_vagas)
            dc_medico[nome] = medico
            print('Medico(a) Cadastrado com sucesso!')

        # A opção 3 tem como objetivo cadastrar um funcionário 
        elif opc == 3:
            try:
                cpf = input('CPF: ')
                nome = input('Nome: ')
                telefone = input('Telefone: ')
                dt_nasc = input('Data de nascimento: ')
                email = input('Email: ')
            except:
                print('Dados invalidos')
        

            funcionario = Funcionario(cpf, nome, telefone, dt_nasc, email)
            dc_funcionarios[cpf] = funcionario
            print('Funcionario Cadastrado com sucesso!')

        # A opção 4 tem como objetivo encerrar a eptapa de cadastramento
        elif opc == 4:
            print('Encerrando etapa de cadastro!\n')
            break

        else:
            print('Escolha uma opção do menu!')


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
        if opc == 1:
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
            
            consulta = Consulta(cpf,nome,dt_nasc,medico,crm,tipo_consulta,hr_consulta)
            verifica_vagas(consulta._medico) 
            dc_consulta[cpf] = consulta
            print(dc_consulta) 
            for chave, valor in dc_consulta.items():
                print(chave)
                print(valor._nome_paciente)
                
            
            """
            consulta = Consulta(cpf,nome,dt_nasc,medico,crm,tipo_consulta,hr_consulta)
            print('Medicos')
            print(dc_medico)
            for medico in dc_medico.keys():
                retorno = dc_medico[medico].vagas_disponiveis()
                if retorno == True:
                    dc_consulta[cpf] = consulta           
                    print('Consulta realizada!')
                elif retorno == False:
                    print('As vagas para esse médico já estão preenchidas!')
                    break
            """
        elif opc == 2:
            cpf = input('CPF do paciente:')
            if cpf in dc_consulta.keys():
                nome = input('Nome do médico: ')
                if nome in dc_medico.keys() and nome == consulta._medico:
                    nome_paciente = dc_consulta[cpf].enviar_consulta(dc_consulta)
                    dc_pacientes[cpf] = nome_paciente
                    print(dc_pacientes)
                else:
                    print('Nome do médico não corresponde ao nome do médico cadastrado na consulta')
            else:
                print('CPF não encontrado!')
        
        elif opc == 3:
            print(dc_consulta)
            cpf_paciente = input('CPF: ')
            if cpf_paciente in dc_consulta.keys():            
                retorno = dc_consulta[cpf_paciente].excluir_consulta(cpf_paciente, dc_consulta)
                print('Excluido:')
                if retorno == False:
                    print('CPF não encontrado')
                print(dc_consulta)
            else:
                print('CPF não encontrado!')

        elif  opc == 4:
            cpf = input('CPF:')
            if cpf in dc_consulta.keys():
                retorno = dc_consulta[cpf].verificar_tipo()
                if retorno == True:
                    print('Nova consulta')
                    print('valor: R$300 reais')
                elif retorno == False:
                    print('Retorno')
                    print('valor: gratis')
            else:
                print('CPF não encontrado')
        
        elif opc == 5:
            for chave, valor in dc_consulta:
                print('\nConsultas:')
                print('CPF: ', chave)
                print('Nome: ', valor._nome_paciente)
                print('Data de nascimento: ', valor._dt_nasc)
                print('Medico: ', valor._medico)
                print('CRM: ', valor._crm)
                print('Tipo da consulta(retorno/nova consulta): ')
                print('Hora da consulta: ', valor._hr_consulta)
        elif opc == 6:
            break
        else:
            print('Escolha uma opção do menu!')
                
            
            



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
        opc = int(input('Opção: '))
        # A opção 1 tem como objetivo buscar e imprimir os dados de um recepcionista 
        if opc == 1:
            cpf = input('Digite o CPF do recepcionista: ')
            for chave in dc_recepcionista.keys():
                if chave == cpf:
                    dc_recepcionista[cpf].imprimir()
                else:
                    print('CPF não encontrado')
                

        # A opção 2 tem como objetivo buscar e imprimir os dados de um médico
        elif opc == 2:
            nome = input('Digite o nome do Médico: ')
            for chave in dc_medico.keys():
                if chave == nome:
                    dc_medico[nome].imprimir()
                else:
                    print('CPF não encontrado')
            

        # A opção 3 tem como objetivo buscar e imprimir os dados de outros funcionários da clínica
        elif opc == 3:
            cpf = input('Digite o CPF do funcionario: ')
            for chave in dc_funcionarios.keys():
                if chave == cpf:
                    dc_funcionarios[cpf].imprimir()
                else:
                    print('CPF não encontrado')

        elif opc == 4:
            if len(dc_recepcionista) > 0:
                for chave, valor in dc_recepcionista.items():
                    print('\nRecepcionista')
                    print("CPF:",chave)
                    print("Nome: ",valor._nome)
                    print("Telefone: ",valor._telefone)
                    print("Data de nascimento: ",valor._dt_nasc)
                    print("Email: ",valor._email)
            else:
                print('Não há recepcionistas cadastrados')
        elif opc == 5:
            if len(dc_medico) > 0:
                for chave, valor in dc_medico.items():
                    print('\nMedico')
                    print('CPF: ', valor._cpf)
                    print('Nome: ', chave)
                    print('Telefone: ', valor._telefone)
                    print('Data de nascimento: ', valor._dt_nasc)
                    print('Email: ', valor._email)
                    print('Especialidade: ', valor._especialidade)
                    print('Hora de atendimento: ', valor._hr_atendimento)
                    print('CRM: ', valor._crm)
            else:
                print('Não há medicos cadastrados')
        elif opc == 6:
            if len(dc_funcionarios) > 0:
                for chave, valor in dc_funcionarios.items():
                    print('\nFuncionario')
                    print("CPF:",chave)
                    print("Nome: ",valor._nome)
                    print("Telefone: ",valor._telefone)
                    print("Data de nascimento: ",valor._dt_nasc)
                    print("Email: ",valor._email)
            else:
                print('Não há funcionarios cadastrados')
        elif opc == 7:
            break
        else:
            print('Escolha uma das opções do menu!')

def verifica_vagas(medico):
    print(medico)
    if medico in dc_medico.keys():
        if dc_medico[medico]._qtd_vagas > 0:
            dc_medico[medico]._qtd_vagas -= 1
            print(dc_medico[medico]._qtd_vagas)
        else:
            print('Esgotado')


"""
=====FUNÇÕES DO MÉDICO======
"""

def imprimir_lista_pacientes():
    nome = input('nome do medico: ')
    if nome in dc_medico.keys():
        dc_medico[nome].imprimir_lista_de_pacientes(dc_pacientes)
    else:
        print('Nome não encontrado')

def excluir_paciente_lista():
    cpf = input('CPF: ')  
    if cpf in dc_pacientes.keys():
        del(dc_pacientes[cpf])
        print('paciente atendido!')
    else:
        print('Paciente não esta na lista')
"""
def verifica_vagas():
    print(dc_medico)
    for nome, medico in dc_medico.items():
        if nome in dc_medico.keys():
            if medico._qtd_vagas > 0:
                medico._qtd_vagas -= 1
                print(medico._qtd_vagas)
            else:
                print('Esgotado')

def verifica_vagas():
     print(dc_medico)
     for chave in dc_medico.keys():
        if dc_medico[chave]._qtd_vagas > 0:
            dc_medico[chave]._qtd_vagas -= 1
            print(dc_medico[chave]._qtd_vagas)
        else:
            print('Esgotado')
    
            


            """


    
"""           
def verifica_vagas():
     print(dc_medico)
     for medico in dc_medico.keys():
        retorno = dc_medico[medico].vagas_disponiveis()
        if retorno == True:         
            print('Consulta realizada!')
        elif retorno == False:
            print('As vagas para esse médico já estão preenchidas!')
            break
        
"""