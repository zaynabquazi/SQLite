from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customer.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=True)
      
with app.app_context():
    # Check if the 'customer' table exists
    inspector = inspect(db.engine)
    if 'customer' not in inspector.get_table_names():
        db.create_all()

    
@app.route('/')

def index():
    customer_count  = Customer.query.count()  # Get the count of customers
    customers = Customer.query.all()
    return render_template('index.html', customers=customers, customer_count=customer_count)

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

@app.route('/delete/<int:customer_id>')
def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

  
