import socket
ip = '10.180.47.232'
port = 7017
name = input('Qual seu nome:')
addr = ((ip, port))

cliente_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente_socket.connect(addr)
cliente_socket.send(name.encode())

while True:
    menssagem = input("Digite uma menssagem para enviar ao servidor: ")
    cliente_socket.send(menssagem.encode())
    print('menssagem enviada')
    if menssagem.lower == 'bye':
        print('Cliente desconectado')
        break

    #print("menssagem recebida: " + cliente_socket.recv(1024).decode())
cliente_socket.close()