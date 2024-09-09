from flask import Flask, render_template, redirect, url_for, request, flash, session
from werkzeug.utils import secure_filename
import os
from random import choices, choice
from string import ascii_letters, digits
from time import sleep
from datetime import datetime
import socket

app = Flask(__name__)

app.config.from_pyfile("config.cfg")

def manage_solution(input_file, result_file) -> int:
    def send(input_file:str, sock:socket.socket) -> int:
        try:
            with open(input_file, "rb") as f:
                sock.send(f.read())
            return 1
        except FileNotFoundError:
            return -2
        except socket.error:
            return -1
    
    def connect() -> socket.socket:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((app.config['SOLVER_IP'], int(app.config['SOLVER_PORT'])))
        sock.settimeout(10)
        return sock
    
    def manage_full_send(input_file:str, sock:socket.socket):
        tries = 0
        while tries < 5:
            send_state = send(input_file, sock)
            if send_state == 1:
                break
            elif send_state == -2:
                return -2
            elif send_state == -1:
                sock = connect()
            tries += 1
        return send_state
    
    sock = connect()
    send_state = manage_full_send(input_file, sock)
    if send_state == -1:
        return -1
    elif send_state == -2:
        return -2
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
        return 0

@app.route('/', methods=['POST', 'GET'])
def index():
    if "POST" == request.method:
        print(request)
        if 'image' not in request.files:
            flash('No file part.', "danger")
        else:
            file = request.files['image']
            if '' == file.filename:
                flash("No file selected.", "danger")
            else:
                ext = "." + file.filename.split('.')[-1]
                filename = datetime.now().strftime("%d%m%y%H%M%S") + "_" + "".join(i for i in choices(ascii_letters+digits, k=3)) + ext
                filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                print(filename)
                file.save(filename)
                session['filename'] = filename
                return redirect(url_for('result'))
    else:
        if session.get('solved'):
            session.pop('solved')
        if session.get('filename'):
            try:
                os.remove(session['filename'])
                session.pop('filename')
            except FileNotFoundError:
                pass
    return render_template('index.html', request=request)

@app.route('/result', methods=['GET'])
def result():
    if not session.get('solved'):
        filename = session.get('filename')
        if not filename:
            return redirect(url_for('/'))
        solution = ""
        result_file = ".".join(i for i in filename.split(".")[:-1]) + "_sol.png"
        result_file = result_file.split("/")[-1]
        full_result_file = "static/" + result_file
        result_file = f"../static/{result_file}"
        result = manage_solution(filename, full_result_file)
        os.remove(session['filename'])
        if result == 0:
            session['filename'] = full_result_file
            print("solved")
            solution = result_file
            session['solved'] = solution
        else:
            session.pop('filename')
            flash(f"There was an issue, Error {result}", "danger")
            redirect(url_for('/'))
    else:
        solution = session['solved']
    return render_template('result.html', img=solution)

if "__main__" == __name__:
    app.run(
        host="192.168.1.88",
        port=5000,
        debug=True
    )