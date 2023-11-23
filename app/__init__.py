from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt

app = Flask(__name__)

db = SQLAlchemy()
bcrypt = Bcrypt(app)        

def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['BCRYPT_LOG_ROUNDS'] = 12
    
    db.init_app(app)
    

    from .routes import route
    app.register_blueprint(route)

    return app

from .users import Users