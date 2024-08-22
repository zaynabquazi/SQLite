from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from setup_db import app, db, Inventory  # Import the app, db object, and Inventory model




# Route to display all inventory items
@app.route('/inventory')
def index():
    inventory_items = Inventory.query.all()
    return render_template('inventory.html', inventory_items=inventory_items)


if __name__ == '__main__':
    app.run(debug=True)
