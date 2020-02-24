'''minimal flask app'''

from flask import Flask, render_template

# Make th application
app = Flask(__name__)

# Make the route w/ a decorator
@app.route("/")

# Define a fn
def hello():
    return render_template("home.html")

#make a second route
@app.route("/about")

# Make a fn that goes with about
def preds():
    return render_template("about.html")