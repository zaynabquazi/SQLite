# Import necessary modules from Flask and SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database URI and disable modification tracking
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customer.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object with the Flask app
db = SQLAlchemy(app)

# Define the Customer model, which represents the 'customer' table in the database
class Customer(db.Model):
    # Primary key column for unique identification of each customer
    id = db.Column(db.Integer, primary_key=True)
    
    # Name column for storing customer names, cannot be null
    name = db.Column(db.String(100), nullable=False)
    
    # Email column for storing customer email addresses, cannot be null
    email = db.Column(db.String(100), nullable=False)
    
    # Phone column for storing customer phone numbers, can be null
    phone = db.Column(db.String(100), nullable=True)

# Ensure that the 'customer' table exists before running the application
with app.app_context():
    inspector = inspect(db.engine)
    # Check if the 'customer' table exists; if not, create it
    if 'customer' not in inspector.get_table_names():
        db.create_all()

# Define the route for the homepage, which displays the list of customers and the customer count
@app.route('/')
def index():
    # Get the total count of customers in the database
    customer_count  = Customer.query.count()
    
    # Retrieve all customer records from the database
    customers = Customer.query.all()
    
    # Render the index.html template, passing the customer list and count
    return render_template('index.html', customers=customers, customer_count=customer_count)

# Define the route for creating a new customer, handling both GET and POST requests
@app.route('/create', methods=['GET', 'POST'])
def create_customer():
    # If the request method is POST, add the new customer to the database
    if request.method == 'POST':
        # Retrieve form data for name, email, and phone
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        
        # Create a new Customer object with the form data
        customer = Customer(name=name, email=email, phone=phone)
        
        # Add the new customer to the session and commit to the database
        db.session.add(customer)
        db.session.commit()
        
        # Redirect to the homepage after successful creation
        return redirect(url_for('index'))
    
    # If the request method is GET, render the create_customer.html template
    return render_template('create_customer.html')

# Define the route for updating an existing customer, handling both GET and POST requests
@app.route('/update/<int:customer_id>', methods=['GET', 'POST'])
def update_customer(customer_id):
    # Retrieve the customer by ID, or return a 404 error if not found
    customer = Customer.query.get_or_404(customer_id)
    
    # If the request method is POST, update the customer details
    if request.method == 'POST':
        # Update customer attributes with form data
        customer.name = request.form['name']
        customer.email = request.form['email']
        customer.phone = request.form['phone']
        
        # Commit the changes to the database
        db.session.commit()
        
        # Redirect to the homepage after successful update
        return redirect(url_for('index'))
    
    # If the request method is GET, render the update_customer.html template
    return render_template('update_customer.html', customer=customer)

# Define the route for deleting an existing customer
@app.route('/delete/<int:customer_id>')
def delete_customer(customer_id):
    # Retrieve the customer by ID, or return a 404 error if not found
    customer = Customer.query.get_or_404(customer_id)
    
    # Delete the customer record from the database
    db.session.delete(customer)
    
    # Commit the changes to the database
    db.session.commit()
    
    # Redirect to the homepage after successful deletion
    return redirect(url_for('index'))

# Entry point for running the Flask application
if __name__ == '__main__':
    # Run the app in debug mode for easier troubleshooting during development
    app.run(debug=True)
