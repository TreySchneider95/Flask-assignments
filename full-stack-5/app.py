from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class User(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    blogs = db.relationship('Blog')

class Blog(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    text = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    user = db.Column(db.Integer, db.ForeignKey('user.pk'))

    @classmethod
    def get_user(cls, pk):
        return User.query.get(pk)

with app.app_context():
    db.create_all()

@app.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email = email, password = password).first()
        if user:
            return redirect(url_for('home', pk = user.pk))
    return render_template('index.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        new_user = User(email = email, password = password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/home/<pk>', methods=['GET', 'POST'])
def home(pk):
    user = User.query.get(pk)
    blogs = Blog.query.all()
    if request.method == "POST":
       title = request.form.get('title')
       text = request.form.get('text')
       created_at = datetime.datetime.now()
       blog = Blog(title = title, text = text, created_at = created_at, user = user.pk)
       db.session.add(blog)
       db.session.commit()
       return redirect(url_for('home', pk = user.pk))
    return render_template('home.html', user = user, blogs = blogs)



if __name__ == '__main__':
    app.run(debug=True, port=5000)

