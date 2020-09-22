# %%
'''
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.100.208", 2021))
s.listen(5)
print("Esperando un cliente:")
(sc, addrC) = s.accept()
print("Se conecto el cliente")
print("IP del Cliente:", addrC)
sc.close()
s.close()
print("Fin del Programa")

'''
# %%
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.100.208", 2021))
s.listen(5)
print("Esperando un cliente:")
(sc, addrC) = s.accept()
print("IP del Cliente:", addrC)
while True:
    mensaje = sc.recv(64)  # recibimos 64 bytes
    men2 = mensaje.decode()
    print("Mensaje: ", men2)
    men = "Mensaje Recibido"
    sc.send(men.encode())

print("Fin del Programa")


# %%
