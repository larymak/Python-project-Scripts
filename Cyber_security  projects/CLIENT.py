#!/usr/bin/python3

import socket
import threading
import time

def send_msg(sock):
    while True:
        try:
            msg = input().encode('utf-8')  # Specify encoding
            sock.send(msg)
        except KeyboardInterrupt:
            print("Exiting gracefully")
            sock.close()
            break

def recv_msg(sock):
    while True:
        try:
            received = sock.recv(1024)
            print(received.decode('utf-8'))  # Specify decoding
        except ConnectionResetError:
            print("Server has closed the connection.")
            break

def connect_to_server(host, port, retries=5, delay=2):
    """Attempt to connect to the server with retries."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Connecting..")
    for attempt in range(retries):
        try:
            s.connect((host, port))
            print("Connected!")
            return s
        except socket.error as e:
            print(f"Connection attempt {attempt+1}/{retries} failed: {e}")
            time.sleep(delay)
    print("Could not connect to the server.")
    return None

host = "127.0.0.1"
port = 8888

s = connect_to_server(host, port)
if s:
    t1 = threading.Thread(target=send_msg, args=(s,))
    t1.start()

    try:
        recv_msg(s)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        s.close()
