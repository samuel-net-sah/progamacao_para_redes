import socket
import threading

clientes = []

def iniciar_servidor(host='0.0.0.0', port=5000):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((host, port))
    servidor.listen()
    print(f'Servidor ouvindo em {host}:{port}')
    while True:
        cliente, endereco = servidor.accept()
        clientes.append(cliente)
        thread = threading.Thread(target=tratar_mensagens_cliente, args=(cliente, endereco), daemon=True)
        thread.start()


def tratar_mensagens_cliente(cliente, endereco):
    try:
        while True:
            mensagem = cliente.recv(10000)
            if not mensagem:
                break
            enviar_mensagem_clientes(mensagem, cliente)
    except Exception as e:
        print('Erro na recepção de mensagem:', e)
    finally:
        try:
            clientes.remove(cliente)
        except ValueError:
            pass
        try:
            cliente.close()
        except Exception:
            pass


def enviar_mensagem_clientes(mensagem, cliente_origem):
    for cliente in list(clientes):
        try:
            if cliente != cliente_origem:
                cliente.sendall(mensagem)
        except Exception as e:
            print('Erro no envio de mensagem:', e)


if __name__ == '__main__':
    iniciar_servidor()
