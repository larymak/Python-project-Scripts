import multiprocessing.util
import socket
from perspective import resolve_image
from sudoku import Grid
import argparse
import multiprocessing
import os

temp_result_file = "resultfile.png"
temp_input_file = "tempfile.jpg"

def process_handle_transaction(proc_num:int, sock:socket.socket):
    print(f"[{proc_num}] Waiting for client...")
    sock2, address2 = sock.accept()
    print(f"[{proc_num}] Connected to client with address: {address2}")
    sock2.settimeout(1)
    rec_buf = b''
    split = temp_input_file.split('.')
    my_temp_input_file = ".".join(i for i in split[:-1]) + str(proc_num) + "." + split[-1]
    split = temp_result_file.split('.')
    my_temp_result_file = ".".join(i for i in split[:-1]) + str(proc_num) + "." + split[-1]
    try:
        while True:
            try:
                rec = sock2.recv(1)
                rec_buf += rec
                if len(rec) == 0:
                    print(f"[{proc_num}] Lost connection")
                    break
            except socket.timeout:
                with open(my_temp_input_file, "wb") as f:
                    f.write(rec_buf)
                rec_buf = b''
                grid_size, points = resolve_image(my_temp_input_file)
                grid = Grid(rows=grid_size[0], columns=grid_size[1])
                assignment_values = {}
                for val,loc in points:
                    assignment_values[loc] = val
                grid.preassign(assignment_values)
                grid.solve()
                grid.save_grid_image(path=my_temp_result_file, size=(400,400))
                with open(my_temp_result_file, "rb") as f:
                    sock2.send(f.read())
                os.remove(my_temp_input_file)
                os.remove(my_temp_result_file)
                sock2.close()
                print(f"[{proc_num}] Finished!")
                break
    finally:
        sock2.close()

class Manager():
    def __init__(self, address:tuple[str,int]):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = address
    
    def wait_for_connect(self):
        print("Waiting for client...")
        self.sock2, self.address2 = self.sock.accept()
        print(f"Connected to client with address: {self.address2}")
        self.sock2.settimeout(1)
    
    def run(self):
        self.sock.bind(self.address)
        self.sock.listen()
        print(f"Listening from address: {self.address}")
        try:
            while True:
                self.wait_for_connect()
                rec_buf = b''
                while True:
                    try:
                        rec = self.sock2.recv(1)
                        rec_buf += rec
                        if len(rec) == 0:
                            print("Lost connection")
                            break
                    except socket.timeout:
                        with open(temp_input_file, "wb") as f:
                            f.write(rec_buf)
                        rec_buf = b''
                        grid_size, points = resolve_image(temp_input_file)
                        grid = Grid(rows=grid_size[0], columns=grid_size[1])
                        assignment_values = {}
                        for val,loc in points:
                            assignment_values[loc] = val
                        grid.preassign(assignment_values)
                        grid.solve()
                        grid.save_grid_image(path=temp_result_file, size=(400,400))
                        with open(temp_result_file, "rb") as f:
                            self.sock2.send(f.read())
                        os.remove(temp_input_file)
                        os.remove(temp_result_file)
                        self.sock2.close()
                        break
        finally:
            try:
                self.sock2.close()
            except socket.error:
                pass
            except AttributeError:
                pass
            self.sock.close()
    
    def run_multiprocessing(self, max_clients:int=8):
        self.sock.bind(self.address)
        self.sock.listen()
        print(f"Listening from address: {self.address}")
        processes:dict[int,multiprocessing.Process]= {}
        proc_num = 0
        try:
            while True:
                if len(processes) <= max_clients:
                    proc = multiprocessing.Process(target=process_handle_transaction, args=(proc_num, self.sock))
                    proc.start()
                    processes[proc_num] = proc
                    proc_num += 1
                    proc_num%=(max_clients*2)
                keys = list(processes.keys())
                for proc_n in keys:
                    if not processes[proc_n].is_alive():
                        processes.pop(proc_n)
        finally:
            if len(processes):
                for proc in processes.values():
                    proc.kill()
            self.sock.close()

if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=3535, help="The port to host the server.")
    parser.add_argument("--host", type=str, default="localhost", help="The host or ip-address to host the server.")
    args = parser.parse_args()
    address = (args.host, args.port)
    manager = Manager(address)
    manager.run_multiprocessing(max_clients=multiprocessing.cpu_count())