# date = 24-11-2021

import socket

host = socket.gethostname()
port = 9337 # CHANGE THIS

#connect with IPv4 and TCP connection
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen(1)

print("\nServer started...\n")

conn,addr = sock.accept()

print("Connection established with:",str(addr))
#send message
message = "Hello thanks for connecting "+str(addr)+"\n"
conn.send(message.encode("ascii"))
while 1:
  data = input("server >>")
  if len(data)==0:break
  message = data.encode("ascii")
  conn.send(message)

conn.close()
