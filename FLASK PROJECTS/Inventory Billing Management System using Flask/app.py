from flask import Flask, render_template, request, redirect, abort, flash, session ,url_for
from werkzeug.exceptions import HTTPException
from firebase import Firebase
import json
from datetime import datetime
from db import products_collection, invoices_collection, users_collection
from helper import *
import os

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET']

config = {
  "apiKey": os.environ.get("FIREBASE_APIKEY"),
  "authDomain": os.environ.get("FIREBASE_AUTHDOMAIN"),
  "databaseURL": os.environ.get("FIREBASE_DATABASEURL"),
  "projectId": os.environ.get("FIREBASE_PROJECT_ID"),
  "storageBucket": os.environ.get("FIREBASE_STORAGE_BUCKET"),
  "messagingSenderId": os.environ.get("FIREBASE_MESSAGING_SENDER_ID"),
  "appId": os.environ.get("FIREBASE_APP_ID"),
  "measurementId": os.environ.get("FIREBASE_MEASUREMENT_ID")
  }

firebase = Firebase(config)
db = firebase.database()
auth = firebase.auth()

exempted_endpoints = ['signup','login','static']

@app.route("/signup", methods = ['GET','POST'])
def signup():
    if request.method=='POST':
        name = request.form.get("name")
        username = request.form.get("email")
        password = request.form.get("password")
        repassword = request.form.get("repassword")
        user_details = {"name": name,"email": username}
        if password == repassword:
            if len(password)>=6:
                try:
                    _user_ = auth.create_user_with_email_and_password(username ,password)
                    auth.send_email_verification(_user_['idToken'])
                    user_details['merchant_id'] = _user_['localId']
                    users_collection.insert_one(user_details)
                    return render_template("success.html")
                except Exception as e:
                    return redirect(url_for('login'))
            else:
                flash('Password is less than 6 characters!')
                return redirect("/signup")
        else:
            flash('Both Passwords do not match!')
            return redirect("/signup")
    return render_template("signup.html")

@app.route("/login",methods = ['GET','POST'] )
def login():
    if request.method == 'POST':
        data = dict(request.form)
        email = data.get("email")
        password = data.get("password")
        user_details = users_collection.find_one({"email": email},{"_id": 0})
        if user_details:
            user = auth.sign_in_with_email_and_password(email ,password)
            access_token = user['idToken']
            acc_info = auth.get_account_info(access_token)
            print(acc_info)
            if not acc_info.get("users")[0].get("emailVerified"):
                abort(500,{"message": f"{email} is not verified!"})
            user_details = users_collection.find_one({"email": email, "merchant_id": user['localId']},{"_id": 0})
            if user_details:
                session['user'] = user['localId']
                return redirect("/")     
            else:
                abort(500,{"message": "Username or Password is Invalid!!"})

        else:
            flash("User doesn't exist!")
            return redirect("/login")
    if 'user' in session:
        return redirect("/")
    return render_template("login.html")

    
@app.route("/",methods = ['GET','POST'])
def start():
    products = list(products_collection.find({"merchant_id": session.get('user')},{"_id":0,"created_on": 0}))
    return render_template("index.html",_products_=json.dumps(products))

@app.route("/checkout",methods = ['POST'])
def checkout():
    bill_data = dict(request.form)
    dt_string = datetime.now()
    bill_data['created_on'] = dt_string
    bill_data['merchant_id'] = session.get('user')
    bill_data['selected_products'] = json.loads(bill_data['selected_products'])
    unavailable_items = []
    for product in bill_data['selected_products']:
        item_id = product['item_id']
        qty = int(product['qty'])
        product_details = products_collection.find_one({"merchant_id": session.get('user'),"item_id": item_id})
        current_stock = product_details.get("item_stock")
        item_name = product_details.get("name")
        if int(current_stock)<=int(qty):
            unavailable_items.append(item_name)
    if unavailable_items == []:
        for product in bill_data['selected_products']:
            item_id = product['item_id']
            qty = int(product['qty'])
            products_collection.update_one({"merchant_id":session.get('user'),"item_id":item_id},{"$inc":{"item_stock": -qty}})
    # return bill_data
        bill_id = random_id(10)
        if bill_data.get("payment_status") == "paid":
            bill_data['amount_to_be_collected'] = "0"
        bill_data['bill_id'] = bill_id
        invoices_collection.insert_one(bill_data)
        return redirect(f"/bill/{bill_id}")
    else:
        for item in unavailable_items:
            flash(f"{item} is out of stock!")
        return redirect("/")

