import socket
import threading
import os

HOST = '0.0.0.0'
PORT = 6000


def handle_client(conn, addr):
    try:
        data = conn.recv(1024)
        if not data:
            return
        line = data.decode('utf-8').strip()
        if not line.startswith('GET|'):
            conn.sendall(b'ERR|comando invalido\n')
            return
        fname = line.split('|', 1)[1]
        if not os.path.exists(fname):
            conn.sendall(b'ERR|arquivo nao encontrado\n')
            return
        size = os.path.getsize(fname)
        conn.sendall(f'OK|{size}\n'.encode('utf-8'))
        with open(fname, 'rb') as f:
            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                conn.sendall(chunk)
    finally:
        conn.close()


def main():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print(f'Servidor backup em {HOST}:{PORT}')
    try:
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
    except KeyboardInterrupt:
        pass
    finally:
        s.close()


if __name__ == '__main__':
    main()
