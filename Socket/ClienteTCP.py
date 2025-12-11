#Importa o módulo socket
import socket
#Cria o objeto socket do tipo IPV4 e TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Estabelece conexão com o servidor que está operando na porta 5000
#cliente.connect(("127.0.0.1", 5000))
cliente.connect(("10.209.1.168", 5000))
#O cliente envia uma mensagem para o servidor
cliente.sendall("Mensagem do cliente".encode())
#O cliente recebe uma mensagem
mesagemServidor = cliente.recv(1024)
print(mesagemServidor.decode())
cliente.close()