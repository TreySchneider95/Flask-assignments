
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == "POST":
        context = {}
        context["fname"] = request.form.get("fname")
        context["lname"] = request.form.get("lname")
        context["email"] = request.form.get("email")
        context["address"] = request.form.get("address")
        context["city"] = request.form.get("city")
        context["state"] = request.form.get("state")
        context["zip"] = request.form.get("zip")
        context["gender"] = request.form.get("gender")
        return render_template('display.html', context=context)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, port=5000)

