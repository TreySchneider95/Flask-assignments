from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app)

class User(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    user_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(user_name = username, password = password).first()
        print(user)
        if user:
            return redirect(url_for('registered', pk = user.pk))
    return render_template('index.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == "POST":
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        user_name = request.form.get('user_name')
        email = request.form.get('email')
        password = request.form.get('password')
        new_user = User(first_name = first_name, last_name = last_name, user_name = user_name, email = email, password = password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('registered', pk = new_user.pk))
    return render_template('register.html')

@app.route('/registed/<pk>', methods=["GET"])
def registered(pk):
    user = User.query.get(pk)
    return render_template('registered.html', user = user)



if __name__ == '__main__':
    app.run(debug=True, port=5000)

