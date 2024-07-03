import os

from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import current_user
from cs50 import SQL
import sqlite3
import re

from helpers import apology, login_required, usd


# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///library.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


""" user authentication routes """


# Forms
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("Please provide a username.", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("Please provide a password.", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")
    else:
        return render_template("login.html")


# register
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id.
    session.clear()

    if request.method == "POST":
        # Get user name and password.
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Validate user input.
        if not username:
            return apology("must provide username", 400)

        elif not password:
            return apology("must provide password", 400)

        elif not confirmation:
            return apology("must confirm password", 400)

        elif password != confirmation:
            return apology("must confirm password", 400)

        # Query the database to check if the username is already taken.
        existing_user = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(existing_user) != 0:
            return apology("userename taken", 400)

        # Generate a hash of the password.
        hashed_password = generate_password_hash(password)

        # Insert the new user into the database.
        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)",
            username,
            hashed_password,
        )

        # Query the database for newly inserted user.
        new_user = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Remember user.
        session["user_id"] = new_user[0]["id"]

        # Display success message.
        flash("Registration successful.", "success")
        return redirect("/")
    else:
        return render_template("register.html")


# logout
@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()
    # Redirect user to login form
    return redirect("/")


# delete
@app.route("/remove", methods=["GET", "POST"])
@login_required
def remove():
    """Delete user account"""
    if request.method == "POST":
        # Get user name and password.
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Validate user input.
        if not username:
            return apology("must provide username", 400)
        elif not password:
            return apology("must provide password", 400)
        elif not confirmation:
            return apology("must confirm password", 400)
        elif password != confirmation:
            return apology("passwords must match", 400)

        # Query the database to check if the username is already taken.
        existing_user = db.execute("SELECT * FROM users WHERE username = ?", username)
        if not existing_user:
            return apology("Wrong username", 403)
        else:
            # Get user id.
            user_id_data = db.execute(
                "SELECT id FROM users WHERE username = ?", (username,)
            )
            user_id = user_id_data[0]["id"]
            # Delete user's account and related data from the database.
            db.execute("DELETE FROM cart WHERE user_id = ?", (user_id,))
            db.execute("DELETE FROM users WHERE username = ?", (username,))
            # Display success message.
            flash("Account deleted successfully.", "success")
            session.clear()
            return redirect("/")
    else:
        return render_template("remove.html")


@app.route("/checkout", methods=["GET", "POST"])
@login_required
def checkout():
    """Check out"""

    if request.method == "POST":
        # Get the form data
        city = request.form.get("city")
        address = request.form.get("address")
        postal_code = request.form.get("postal_code")
        phone_number = request.form.get("phone_number")

        # Validate the form data
        if not city or not address or not postal_code or not phone_number:
            return apology("Please provide all required information.", 400)
        elif not postal_code.isdigit() or int(postal_code) <= 0:
            return apology(
                "Invalid postal code. Please provide a valid postal code.", 400
            )
        elif not phone_number.isdigit() or int(phone_number) <= 0:
            return apology(
                "Invalid phone number. Please provide a valid phone number.", 400
            )

        try:
            # Get the user's ID from the session
            user_id = session["user_id"]

            # Fetch the product id from the cart table based on the user_id
            rows = db.execute(
                "SELECT product_id FROM cart WHERE user_id = ?", (user_id,)
            )
            for row in rows:
                # Extract the product id from the row
                product_id = row["product_id"]
                # Insert the order into the database
                db.execute(
                    "INSERT INTO orders (user_id, city, address, postal_code, phone_number, product_id) VALUES (:user_id, :city, :address, :postal_code, :phone_number, :product_id)",
                    user_id=user_id,
                    city=city,
                    address=address,
                    postal_code=postal_code,
                    phone_number=phone_number,
                    product_id=product_id,
                )

                # Display success message.
                flash("Address saved successfully.", "success")
                return redirect("/cart")

        except Exception as e:
            # Log errors
            print("Error:", str(e))
            return apology("An error occurred while saving the address.", 500)

    else:
        # Render the check out template
        return render_template("checkout.html")


# Displaying routes
@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    """Display profile"""

    # Get the user's ID from the session
    user_id = session["user_id"]
    # Query the database for the user's data
    user_data = db.execute("SELECT * FROM users WHERE id = ?", user_id)
    # Query the database for the user's orders
    orders = db.execute(
        "SELECT address, city, postal_code, phone_number, history, id FROM orders WHERE user_id = ?",
        user_id,
    )
    # Query the database for the products in the user's cart
    items = db.execute(
        "SELECT products.price, cart.quantity FROM cart JOIN products ON cart.product_id = products.id WHERE cart.user_id = ?",
        user_id,
    )

    # Calculate the total amount for the items in the cart
    total_amount = 0
    for item in items:
        total_amount += item["price"] * item["quantity"]

    # Render the profile template with the user's data, orders, and total amount
    return render_template(
        "profile.html", user_data=user_data[0], orders=orders, total_amount=total_amount
    )


@app.route("/", methods=["GET", "POST"])
def index():
    """Display shop catalog"""

    #  Query the database for all products and supplies
    products = db.execute("SELECT * FROM products")

    # Renders them using the 'index.html' template.
    return render_template("index.html", products=products)



# cart and product details
@app.route("/productdetails/<int:id>", methods=["GET", "POST"])
def productdetails(id):
    """Display products details"""

    #  Query the database for the product details according to its id.
    details = db.execute("SELECT * FROM products WHERE id=?", (id,))
    # Print the product details to the console (for debugging purposes).
    print("Product:", details)
    # Renders them using the 'productdetails.html' template.
    return render_template("productdetails.html", details=details)


@app.route("/addtocart/<id>", methods=["GET", "POST"])
@login_required
def addtocart(id):
    """Adds products to the cart"""
    try:
        # Check if the request method is POST
        if request.method == "POST":
            # Get the quantity from the form.
            quantity = request.form.get("quantity")
            # Validate the quantity
            if not quantity:
                return apology("Must provide quantity", 400)
            elif not quantity.isdigit():
                return apology("invalid  number", 400)
            # Convert quantity into an int
            quantity = int(quantity)

            # Check if the quantity is less than 0
            if quantity <= 0:
                return apology("invalid number", 400)
            # Get the user's ID from the session
            user_id = session["user_id"]
            # Convert the poduct id into an int
            product_id = int(id)

            # Check if product exists
            product = db.execute("SELECT * FROM products WHERE id=?", (id,))
            if not product:
                return apology("product does not exist", 404)

            # Insert the product into the cart in the database
            db.execute(
                "INSERT INTO cart (user_id, product_id, quantity) VALUES (:user_id, :product_id, :quantity)",
                user_id=user_id,
                product_id=product_id,
                quantity=quantity,
            )
            # Display success message.
            flash("Added to cart!", "success")
    # Log errors
    except Exception as e:
        app.logger.error(f"Error in addtocart: {e}")
        return apology("an error occurred", 500)
    else:
        # Render the product details page
        return render_template("productdetails.html")


@app.route("/cart", methods=["GET", "POST"])
@login_required
def cart():
    """Display cart"""

    # Get the user's ID from the session
    user_id = session["user_id"]
    # Query the data base to get the data of the products in the user's cart
    query = """ SELECT p.id, p.name, p.price, p.availability, p.cover, c.quantity
    FROM products p
    INNER JOIN cart c ON p.id = c.product_id
    WHERE c.user_id = ?
    """
    # Execute the SQL query
    rows = db.execute(query, (user_id,))
    # Renders them using the 'cart.html' template.
    return render_template("cart.html", rows=rows)



