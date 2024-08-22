from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database URI and disable modification tracking
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customer.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object with the Flask app
db = SQLAlchemy(app)

# Define the Customer model, representing the 'customer' table in the database
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=True)

# Define the Inventory model, representing the 'inventory' table in the database
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.String(100), nullable=True)

# Create the tables if they don't exist
 
    with app.app_context():
        inspector = inspect(db.engine)
        if 'inventory' not in inspector.get_table_names():
            db.create_all()
        if 'customer' not in inspector.get_table_names():
            db.create_all()

