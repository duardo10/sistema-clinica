import mysql.connector
from conexao_BDmysql import *


# configurações da conexão com o banco de dados 
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'mydb',
    'raise_on_warnings': True
}
"""
    PARTE DO MAIN
    """
try:
    # conectar com o banco de dados
    conexao = mysql.connector.connect(**config)

    # criando cursor para executar consultas
    cursor = conexao.cursor()

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
                    pass
                if op == 2:
                    excluir_paciente_lista()
                    pass
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
                    imprimir_dados()
                if op == 5:
                    break
        elif op == 3:
            # fechar o cursor e a conexão
            cursor.close()
            conexao.close()
            break
        else:
            print('Escolha uma opção do menu!')

except mysql.connector.Error as erro:
    print(f'Eroo ao conectar o Banco de Dados: {erro}')