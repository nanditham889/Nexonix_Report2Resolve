from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nexus.db'
app.config['SECRET_KEY'] = 'hackathon_secret'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

db = SQLAlchemy(app)

class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500))
    dept = db.Column(db.String(100))
    status = db.Column(db.String(50), default='Open') # Open, In Progress, Resolved
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    img_before = db.Column(db.String(200), default='pothole_before.jpg')
    img_after = db.Column(db.String(200))
    vote_count = db.Column(db.Integer, default=1)

def ai_classify(text):
    text = text.lower()
    if 'water' in text or 'pipe' in text: return 'Water'
    if 'light' in text or 'electric' in text: return 'Electricity'
    return 'Roads'

@app.route('/')
def index(): return render_template('login.html')

@app.route('/citizen')
def citizen():
    items = Complaint.query.all()
    return render_template('citizen.html', complaints=items)

@app.route('/submit', methods=['POST'])
def submit():
    desc = request.form.get('desc')
    lat, lng = float(request.form.get('lat')), float(request.form.get('lng'))
    dept = ai_classify(desc)
    
    # Simple Duplicate Check (Distance based)
    match = Complaint.query.filter_by(dept=dept, status='Open').first()
    if match and abs(match.lat - lat) < 0.01:
        match.vote_count += 1
    else:
        new_c = Complaint(description=desc, dept=dept, lat=lat, lng=lng)
        db.session.add(new_c)
    db.session.commit()
    return redirect(url_for('citizen'))

@app.route('/officer')
def officer(): return render_template('officer_hub.html')

@app.route('/dept/<name>')
def dept_view(name):
    items = Complaint.query.filter_by(dept=name).all()
    return render_template('officer_dept.html', items=items, dept_name=name)

@app.route('/worker')
def worker():
    items = Complaint.query.filter_by(status='Open').all()
    return render_template('worker.html', items=items)

@app.route('/claim/<int:id>')
def claim(id):
    c = Complaint.query.get(id)
    c.status = 'In Progress'
    db.session.commit()
    return redirect(url_for('worker'))

@app.route('/resolve/<int:id>')
def resolve(id):
    c = Complaint.query.get(id)
    c.status = 'Resolved'
    c.img_after = 'pothole_after.jpg'
    db.session.commit()
    return redirect(url_for('worker'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)