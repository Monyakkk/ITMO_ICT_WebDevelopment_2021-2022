import socket
soc = socket.socket()
soc.connect(('localhost',9090))
print("long base of trapezoid:")
a = input()
soc.send(a.encode())
print("short base of trapezoid:")
b = input()
soc.send(b.encode())
print("altitude of trapezoid:")
h = input()
soc.send(h.encode())
ans = soc.recv(1024)
ans = int(ans.decode('utf8'))
print("your anwser:")
print(ans/2)
soc.close()
