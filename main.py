from funcoes import *


def menu_principal():
    print('-'*30)
    print('1 - Realizar cadastros\n')
    print('2 - Atendimento')
    print('3 - consulta')
    print('4 - Finalizar o dia')
    print('-'*30)

while True:
    menu_principal()
    op = int(input('Opcao: '))
    if op == 1:
        menu_cadastro()
        cadastro()
    if op == 2:
        menu_atendimento()
        atendimento()
    if op == 3:
        menu_consulta()
        consulta()

    if op == 4:
        break