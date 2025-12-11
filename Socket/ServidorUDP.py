import socket

servidor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
servidor.bind(("0.0.0.0", 5000))
print("Servidor UDP esperando menssagem... ")

while True:
    data , adress = servidor.recv(1024)
    print(data.decode())
    servidor.senditor("Recebido")