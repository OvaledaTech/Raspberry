import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.100.206", 2021))
print("Se conecto al servidor")
s.close()
print("Fin del Programa")
