
from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "thisIsASectetKey"

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == "POST":
        session["fname"] = request.form.get("fname")
        session["lname"] = request.form.get("lname")
        session["email"] = request.form.get("email")
        session["address"] = request.form.get("address")
        session["city"] = request.form.get("city")
        session["state"] = request.form.get("state")
        session["zip"] = request.form.get("zip")
        session["gender"] = request.form.get("gender")
        return redirect('/show')
    return render_template('index.html')

@app.route("/show", methods=["GET"])
def show():
    return render_template('display.html')



if __name__ == '__main__':
    app.run(debug=True, port=5000)

