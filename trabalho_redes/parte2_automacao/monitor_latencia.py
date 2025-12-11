import socket
import sys
import time


def measure(host, port=80, attempts=5, timeout=1.0):
    lat = []
    fail = 0
    for _ in range(attempts):
        s = socket.socket()
        s.settimeout(timeout)
        t0 = time.time()
        try:
            s.connect((host, port))
            s.close()
            lat.append((time.time() - t0) * 1000)
        except Exception:
            fail += 1
        time.sleep(0.1)
    return lat, fail


def main():
    if len(sys.argv) < 2:
        print('Uso: python monitor_latencia.py <host> [port] [attempts]')
        return
    host = sys.argv[1]
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 80
    attempts = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    lat, fail = measure(host, port, attempts)
    total = attempts
    avg = sum(lat) / len(lat) if lat else 0
    mx = max(lat) if lat else 0
    loss = (fail / total) * 100
    print(f'Host: {host}:{port}')
    print(f'Tentativas: {total}')
    print(f'Latência média: {avg:.1f} ms')
    print(f'Latência máxima: {mx:.1f} ms')
    print(f'Perda: {loss:.1f}% ({fail} de {total})')


if __name__ == '__main__':
    main()
