import socket
import sys


def parse_range(s):
    try:
        base, last = s.rsplit('.', 1)
        a, b = last.split('-')
        return [f"{base}.{i}" for i in range(int(a), int(b) + 1)]
    except Exception:
        return []


def up(ip, port=80, timeout=0.8):
    s = socket.socket()
    s.settimeout(timeout)
    try:
        s.connect((ip, port))
        s.close()
        return True
    except Exception:
        return False


def main():
    rng = sys.argv[1] if len(sys.argv) > 1 else input('Faixa (ex: 192.168.0.1-192.168.0.10): ')
    ips = parse_range(rng.strip())
    if not ips:
        print('Faixa inválida')
        return
    vivos = []
    for ip in ips:
        ok = up(ip)
        print(f'{ip} -', 'UP' if ok else 'DOWN')
        if ok:
            vivos.append(ip)
    print('\nAtivos:', len(vivos))
    with open('hosts_ativos.txt', 'w', encoding='utf-8') as f:
        for h in vivos:
            f.write(h + '\n')


if __name__ == '__main__':
    main()
