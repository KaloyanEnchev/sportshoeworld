# 👟 SportShoeWorld

**SportShoeWorld** is a high-performance, feature-rich Django web application designed for managing and exploring a comprehensive sports shoe catalog. Built with modern web standards, it offers a seamless experience for users and powerful management tools for administrators.

---

## Deployed application link: https://sportshoeworld-dgccg4epbbcpgxbu.swedencentral-01.azurewebsites.net/

---

## ✨ Key Features

### 🔍 Advanced Discovery
- **Global Search**: Instantly find products by searching through models and descriptions.
- **Dynamic Categories**: Specialized views for Basketball, Football, Volleyball, and Handball.

### 👤 User Experience
- **Custom Authentication**: Secure email-based login system with personalized user profiles.
- **Review System**: Collaborative feedback with star ratings and detailed comments.
- **Responsive UI**: A clean, mobile-friendly interface built with custom CSS and modern templates.

### 🛠 Technical Excellence
- **RESTful API**: Full-featured API built with Django REST Framework for external integrations.
- **Background Processing**: Celery and Redis handle heavy tasks like data normalization and automated cleanup.
- **Security Hardened**: Production-ready security settings including HSTS, XSS protection, and API rate limiting (throttling).
- **Modern Admin**: A sleek, responsive dashboard powered by `django-unfold`.

---

## 🚀 Tech Stack

- **Backend**: Python, Django 5.x
- **API**: Django REST Framework (DRF)
- **Database**: PostgreSQL
- **Task Queue**: Celery & Redis
- **Frontend**: HTML5, CSS3, Django Templates
- **Security**: WhiteNoise, python-decouple, DRF Throttling

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- PostgreSQL
- Redis Server (for Celery)

### 1. Clone & Environment
```bash
git clone https://github.com/KaloyanEnchev/sportshoeworld.git
cd SportShoeWorld
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configuration
Create a `.env` file in the root directory:
```env
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=sportshoeworld
DB_USER=your_user
DB_PASS=your_password
DB_HOST=localhost
DB_PORT=5432
```

### 3. Database & Admin
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 4. Run Services (Separate Terminals)
```bash
# Terminal 1: Django Server
python manage.py runserver

# Terminal 2: Celery Worker
celery -A SportShoeWorld worker -l info
```

---

## 📁 Project Structure

```text
├── accounts/       # User management & Profiles
├── api_shoes/      # REST API endpoints & Serializers
├── shoes/          # Core catalog, Advanced Filtering & Logic
├── reviews/        # User feedback system & Celery tasks
├── common/         # Shared mixins, choices, and validators
├── templates/      # Global and app-specific templates
└── static/         # Optimized CSS and assets
```

---

## 🔌 API Overview

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/shoes/` | `GET` | List all shoes (Supports filtering) |
| `/api/shoes/` | `POST` | Create a new shoe entry |
| `/api/shoes/<id>/` | `GET` | Get detailed shoe information |
| `/api/shoes/stats/` | `GET` | Global catalog statistics |

---

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

---
**Developed by [Kaloyan Enchev](https://github.com/KaloyanEnchev)**
