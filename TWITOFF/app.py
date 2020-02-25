''' Code for our app '''

# import, make app, make route
from decouple import config
from flask import Flask, render_template, request
from .models import DB, User

# Make our app factory

def create_app():
    app = Flask(__name__)

    # add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')

    # Stop trackingmodifications on sqlalchemy confid
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #have the database know/connect the app
    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)
    return app

# Make route