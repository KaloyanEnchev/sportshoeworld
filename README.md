# SportShoeWorld

SportShoeWorld is a Django-powered web application for managing a sports shoe catalog. It features modular architecture, a RESTful API, and background task processing with Celery.

## Key Features
- **Shoe Catalog:** Browse and filter by category (Basketball, Football, etc.) and gender.
- **User Accounts:** Secure registration, login, and profile management.
- **Reviews:** User-driven rating and review system for products.
- **REST API:** Full CRUD operations for shoe data via Django REST Framework.
- **Admin Panel:** Modern management interface using `django-unfold`.
- **Background Tasks:** Asynchronous processing powered by Celery and Redis.

## Quick Setup

### Prerequisites
- Python 3.8+, PostgreSQL, Redis, Git.

### Installation
1. **Clone & Enter:**
   ```bash
   git clone https://github.com/KaloyanEnchev/sportshoeworld.git && cd SportShoeWorld
   ```
2. **Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Configure `.env`:**
   Create a `.env` file based on `.env.template` with your `DB_*` and `SECRET_KEY` values.
4. **Database & Admin:**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
5. **Run Services (Separate Terminals):**
   - Server: `python manage.py runserver`
   - Worker: `celery -A SportShoeWorld worker -l info`

## Project Structure
- `accounts/`: User authentication and profiles.
- `shoes/`: Core catalog and shoe management.
- `api_shoes/`: REST API endpoints.
- `reviews/`: User feedback and ratings.
- `SportShoeWorld/`: Core settings and Celery configuration.

## API Endpoints
- `GET /api/shoes/`: List all shoes.
- `POST /api/shoes/`: Add a new shoe.
- `GET /api/shoes/<id>/`: View shoe details.
- `GET /api/shoes/stats/`: View shoe catalog statistics.

## Usage
Access the web app at `http://127.0.0.1:8000` and the admin panel at `http://127.0.0.1:8000/admin/`.
