
from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "ThisIsASectetKey"



@app.route('/', methods = ['GET'])
def home():
    if not 'num' in session.keys():
        session['num'] = 0
    session["num"] += 1
    session['current'] = 'byone'
    return render_template('index.html')

@app.route('/bytwo', methods=['GET'])
def bytwo():
    session['num'] += 2
    session['current'] = 'bytwo'
    return render_template('index.html')

@app.route('/reset', methods=["GET"])
def reset():
    session['num'] = 0
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True, port=5000)

