import socket
import sys


def check(ports):
    out = {}
    for p in ports:
        s = socket.socket()
        s.settimeout(0.8)
        try:
            s.connect(('127.0.0.1', int(p)))
            s.close()
            out[p] = True
        except Exception:
            out[p] = False
    return out


def main():
    ports = [22, 80, 5432] if len(sys.argv) == 1 else [int(x) for x in sys.argv[1:]]
    res = check(ports)
    print('Relatório de verificação - localhost')
    for p, ok in res.items():
        print(f'Porta {p}:', 'OK' if ok else 'FALHA')


if __name__ == '__main__':
    main()
