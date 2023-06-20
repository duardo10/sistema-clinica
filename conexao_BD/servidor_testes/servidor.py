import socket
host = '0.0.0.0'
port = 8094
addr = (host, port)

serv_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serv_socket.bind(addr)
serv_socket.listen(10)
print("Aguardando conexão...")
conexao, cliente = serv_socket.accept()
print("Conectado")
print("Aguardando menssagem...")

while True:
    try:
        recebe = conexao.recv(1024)
        if recebe.decode().lower() == 'sair':
            print('Finalizado')
            conexao.send('conexão encerrada'.encode())
            break
        print("menssagem recebida: " + recebe.decode())
        enviar = input("Digite uma menssagem para enviar para o cliente: ")
        conexao.send(enviar.encode())
        if enviar.lower() == 'sair':
            print('finalizado')
            conexao.close()
            break
        
    except:
        serv_socket.close()
        break

conexao.close()
serv_socket.close()