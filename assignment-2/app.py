
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/name', methods = ['GET', 'POST'])
def name():
    return render_template('name.html', name="Trey")

@app.route('/food', methods = ['GET', 'POST'])
def food():
    return render_template('food.html', food="Pizza")

@app.route('/vacation', methods = ['GET', 'POST'])
def vacation():
    return render_template('vacation.html', vacation="La Paz Mexico")


if __name__ == '__main__':
    app.run(debug=True, port=5000)

