
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

DEFAULT_INFO = {'fname': 'Joe', 'lname': 'Shmo', 'ffood': 'Pizza', 'fvacation': 'La Paz Mexico'}

@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html', info = DEFAULT_INFO)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == "POST":
        the_form = request.form
        context = {}
        context['fname'] = the_form.get("fname")
        context['lname'] = the_form.get("lname")
        context['email'] = the_form.get("email")
        context['ffood'] = the_form.get("ffood")
        return render_template('display.html', context=context)
    return render_template('form.html')

@app.route('/numbers', methods=['GET'])
def numbers():
    return render_template('numbers.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

