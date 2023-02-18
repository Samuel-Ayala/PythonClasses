#----Ejercicio 1----#
#Crear un programa cliente que envie los datos de una maquina virtual a un servidor
#en una lista con la siguiente estructura: 
#["# de regiones donde esta replicada", "tipo de disco (HDD/SSD Estandar/SSD premium)"
#, "¿Tiene politica(s) de Backup? (SI/NO)", "¿Cuenta con Site Recovery? (SI/NO)"]. 
#Ejm: [2,HDD,SI,NO]. Por el lado del servidor se deben recibir los datos y evaluar el
#nivel de disponibilidad que presenta la VM. Luego, enviar un mensaje al cliente mencionando
#el nivel de disponibilidad. Ejm: "La maquina virtual tiene 99.9% de disponibilidad"
#La evaluacion de la disponibilidad se debe realizar tomando en cuenta la siguiente informacion:
#
#95% de disponibilidad cuando la VM cuenta con disco HDD
#98% de disponibilidad cuando la VM cuenta con disco SSD estandar
#99% de disponibilidad cuando la VM cuenta con disco SSD premium
#Si la VM tiene backup: +0.9%
#Si la VM esta replicada en 2 o mas regiones: +0.09%
#Si la VM tiene site recovery: +0.009%
# 
#Ejm: Si la VM tiene disco SSD Premium, tiene politica de Backup y esta replicada en 3 regiones
#entonces su disponibilidad sera de 99 + 0.9 + 0.09 = 99.99%

#Cliente
import socket
import pickle

SOCK_BUFFER = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("192.168.1.37", 5005)

print(f"Conectando a servidor -> {server_address[0]}, puerto -> {server_address[1]}")
sock.connect(server_address)

datos = [2,"SSD estandar","SI","NO"]
datos_empaquetados = pickle.dumps(datos)

try:
    sock.sendall(datos_empaquetados)
    data = sock.recv(SOCK_BUFFER)
except Exception as e:
    print(f"Excepcion: {e}")
finally:
    print("Cierre de conexion")
    sock.close()

res = data.decode()
print(res)




















