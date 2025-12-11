
import socket
import threading


servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


servidor.bind(("127.0.0.1", 5000))


servidor.listen()

print("Esperando uma conexão!!!!")

print("Endereço do cliente conectado: ", address)

mensagem = conn.recv(1024)
print("Mensagem recebida: ", mensagem.decode())


conn.sendall("Mensagem recebida com sucesso".encode())


conn.close()

servidor.close()