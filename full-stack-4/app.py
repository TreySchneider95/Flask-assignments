from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app)

class User(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String)
    email = db.Column(db.String)
    created_at = db.Column(db.DateTime)

with app.app_context():
    db.create_all()

@app.route('/', methods = ['GET'])
def home():
    users = User.query.all()
    return render_template('index.html', users = users)

@app.route('/users/create', methods=["GET", "POST"])
def create():
    if request.method == "POST":
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        created_at = datetime.datetime.now()
        user = User(full_name = full_name, email = email, created_at = created_at)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('new_user.html')

@app.route('/users/<pk>', methods=["GET"])
def show_user(pk):
    user = User.query.get(pk)
    return render_template('show_user.html', user = user)

@app.route("/users/<pk>/edit", methods=['GET', 'POST'])
def edit_user(pk):
    user = User.query.get(pk)
    if request.method == "POST":
        user.full_name = request.form.get('full_name')
        user.email = request.form.get('email')
        db.session.commit()
        return redirect(url_for('show_user', pk = user.pk))
    return render_template('edit_user.html', user = user)

@app.route('/users/<pk>/destroy', methods=['GET'])
def delete_user(pk):
    user = User.query.get(pk)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)

