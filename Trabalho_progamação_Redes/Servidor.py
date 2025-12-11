import socket
import threading
from datetime import datetimt 

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("0.0.0.0,5000"))
servidor.listen()
print("Agurdando conexões com o cliente...")

def tratar_cliente(cliente_socket, endereco):
    print(f"Conexão estabelecida com {endereco}")
    while True:
        dados = cliente_socket.recv(1024)
        if not dados:
            break
        mensagem = dados.decode("utf-8")
        print(f"[{datetimt.now()}] Mensagem recebida de {endereco}: {mensagem}")
        cliente_socket.send(f"Mensagem recebida: {mensagem}".encode("utf-8"))
    cliente_socket.close()
    print(f"Conexão encerrada com {endereco}")