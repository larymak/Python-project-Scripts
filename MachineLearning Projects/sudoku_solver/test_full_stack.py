import socket

result_file = "resultfile2_server.png"
input_file = "f1.jpg"

def main(address:tuple[str,int]):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    sock.settimeout(10)
    with open(input_file, "rb") as f:
        sock.send(f.read())
    res_buf = b''
    try:
        while True:
            try:
                res = sock.recv(1)
                res_buf += res
                if 0 == len(res):
                    sock.close()
                    with open(result_file, "wb") as f:
                        f.write(res_buf)
                    break
            except socket.timeout:
                with open(result_file, "wb") as f:
                    f.write(res_buf)
                break
    finally:
        sock.close()

if "__main__" == __name__:
    main(("localhost", 3535))