# 🧾 Employee Records Management System

A full-featured employee management system built with **Flask**, **MySQL**, and **JavaScript**.

## ✨ Features

✅ Email notifications on employee onboarding  
✅ Role-based access control (HR vs. Admin)  
✅ Activity logs for all key actions  
✅ Interactive dashboard with charts (e.g., total employees, departments)  
✅ RESTful API integration for third-party tools  
✅ Secure login/logout with session management  
✅ Responsive and user-friendly UI

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, Flask-SQLAlchemy, Flask-Login, Flask-Mail  
- **Database:** MySQL  
- **Frontend:** HTML, CSS, JavaScript, Chart.js  
- **API:** Flask-RESTful  
- **Authentication:** Role-based access via Flask-Login  
- **Deployment:** Gunicorn, Dotenv, etc.

---

## 📂 Project Structure

```bash
employee_mgmt/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   ├── templates/
│   ├── static/
│   ├── forms/
│   ├── api/
│   └── utils/
│
├── migrations/
├── .env
├── config.py
├── run.py
├── requirements.txt
└── README.md
