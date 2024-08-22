from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import inspect
from setup_db import app, db, Customer  # Import the app, db object, and Customer model

# Create the tables if they don't exist
with app.app_context():
    inspector = inspect(db.engine)
    if 'customer' not in inspector.get_table_names():
        db.create_all()

# Route for the homepage, which displays the list of customers and the customer count
@app.route('/')
def index():
    customer_count = Customer.query.count()  # Get the count of customers
    customers = Customer.query.all()  # Retrieve all customer records
    return render_template('index.html', customers=customers, customer_count=customer_count)

# Route for creating a new customer, handling both GET and POST requests
@app.route('/create', methods=['GET', 'POST'])
def create_customer():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        customer = Customer(name=name, email=email, phone=phone)
        db.session.add(customer)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_customer.html')

# Route for updating an existing customer, handling both GET and POST requests
@app.route('/update/<int:customer_id>', methods=['GET', 'POST'])
def update_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    if request.method == 'POST':
        customer.name = request.form['name']
        customer.email = request.form['email']
        customer.phone = request.form['phone']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update_customer.html', customer=customer)

# Route for deleting an existing customer
@app.route('/delete/<int:customer_id>')
def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
