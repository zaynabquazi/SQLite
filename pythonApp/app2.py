from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
#modify the app to not use the 24 hour clock
#and to use the 12 hour clock




@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name')
    current_hour = datetime.now().hour

    if 5 <= current_hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    return render_template('greet.html', name=name, greeting=greeting)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
