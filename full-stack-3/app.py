from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class Course(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    created_on = db.Column(db.DateTime)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == "POST":
        name = request.form.get('name')
        description = request.form.get('description')
        new_course = Course(name = name, description = description, created_on = datetime.datetime.now())
        db.session.add(new_course)
        db.session.commit()
        return redirect(url_for('home'))
    courses = Course.query.all()
    return render_template('index.html', courses = courses)

@app.route('/delete/<pk>', methods=['GET'])
def delete(pk):
    course = Course.query.get(pk)
    db.session.delete(course)
    db.session.commit()
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True, port=5000)

