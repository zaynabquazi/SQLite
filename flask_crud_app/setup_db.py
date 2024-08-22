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
