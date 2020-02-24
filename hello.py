'''minimal flask app'''

from flask import Flask

# Make th application
app = Flask(__name__)

# Make the route w/ a decorator
@app.route("/")

# Define a fn
def hello():
    return "Hello World!"