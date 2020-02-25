'''Entry point for our twitoff flask app'''

from .app import create_app

#Capitalize APP because it's a global variable
APP = create_app()