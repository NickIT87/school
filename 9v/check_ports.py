import socket

def check_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex(('127.0.0.1', port))
    sock.close()
    return result == 0

available_ports = []
for port in range(1, 65536):
    if check_port(port):
        available_ports.append(port)

print("Available ports:", available_ports)

