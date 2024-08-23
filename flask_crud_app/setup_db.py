from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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
    quantity = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String(255), nullable=True)

# create a new orders table
# once you have the code, you run python3 setup_db.py to create the table
# -- Create the orders table with a foreign key to the customer table
# CREATE TABLE orders (
#    id INTEGER PRIMARY KEY,
#    customer_id INTEGER,
#    order_date TEXT,
#    FOREIGN KEY (customer_id) REFERENCES customer(id)
# );
class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    order_date = db.Column(db.String(100), nullable=False)
    customer = db.relationship('Customer', backref='orders')
    
# Create the tables if they don't exist
with app.app_context():
    db.create_all()
