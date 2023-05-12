from guiche import Guiche
from recepcionista import Recepcionista
from medico import Medico
from funcionario import Funcionario
from consulta import Consulta

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

        if op == 2:
            retorno = gui.finalizar_atendimento()
            if retorno == True:
                print('Guichê liberado!\n')
            else:
                print('Este Guichê não foi utilizado\n')
        
        if op == 3:
            print('Encerrando expediente!\n')

def menu_cadastro():
    print('-'*30)
    print('1 - Cadastrar Recepcionista')
    print('2 - cadastrar Médico')
    print('3 - Cadastrar outros funcionarios')
    print('4 - Encerrar cadastro')
    print('-'*30)

def cadastro():
    dc_recepcionista = {}
    dc_medico = {}
    dc_funcionarios = {}

    while True:
        menu_cadastro()
        opc = int(input('Opcao:'))
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

        if opc == 2:
            try:
                cpf = input('CPF: ')
                nome = input('Nome: ')
                telefone = input('Telefone: ')
                dt_nasc = input('Data de nascimento: ')
                email = input('Email: ')
                especialidade = input('Especialidade: ')
                hr_atendimento = input('Hora de atendimento: ')
                crm = input('CRM: ')
            except:
                print('Dados invalidos')
            medico = Medico(cpf, nome, telefone, dt_nasc, email, especialidade, hr_atendimento, crm)
            dc_medico[cpf] = medico
            print('Medico(a) Cadastrado com sucesso!')

        if opc == 3:
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
        
        if opc == 4:
            print('Encerrando etapa de cadastro!\n')
            break


def menu_consulta():
    print('-'*30)
    print('1 - Realizar uma consulta\n')
    print('2 - Enviar consulta para o medico\n')
    print('3 - Excluir a consulta')
    print('4 - finalizar consulta')
    print('-'*30)

def consulta():
    dc_consulta = {}
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
            dc_consulta[cpf] = consulta
            print('Consulta realizada!')
        if opc == 2:
            cpf_n = input('CPF: ')
            if cpf_n in dc_consulta.keys():
                dc_consulta[cpf].enviar_consulta(cpf_n)
            else:
                print('CPF não encontrado!')
        if opc == 3:
            cpf_n = input('CPF: ')
            if cpf_n in dc_consulta.keys():
                dc_consulta[cpf].excluir_consulta(cpf_n)
            else:
                print('CPF não encontrado!')
        
        if opc == 4:
            break


        


    
