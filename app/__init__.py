from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options

bootstrap = Bootstrap()
db=SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)


    app.config.from_object(config_options[config_name])


    #initialize extensions
    bootstrap.init_app(app)
    db.init_app(app)



    # register Blueprint

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint) 
    



    return app
