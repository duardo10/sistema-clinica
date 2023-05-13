from funcoes_recepcionista import *
from funcoes_medico import *


def menu_principal():
    print('-'*30)
    print('1 - Realizar cadastros')
    print('2 - Atendimento')
    print('3 - consulta')
    print('4 - imprimir dados')
    print('5 - Finalizar o dia')
    print('-'*30)

def menu_medico():
    print('-'*30)
    print('1 - imprimir lista de pacientes')
    print('2 - Excluir paciente da lista')
    print('3 - Encerrar seção do médico')
    print('-'*30)

def login():
    print('=-'*30)
    print('    Login')
    print('=-'*30)
    print('-'*30)
    print('1 - médico')
    print('2 - recepcionista')
    print('3 - encerrar programa')
    print('-'*30)


"""
##-MAIN-##
"""
while True:
    login()
    op = int(input('Opcao: '))
    if op == 1:
        while True:
            menu_medico()
            op = int(input('Opcao: '))
            if op == 1:
                imprimir_lista_pacientes()
            if op == 2:
                excluir_paciente_lista()
            if op == 3:
                break
    elif op == 2:
        while True:
            menu_principal()
            op = int(input('Opcao: '))
            if op == 1:
                cadastro()
            if op == 2:
                atendimento()
            if op == 3:
                consulta()
            if op == 4:
                imprimir()
            if op == 5:
                break
    elif op == 3:
        break
    else:
        print('Escolha uma opção do menu!')