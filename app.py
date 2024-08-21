from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///phonebook.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Person model (maps to the Person table)
class Person(db.Model):
    __tablename__ = 'Person'
    Key = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))

# Define routes for CRUD operations
@app.route('/')
def index():
    people = Person.query.all()  # Fetch all persons
    return render_template('index.html', people=people)

@app.route('/add', methods=['POST'])
def add_person():
    name = request.form.get('name')
    new_person = Person(Name=name)
    db.session.add(new_person)
    db.session.commit()  # Save the new person to the database
    return redirect(url_for('index'))

@app.route('/edit/<int:key>', methods=['GET', 'POST'])
def edit_person(key):
    person = Person.query.get_or_404(key)  # Get the person or return 404
    if request.method == 'POST':
        person.Name = request.form.get('name')
        db.session.commit()  # Update the person's name in the database
        return redirect(url_for('index'))
    return render_template('edit.html', person=person)

@app.route('/delete/<int:key>')
def delete_person(key):
    person = Person.query.get_or_404(key)
    db.session.delete(person)  # Delete the person from the database
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    db.create_all()  # Create tables if they don't exist
    app.run(debug=True)  # Start the Flask application