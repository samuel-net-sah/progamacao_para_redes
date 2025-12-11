import socket


cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("0.0.0.0", 5000))

try:
    while True:
        mensagem = input('> ')
        if mensagem.strip().lower() == '/exit':
            break
        cliente.sendall(mensagem.encode())
        resposta = cliente.recv(1024)
        print(resposta.decode())
except KeyboardInterrupt:
    pass
finally:
    cliente.close()
