import socket

SOCK_BUFFER = 1024

def exp(n):
    res = 1
    for i in range(n):
        res *= n
    return res

if __name__ == "__main__":
    #creamos el socket
    #AF_INET -> el formato del socket es direccion IPv4 mas numero de puerto
    #SOCK_STREAM -> el protocolo de transporte empleado es TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #puertos reservados: del 0 al 1023
    server_address = ("127.0.0.1", 5000)
    print(f"Iniciando servidor en direccion -> {server_address[0]}, puerto -> {server_address[1]}")
    sock.bind(server_address)

    sock.listen(1)

    while True:
        print("Esperando conexiones")
        conn, client_address = sock.accept()
        try:
            data = conn.recv(SOCK_BUFFER)
            if data:
                res = exp(int(data.decode("utf-8")))
                print(f"Recibimos {int(data)}, retornamos {res}")
                conn.sendall(str(res).encode("utf-8"))
        except Exception as e:
            print(f"Excepcion: {e}")
        finally:
            print("Cliente cerro la conexion")
            conn.close()