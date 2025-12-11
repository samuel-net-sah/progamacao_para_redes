import socket
import sys

CONFIG_FILE = 'servicos.txt'


def check(ip, port, timeout=1.0):
    s = socket.socket()
    s.settimeout(timeout)
    try:
        s.connect((ip, int(port)))
        s.close()
        return True
    except Exception:
        return False


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else CONFIG_FILE
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = [l.strip() for l in f if l.strip() and not l.strip().startswith('#')]
    except Exception:
        print('Erro ao ler', path)
        return
    for line in lines:
        name, ip, port = line.split(';')[:3]
        ok = check(ip, port)
        print(('[OK] ' if ok else '[FALHA]') + f" {name} ({ip}:{port})")


if __name__ == '__main__':
    main()
