import socket

SOCK_BUFFER = 1024
n = 5

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("127.0.0.1", 5000)

print(f"Conectando a servidor -> {server_address[0]}, puerto -> {server_address[1]}")

sock.connect(server_address)

try:
    sock.sendall(str(n).encode("utf-8"))
    data = sock.recv(SOCK_BUFFER)
except Exception as e:
    print(f"Excepcion: {e}")
finally:
    print("Cierro conexion")
    sock.close()
    
res = int(data.decode('utf-8'))
print(res)
