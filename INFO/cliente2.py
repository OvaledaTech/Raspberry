import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.14", 2021))
x = True
while x:
    a = input("Digite un texto a enviar: ")
    if a == "Fin":
        x = False
    b = a.encode()
    s.send(b)
    mensaje = s.recv(64)
    c = mensaje.decode()
    print("Mensaje del servidor: ", c)
s.close()
print("Fin del programa")
