import socket
import pickle

SOCK_BUFFER = 1024

def procesamiento_de_datos(arreglo):
    disponibilidad = 0
    #Disco
    if (arreglo[1] == "HDD"):
        disponibilidad += 95
    elif (arreglo[1] == "SSD estandar"):
        disponibilidad += 98
    else:
        disponibilidad += 99
    
    #Backup
    if (arreglo[2] == "SI"):
        disponibilidad += 0.9
    
    #Replicacion
    if (arreglo[0] >= 2):
        disponibilidad += 0.09
    
    #Site Recovery
    if (arreglo[3] == "SI"):
        disponibilidad += 0.009
    
    return disponibilidad 

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_address = ("192.168.1.37",5005)
    print(f"Iniciando servidor en direccion -> {server_address[0]}, puerto -> {server_address[1]}")
    sock.bind(server_address)
    sock.listen(1)

    while True:
        print("Esperando conexiones")
        conn, client_address = sock.accept()
        try:
            data = conn.recv(SOCK_BUFFER)
            if data:
                arr = pickle.loads(data)
                dispo = procesamiento_de_datos(arr)
                msg = "La maquina virtual tiene " + str(dispo) +"%" + " de disponibilidad"
                conn.sendall(msg.encode())
        except Exception as e:
            print(f"Excepcion: {e}")
        finally:
            print("Cliente cerro la conexion")
            conn.close()





















