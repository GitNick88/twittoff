''' Code for our app '''

# import, make app, make route

from flask import Flask
from .models import DB

# Make our app factory

def create_app():
    app = Flask(__name__)

    # add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    #have the database know about the app
    DB.init_app(app)

    @app.route('/')
    def root():
        return 'Welcome to Twittoff!'
    return app

# Make route