from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
database_conn = 'mysql+pymysql://root:rootroot@localhost/custdb?'
app.config['SQLALCHEMY_DATABASE_URI'] = database_conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Customer(db.Model):
    customerId = db.Column('cust_id', db.Integer, primary_key=True)
    customerName = db.Column('cust_name', db.String(100))
    customerAge = db.Column('cust_age', db.Integer)
    customerBalance = db.Column('cust_balance', db.Float)
    customerAddress = db.Column('cust_address', db.String(100))


db.create_all()
