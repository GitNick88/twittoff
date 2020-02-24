''' Code for our app'''

# import, make app, make route

from flask import Flask

# Make our app factory

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'Welcome to Twittoff!'
    return app

# Make route