from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
   grades = [
    {'name': 'Ben', 'english': 90, 'science': 80, 'maths': 80 },
    {'name': 'Jack', 'english': 80, 'science': 90, 'maths': 90 }]   
    return render_template('home.html',grades = grades, favourite_food='chocolate', number = 20)

@app.route('/about')
def about():
    return 'This a test website.'