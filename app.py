from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# --- CONFIGURATION ---
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'static', 'uploads')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nexus.db'
app.config['SECRET_KEY'] = 'hackathon_secret'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

db = SQLAlchemy(app)

# --- MODELS ---
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50)) 

class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500))
    dept = db.Column(db.String(100))
    status = db.Column(db.String(50), default='Submitted') 
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    img_before = db.Column(db.String(200), default='pothole_before.jpg')
    img_after = db.Column(db.String(200))
    vote_count = db.Column(db.Integer, default=1)
    assigned_to = db.Column(db.String(100), nullable=True)

def ai_classify(text):
    text = text.lower()
    if any(w in text for w in ['water', 'pipe', 'leak']): return 'Water'
    if any(w in text for w in ['light', 'electric', 'power']): return 'Electricity'
    if any(w in text for w in ['garbage', 'waste', 'trash', 'dump']): return 'Sanitation'
    return 'Roads'

# --- ROUTES ---
@app.route('/')
def index(): return render_template('login.html')

@app.route('/citizen')
def citizen_auth(): return render_template('citizen_auth.html', role="Citizen")

@app.route('/officer')
def officer_auth(): return render_template('citizen_auth.html', role="Authority")

@app.route('/worker')
def worker_auth(): return render_template('citizen_auth.html', role="Field Staff")

@app.route('/auth_action', methods=['POST'])
def auth_action():
    email = request.form.get('email')
    password = request.form.get('password')
    username = request.form.get('username')
    role_from_url = request.args.get('role', 'Citizen') 
    user = User.query.filter_by(email=email, password=password).first()
    if username and not user:
        user = User(username=username, email=email, password=password, role=role_from_url)
        db.session.add(user)
        db.session.commit()
    if user:
        if user.role == "Authority": return redirect(url_for('officer_dashboard'))
        elif user.role == "Field Staff": return redirect(url_for('worker_dashboard'))
        else: return redirect(url_for('citizen_dashboard'))
    return redirect(url_for('index'))

@app.route('/citizen_dashboard')
def citizen_dashboard():
    items = Complaint.query.all()
    return render_template('citizen.html', complaints=items)

@app.route('/officer_hub')
def officer_dashboard(): return render_template('officer_hub.html')

@app.route('/worker_tasks')
def worker_dashboard():
    items = Complaint.query.filter(Complaint.status != 'Resolved').all()
    return render_template('worker.html', items=items)

@app.route('/submit', methods=['POST'])
def submit():
    desc = request.form.get('desc')
    lat = float(request.form.get('lat'))
    lng = float(request.form.get('lng'))
    file = request.files.get('img_before')
    filename = 'pothole_before.jpg'
    if file and file.filename != '':
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    dept = ai_classify(desc)
    new_c = Complaint(description=desc, dept=dept, lat=lat, lng=lng, img_before=filename)
    db.session.add(new_c)
    db.session.commit()
    return redirect(url_for('citizen_dashboard'))

@app.route('/dept/<name>')
def dept_view(name):
    items = Complaint.query.filter_by(dept=name).all()
    return render_template('officer_dept.html', items=items, dept_name=name)

@app.route('/assign/<int:id>', methods=['POST'])
def assign(id):
    c = Complaint.query.get(id)
    worker = request.form.get('worker_name')
    if c and worker:
        c.assigned_to = worker
        c.status = 'Assigned'
        db.session.commit()
    return redirect(request.referrer)

@app.route('/claim/<int:id>')
def claim(id):
    c = Complaint.query.get(id)
    if c:
        c.status = 'In Progress'; db.session.commit()
    return redirect(url_for('worker_dashboard'))

@app.route('/resolve/<int:id>')
def resolve(id):
    c = Complaint.query.get(id)
    if c:
        c.status = 'Resolved'; db.session.commit()
    return redirect(url_for('worker_dashboard'))

if __name__ == '__main__':
    with app.app_context(): db.create_all()
    app.run(debug=True)