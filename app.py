from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', favourite_food='chocolate', number1 = 12, number2 =  10)

@app.route('/about')
def about():
    return 'This a test website.'