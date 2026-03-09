import socket

s=socket.socket()
result = s.connect_ex(("google.com", 80))

if result == 0:
    print("port is open")
else:
    print("port is not open")