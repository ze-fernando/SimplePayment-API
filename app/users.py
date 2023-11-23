from . import db, bcrypt
from werkzeug.security import check_password_hash


class Users(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    balance = db.Column(db.Float, default=0.0)
    type = db.Column(db.String(10), nullable=False)

    def set_pass(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        
    def check_pass(self, password):
        return bcrypt.check_password_hash(self.password, password)