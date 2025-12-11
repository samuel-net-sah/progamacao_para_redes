import socket
import sys
import os


def main():
    if len(sys.argv) < 4:
        print('Uso: python cliente_backup.py <host> <porta> <arquivo_remoto> [dest_local]')
        return
    host = sys.argv[1]
    port = int(sys.argv[2])
    filename = sys.argv[3]
    dest = sys.argv[4] if len(sys.argv) > 4 else os.path.basename(filename)
    s = socket.socket()
    s.connect((host, port))
    try:
        s.sendall(f'GET|{filename}\n'.encode('utf-8'))
        header = b''
        while b'\n' not in header:
            chunk = s.recv(1024)
            if not chunk:
                print('Conexão fechada')
                return
            header += chunk
        line, rest = header.split(b'\n', 1)
        line = line.decode('utf-8').strip()
        if line.startswith('ERR|'):
            print('Erro:', line.split('|', 1)[1])
            return
        size = int(line.split('|', 1)[1])
        received = rest
        with open(dest, 'wb') as f:
            f.write(received)
            remaining = size - len(received)
            while remaining > 0:
                chunk = s.recv(4096)
                if not chunk:
                    break
                f.write(chunk)
                remaining -= len(chunk)
        print('Arquivo salvo em', dest)
    finally:
        s.close()


if __name__ == '__main__':
    main()
