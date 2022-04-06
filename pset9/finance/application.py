import os
import datetime
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd, apology1

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Get user id
    user_id = session["user_id"]

    # Look for the cash left in the user's account
    cash = db.execute('SELECT cash  FROM users WHERE id=?', user_id)
    cashLeft = cash[0]["cash"]

    # Query database of all transactions for logged user
    indexTable = db.execute('SELECT stockSymbol AS Symbol, stockName AS Name, SUM( boughtShares) Shares, boughtPrice AS Price, SUM(totalPrice) AS Total  FROM transactions WHERE user_id=? GROUP BY stockSymbol', user_id)

    sumTotal = db.execute('SELECT SUM(totalPrice) FROM transactions WHERE user_id=?', user_id)
    total = sumTotal[0]["SUM(totalPrice)"]

    if  not total:
        return render_template("index.html", rows=indexTable, cash=cashLeft, total=cashLeft)



    else:

        # Return index page listing all stocks
        return render_template("index.html", rows=indexTable, cash=cashLeft, total=float(total) + cashLeft)




@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # If user requests for the buy page
    if request.method == "GET":
        return render_template("buy.html")

    # Else if user submits the data
    else:

        # Extract the data about the stock from the form submitted
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Lookup for stock information
        stockInfo =  lookup(symbol)

        # Name, price of the stock
        stockName = stockInfo["name"]
        currentPrice = stockInfo["price"]

        # Totalcash, user_id of the user
        user_id = session["user_id"]
        cash = db.execute('SELECT cash FROM users WHERE id=?', user_id)

        # Current cash before buy
        totalCash = cash[0]["cash"]

        # Total bill for the purchase
        totalPrice = int(shares)*currentPrice

        # Cash will left after bought
        cashLeft = totalCash - totalPrice

        # CurrentTime
        currentTime = datetime.datetime.now()

        # If stockInfo not available
        if not stockInfo:
            return apology1("Oops! Symbol doesn't exists.")

        # Check if user can afford the stock
        if totalCash >= totalPrice:

            # Insert bought shares into user's account
            db.execute("INSERT INTO transactions (user_id, stockSymbol, stockName, boughtShares, boughtPrice, transactionTime, totalPrice) VALUES (?, ?, ?, ?, ?, ?, ?)", user_id, str(symbol).upper(), stockName, shares, currentPrice, currentTime, totalPrice)

            # Update the cash left
            db.execute("UPDATE users SET cash = ? WHERE id = ?",(cashLeft, user_id))

            flash("Bought!")

            # Redirect the user to show index table
            return redirect("/")

        # Else if user cannot afford
        else:

            # Apology
            return apology1("You do not hold an enough amount!")




@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # If the user wants a quote
    if request.method == "GET":

        # Displays a form to get a quote
        return render_template("quote.html")

    # Else if user submits a form
    elif request.method == "POST":

        # Extract the user input
        symbol = request.form.get("symbol")

        # Stock information
        stockInfo = lookup(symbol)

        # If no stock available
        if not stockInfo:

            # Return apology
            return apology1("Oops! The symbol doesn't exists.")

        # Quote the stock information
        return render_template("quoted.html", name=stockInfo["name"], price=stockInfo["price"], symbol=stockInfo["symbol"] )


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # If user submits the form to register
    if request.method == "POST":

        # Extract user's information
        username = request.form.get("username")
        password = request.form.get("password")

        # Query database to look for the same username
        rows = db.execute("SELECT * FROM users")

        # Look for the same username
        for row in rows:

            # Ensure username doesn't exists
            if username == row["username"]:

                # if the same username exists return apology
                return apology1("Username already exists.")

        # Generate password hash
        passwordHash = generate_password_hash(password)

        # Query database to insert a user
        db.execute("INSERT INTO users (username , hash) VALUES(:username, :hash)", username=username , hash=passwordHash)

        flash("Registered!")

        # redirect user to the homepage
        return redirect("/")

    # Else if user wants to register
    else:

        # Render a form to fill
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # If user wants to sell the stock
    if request.method == "GET":

        # Render a form to sell
        rows = db.execute("SELECT stockSymbol FROM transactions WHERE user_id=? GROUP BY stockSymbol", session["user_id"])
        return render_template("sell.html", rows=rows)
    else:

        # Extract user's input
        selected = request.form.get("selected")
        shares = request.form.get("shares")

        # CurrentTime
        currentTime = datetime.datetime.now()

        # Lookup Stock information
        stockInfo = lookup(selected)
        currentPrice = stockInfo["price"]
        stockSymbol = stockInfo["symbol"]
        stockName = stockInfo["name"]

        # Remember user_id
        user_id = session["user_id"]

        # Check the left in user's account
        cashLeft = db.execute('SELECT  cash FROM  users WHERE id=?', user_id)
        totalCash = cashLeft[0]["cash"]
        sharesHolding = db.execute('SELECT SUM( boughtShares) FROM transactions WHERE user_id=? GROUP BY stockSymbol HAVING stockSymbol=?', user_id, selected)
        holdings = sharesHolding[0]["SUM( boughtShares)"]
        db.execute('UPDATE transactions SET boughtShares = ? WHERE stockSymbol=?', (int(holdings)- int(shares)),selected )

        db.execute('INSERT INTO soldtransactions (user_id, stockSymbol, stockName, soldShares, soldPrice, totalPrice, transactionTime) VALUES (?, ?, ?, ?, ?, ?, ?)', user_id, stockSymbol, stockName, ("-"+ shares), currentPrice, (currentPrice*int(shares)), currentTime)
        db.execute('UPDATE users SET cash=? WHERE id=?', (totalCash+currentPrice), user_id)
        # Query database of all transactions for logged user
        indexTable = db.execute('SELECT stockSymbol AS Symbol, stockName AS Name, SUM( boughtShares) Shares, boughtPrice AS Price, SUM(totalPrice) AS Total  FROM transactions WHERE user_id=? GROUP BY stockSymbol', user_id)
        # for row in indextable:
        #     if stockSymbol == indextable["Symbol"]:

                #db.execute('UPDATE transactions SET  boughtShares=? WHERE user_id=? HAVING stockSymbol=?(', )
        flash("Sold!")
        return redirect("/")
    # return apology("TODO")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
