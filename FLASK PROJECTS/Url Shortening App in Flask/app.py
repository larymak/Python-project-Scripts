from flask import Flask, request, render_template, redirect, flash
from helpers import random_string_generator, random_string_generator_only_alpha, is_valid_url
from db import url_data_collection
import os
from datetime import datetime


app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET']

url_ = os.environ['APP_URL']

reserved_keywords = ['login', 'logout', 'shorten-url']


@app.route("/", methods = ['GET'])
def start():
    return render_template("index.html")

@app.route("/shorten-url", methods=['POST'])
def shorten_url():
    data = request.form
    url_input = data.get("url_input")
    data_id = random_string_generator_only_alpha(10)
    if not is_valid_url(str(url_input)):
        flash({'type':'error', 'data':"Inavlid URL"})
        return redirect("/")
    random_slug = random_string_generator(7)
    shortened_url = f"{url_}/{random_slug}"
    shortened_url_ = shortened_url[len(url_)+1:]
    if shortened_url == url_input:
        flash({'type':'error', 'data':"Infinite Redirect Error!"})
        return redirect("/")
    first_keyword = shortened_url_.split("/")[0]
    if first_keyword in reserved_keywords:
        flash({'type':'error', 'data':f"{first_keyword} is a reserved keyword! Please use any other word!"})
        return redirect("/")
    incoming_data = {
        "no_of_/": shortened_url_.count("/"),
        "order": shortened_url_.split("/"),
        "redirect_url": url_input,
        "shortened_url": shortened_url,
        "data_id": data_id,
        "created_at": datetime.now()
    }
    if url_details := url_data_collection.find_one({"no_of_/": incoming_data['no_of_/'], "order":incoming_data['order']}):
        flash({'type':'error', 'data':"This Domain is Already Taken!"})
        return redirect("/")
    url_data_collection.insert_one(incoming_data)
    flash({'type':'data', 'data':shortened_url})
    return redirect("/")


@app.before_request
def before_request_func():
    host_url = request.host_url
    url = request.url
    url = url[len(host_url):]
    incoming_data = {
        "no_of_/":url.count("/"),
        "order":url.split("/")
    }
    if url_details := url_data_collection.find_one({"no_of_/": incoming_data['no_of_/'], "order":incoming_data['order']}):
        redirect_url = url_details.get("redirect_url")
        return redirect(redirect_url)
