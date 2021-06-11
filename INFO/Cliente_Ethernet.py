# %%
'''
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.100.208",2021))
print("Se conecto al servidor")
s.close()
print("Fin del Programa")
'''

# %%
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.100.208",2021))
fin=True
while fin:
    a=input("Digitar un texto a enviar: ")
    if a=="Fin":
        fin=False
    b=a.encode()
    s.send(b)
    mensaje=s.recv(64)
    print("Mensaje del servidor: ",mensaje)
s.close()
print("Fin del Programa")

