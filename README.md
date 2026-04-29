# Nexonix_Report2Resolve
smart AI-powered civic issue reporting and resolution system
# 🚨 Report2Resolve: Smart Urban Governance System

**Report2Resolve** is a full-stack automated incident reporting and dispatch system designed to bridge the gap between citizens and government departments.  
It provides a modern SaaS-style interface with a proximity-aware task assignment system for efficient urban issue resolution.

---

## 🚀 Key Features

### 🧠 Smart Dispatch Queue
- Automatically identifies and suggests the **nearest available staff** (e.g., *0.4 km away*)  
- Improves response time and resource efficiency  

---

### 🏙 Three-Tiered Ecosystem

#### 👤 Citizen Portal
- Submit complaints with:
  - GPS coordinates 📍  
  - Photo evidence 📸  
- Simple and user-friendly interface  

#### 🧑‍💼 Officer Dashboard
- View and manage incoming reports  
- Verify uploaded evidence  
- Assign tasks to field workers  

#### 🛠 Field Worker Interface
- Mobile-friendly mode UI  
- View assigned tasks  
- Upload "After" images as proof of completion  

---

### 📸 Visual Proof Verification
- Tasks **cannot be marked as resolved** without uploading proof  
- Ensures accountability and transparency  

---

### 🔄 Real-Time Status Tracking
Track report lifecycle:
- **Submitted → In Progress → Resolved**

---

## 🛠 Tech Stack

| Layer       | Technology Used |
|------------|----------------|
| Backend     | Python (Flask) / Java (Servlets & JSP) |
| Frontend    | HTML5, Tailwind CSS, Jinja2 |
| UI Elements | Lucide Icons |
| Database    | SQLite |
| Design      | SaaS-inspired (Zinc + Emerald theme) |

---

## 📂 Project Structure
Report2Resolve/
│
├── static/
│ ├── uploads/ # Stores before & after images
│ └── css/ # Tailwind/custom styles
│
├── templates/
│ ├── citizen.html # Citizen complaint portal
│ ├── officer_dept.html # Officer dashboard
│ └── worker.html # Field worker interface
│
├── app.py # Flask backend
└── database.db # SQLite database

1 Install Requirements
pip install flask

2 Run the App
python app.py

3 Open in Browser
http://127.0.0.1:5000


🧪 How to Use
👤 Citizen
Submit a complaint with image + location

🧑‍💼 Officer
View complaints
Assign to nearest worker

🛠 Worker
Accept task
Upload "after" image to mark as resolved

⚡ Demo Flow (Recommended for Judges)
Submit a complaint from Citizen Portal
Open Officer Dashboard → assign task
Open Worker Interface → complete task
Upload proof → status becomes Resolved
💡 Core Idea

Report2Resolve solves the gap between complaint submission and actual resolution by:

Ensuring proof-based completion
Using proximity-based task assignment
Providing role-based dashboards