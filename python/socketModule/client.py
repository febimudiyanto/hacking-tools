#date = 24-11-2021

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(),9337))
msg = sock.recv(1024) 
sock.close()
print(msg.decode("ascii"))

