import socket
ip = '192.168.0.118'
port = 9002
addr = ((ip, port))

cliente_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente_socket.connect(addr)

while True:
    try:
        menssagem = input("Digite uma menssagem para enviar ao servidor: ")
        #if menssagem.lower == 'sair':
        #    print('saida!.')
        #    break
        cliente_socket.send(menssagem.encode())
        print('menssagem enviada')
        print("menssagem recebida: " + cliente_socket.recv(1024).decode())

    except:
        cliente_socket.close()
        