@app.route("/bill/<string:bill_key>", methods=['GET','POST'])
def bill(bill_key):
    if request.method == 'POST':
        incoming_updates = dict(request.form)
        if incoming_updates['payment_status'] == 'paid':
            incoming_updates['amount_to_be_collected'] = "0"
            incoming_updates['paid_amount'] = incoming_updates['checkout_amount'].replace(",",'')
        elif incoming_updates['payment_status'] == 'unpaid':
            incoming_updates['amount_to_be_collected'] = incoming_updates['checkout_amount'].replace(",",'')
            incoming_updates['paid_amount'] = "0"
        invoices_collection.update_one({"merchant_id":session.get('user'),"bill_id": bill_key},{"$set":incoming_updates})
        return redirect(f"/bill/{bill_key}")
    try:
        bill_details = invoices_collection.find_one({"merchant_id": session.get('user'),"bill_id": bill_key},{"_id":0,"created_on": 0})
    except:
        bill_details = None
    if bill_details is not None:
        return render_template("bill.html",bill_key=bill_key, bill_details=json.dumps(bill_details),bill_details_json=bill_details)
    else:
        abort(404,
      {
           "message": f"Bill with Bill ID '{bill_key}' doesn't exist"
      })

@app.route("/products", methods = ['GET','POST'])
def products():
    if request.method == 'POST':
        item_data = dict(request.form)
        item_data['item_stock'] = int(item_data['item_stock'])
        dt_string = datetime.now()
        item_data['created_on'] = dt_string
        item_data['merchant_id'] = session.get('user')
        item_data['item_id'] = random_id(10)
        products_collection.insert_one(item_data)
        return redirect("/products/0")
    return redirect('/products/0')

@app.route("/products/<int:page_index>", methods = ['GET','POST'])
def products_idx(page_index):
    if request.method == "POST":
        query = request.form.get("search")
        page_size = 10
        pipeline = [{"$match":{"merchant_id": session.get('user')}},{"$project":{"_id":0}}]
        res= []
        products = list(products_collection.aggregate(pipeline))
        for product in products:
            if query in product.get("name").lower():
                res.append(product)
        return render_template("products.html",products=res,total_pages=0,page_size=page_size, page_index=0,merchant_id=session.get('user'), handle_catch=handle_catch)
    page_size = 10
    pipeline = [{"$match":{"merchant_id": session.get('user')}},{"$project":{"_id":0}},{'$skip':  int(page_index)*page_size}, {'$limit':  page_size}]
    products = products_collection.aggregate(pipeline)
    temp = len(list(products_collection.find({"merchant_id":session.get("user")},{"_id":0})))
    if temp%page_size == 0:
        total_pages = temp//page_size
    else:
        total_pages = temp//page_size + 1

    return render_template("products.html",products=products,total_pages=total_pages,page_size=page_size, page_index=page_index,merchant_id=session.get('user'), handle_catch=handle_catch)

@app.route("/products/<string:merchant_id>/<string:item_id>/<string:page_index>", methods = ['POST'])
def products_update(merchant_id, item_id,page_index):
    item_data = dict(request.form)
    item_data['item_stock'] = int(item_data['item_stock'] )
    products_collection.update_one({"item_id": item_id,"merchant_id": merchant_id},{"$set":item_data})
    return redirect(f"/products/{page_index}")

@app.route("/products_delete/<string:merchant_id>/<string:item_id>/<string:page_index>", methods = ['POST'])
def products_delete(merchant_id, item_id,page_index):
    products_collection.delete_one({"item_id": item_id,"merchant_id": merchant_id})
    return redirect(f"/products/{page_index}")

@app.route("/bills", methods = ['GET','POST'])
def bills_temp():
    return redirect("/bills/0")

@app.route("/bills/<int:page_index>", methods = ['GET','POST'])
def bills(page_index):
    if request.method == "POST":
        payment_status_filter = str(request.form.get("payment_status"))
        page_size = 10
        if payment_status_filter!="":
            pipeline = [{"$match":{"merchant_id": session.get('user'),"payment_status":payment_status_filter}},{"$project":{"_id":0}}]
        else:
            return redirect("/bills/0")
        all_bills = list(invoices_collection.aggregate(pipeline))
        return render_template("bills.html",all_bills=all_bills,total_pages=0,page_size=page_size, page_index=0,merchant_id=session.get('user'), handle_catch=handle_catch)
    page_size = 10
    pipeline = [{"$match":{"merchant_id": session.get('user')}},{"$project":{"_id":0}},{'$skip':  int(page_index)*page_size}, {'$limit':  page_size}]
    all_bills = invoices_collection.aggregate(pipeline)
    temp = len(list(invoices_collection.find({"merchant_id":session.get("user")},{"_id":0})))
    if temp%page_size == 0:
        total_pages = temp//page_size 
    else:
        total_pages = temp//page_size +1
        
    # all_bills = invoices_collection.find({"merchant_id":session.get('user')},{"_id":0})
    return render_template("bills.html", all_bills=all_bills,total_pages=total_pages,page_index=page_index, page_size=page_size,handle_catch=handle_catch)

@app.route("/logout", methods = ['GET','POST'])
def logout():
    session.pop('user')
    return redirect("/login")

@app.before_request
def before_request_func():
    if request.endpoint in exempted_endpoints:
        return 
    if 'user' not in session:
        return redirect(url_for('login'))
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)