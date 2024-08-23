from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import inspect
from setup_db import app, db, Customer, Inventory, Orders  # Consolidated import statement


# Route for orders 
@app.route('/orders')
def zaynab():
    order_items = Orders.query.all()
    order_count = Orders.query.count()
    return render_template('orders.html', order_items=order_items, order_count=order_count)

# Route to display all inventory items
@app.route('/inventory')
def inventory():
    inventory_items = Inventory.query.all()
    return render_template('inventory.html', inventory_items=inventory_items)
q

@app.route('/create_inventory', methods=['GET', 'POST'])
def create_inventory():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        quantity = request.form['quantity']
        
        # Assuming Inventory is a model you have imported and defined
        new_inventory = Inventory(name=name, price=price, quantity=quantity)
        db.session.add(new_inventory)
        db.session.commit()
        
        return redirect(url_for('inventory'))  # Redirect to the inventory list after creation
    
    return render_template('create_inventory.html')  # Render the form on GET request

@app.route('/update/<int:inventory_id>', methods=['GET', 'POST'])
def update_inventory(inventory_id):
    inventory = Inventory.query.get_or_404(inventory_id)
    if request.method == 'POST':
        inventory.name = request.form['name']
        inventory.price = request.form['price']
        inventory.quantity = request.form['quantity']
        db.session.commit()
        return redirect(url_for('inventory'))  # Redirect to the homepage route
    return render_template('update_inventory.html', inventory=inventory)

# Route for the homepage, which displays the list of customers and the customer count
@app.route('/')
def homepage():
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
        return redirect(url_for('homepage'))  # Redirect to the homepage route
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
        return redirect(url_for('homepage'))  # Redirect to the homepage route
    return render_template('update_customer.html', customer=customer)

# Route for deleting an existing customer
@app.route('/delete/<int:customer_id>')
def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for('homepage'))  # Redirect to the homepage route

if __name__ == '__main__':
    app.run(debug=True)
