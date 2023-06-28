#!/usr/bin/python3

import socket
import threading 

def send_msg():
	while True:
		msg = input().encode()
		client.send(msg)

def recv_msg():
	while True:
		recived = client.recv(1024)
		print(recived.decode())
    

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind("127.0.0.1",8888)
print("Listeniing......")
s.listen(1)
client.addr = s.accept()
print()
print("connected.....")

t1 = threading.Thread(target=send_msg)
t1.start()
recv_msg()