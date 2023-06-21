#!/usr/bin/python3

import socket
import threading


def send_msg():
	while True:

		msg =input().encode()
		s.send(msg)

def recv_msg():
	while True:
		recevied = s.recv(1024)
		print(recevied.decode())


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("connecting..")
while True:
	try:
		s.connect("127.0.0.1",8888)
		break
	except CoonectionRefusedError:
		continue

print("connected....")		

t1 = threading.Thread(target=send_msg)
t1.start()
recv_msg()
