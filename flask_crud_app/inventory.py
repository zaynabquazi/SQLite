from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from setup_db import app, db, Inventory  # Import the app, db object, and Inventory model

# Ensure the Inventory model is defined in setup_db
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=True)

# Route to display all inventory items
@app.route('/inventory')
def index():
    inventory_items = Inventory.query.all()
    return render_template('inventory.html', inventory_items=inventory_items)

# Route for creating a new inventory item
@app.route('/create2', methods=['GET', 'POST'])
def create_inventory():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        quantity = request.form['quantity']
        new_inventory = Inventory(name=name, price=price, quantity=quantity)
        db.session.add(new_inventory)
        db.session.commit()
        return redirect(url_for('index'))  # Redirect to the inventory route

    return render_template('create_inventory.html')

if __name__ == '__main__':
    app.run(debug=True)
