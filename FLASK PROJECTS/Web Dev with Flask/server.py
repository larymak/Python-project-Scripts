# @author deepak sai pendyala
import csv
from flask import Flask,render_template,url_for,redirect,request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_database(data):
    with open('./Portfo/database.txt',mode='a')as database:
        name=data["name"]
        email=data["email"]
        message=data['message']
        file=database.write(f'\n {name},{email},{message}')

def write_to_csv(data):
    with open('./Portfo/database.csv',mode='a',newline='')as database2:
        name=data["name"]
        email=data["email"]
        message=data['message']
        csv_witer=csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_witer.writerow([name,email,message])


@app.route('/submit_form',methods=['POST','GET'])
def Sumbit_form():
    if request.method=='POST':
        try:
            data=request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'didnt save to database'
    else:
        return 'woops,Something went wrong'


# set FLASK_APP=server.py
# $env:FLASK_APP = "server.py"
#python -m flask run 

#$env:FLASK_ENV = "development"
#python -m flask run 
