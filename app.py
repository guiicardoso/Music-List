from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/bey')
def bye():
    return ' Bye'

app.run(debug=True)

