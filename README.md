# 🧾 Employee Records Management System

A full-featured **Employee Records Management System** built with **Flask**, designed for small to medium-sized organizations to manage employee data securely and efficiently.

## 🚀 Features

- ✅ **Employee Onboarding with Email Notification**
- ✅ **Role-Based Access Control (RBAC)** – Admins, HRs, and Users
- ✅ **Audit Trail** – Tracks changes and logs activities
- ✅ **Dashboard** – Visual charts showing employees per department, gender ratio, etc.
- ✅ **RESTful API** – For third-party integration
- ✅ **Authentication** – Login/Logout, Secure Sessions
- ✅ **Responsive UI** – Can be extended with Bootstrap or any frontend framework

---

## 🛠️ Tech Stack

| Layer        | Technology Used              |
|--------------|------------------------------|
| Backend      | Python (Flask)               |
| Database     | SQLite / PostgreSQL          |
| ORM          | SQLAlchemy                   |
| Forms        | Flask-WTF                    |
| Email        | Flask-Mail                   |
| Auth         | Flask-Login                  |
| API Layer    | Flask-RESTful + Flask-CORS   |
| Charts       | Chart.js (optional frontend) |

---

## 📁 Project Structure

```
employee_mgmt/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   │   ├── auth.py
│   │   ├── dashboard.py
│   │   └── employee.py
│   ├── templates/
│   ├── static/
│   ├── forms/
│   │   └── employee_form.py
│   ├── api/
│   │   └── endpoints.py
│   ├── utils/
│   │   ├── mailer.py
│   │   └── logger.py
│   └── config.py
│
├── migrations/
├── .env
├── run.py
├── requirements.txt
└── README.md
```

---

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/employee-mgmt.git
cd employee-mgmt

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env

# Initialize the database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Run the app
flask run
```

---

## ⚙️ Environment Variables (`.env`)

```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
SQLALCHEMY_DATABASE_URI=sqlite:///db.sqlite3
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-email-password
```

---

## 📊 Dashboard

The dashboard displays:

- 📌 Total employees
- 📌 Department-wise distribution
- 📌 Gender ratio
- 📌 Recently added staff

*Data visualizations can be powered by Chart.js or similar libraries.*

---

## 📡 REST API Endpoints

```http
GET /api/employees            # List all employees
POST /api/employees           # Create new employee
PUT /api/employees/<id>       # Update employee
DELETE /api/employees/<id>    # Delete employee
```

Enable CORS for safe external access.

---

## 🔐 Role-Based Access

| Role     | Access to                        |
|----------|----------------------------------|
| Admin    | All CRUD, user creation, logs    |
| HR       | Manage employees only            |
| User     | View own profile                 |

*Implemented using Flask-Login decorators.*

---

## 📬 Email Notifications

Upon successful employee creation, the system sends a welcome email. Configuration handled in `utils/mailer.py`.

---

## 🧾 Activity Logs

All changes (create, update, delete) are logged with:

- User who made the change
- Timestamp
- Nature of action

Stored in the database for audit purposes.

---

## 🧪 Testing

Basic testing using `unittest` or `pytest` is recommended. Add test cases under a `/tests` directory.

---

## 📦 Deployment

Ready for deployment with **Gunicorn** and **Heroku** or **Render**.

Example:

```bash
gunicorn run:app
```

---

## 🤝 Contribution

PRs are welcome! Follow these steps:

1. Fork the repo
2. Create your branch (`git checkout -b feature/new`)
3. Commit changes (`git commit -m "Add new feature"`)
4. Push (`git push origin feature/new`)
5. Open Pull Request

---

## 📄 License

MIT License – feel free to use and modify.

---

## 👨‍💻 Author

**John Ezekiel**  
Data Analyst | Python Developer | SQL Enthusiast  
[LinkedIn](https://www.linkedin.com/in/john-ezekiel-coren/) | [GitHub](https://github.com/Sirius1616)

