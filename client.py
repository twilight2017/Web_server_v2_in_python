import socket

# create a socket and connect to a server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
sock.connect(('localhost', 8888))

# send and receive some data
sock.sendall(b'test')
data = sock.recv(1024)
print(data.decode())