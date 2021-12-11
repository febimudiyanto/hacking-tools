#date = 24-11-2021
import socket
import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(),9337))
print("connect with ",socket.gethostname())
while 1:
    msg = sock.recv(1024) 
    if not msg:break
    now = datetime.datetime.now()
    print("["+now.strftime('%Y-%m-%d %H:%M:%S')+"] ",msg.decode("ascii"))
sock.close()
