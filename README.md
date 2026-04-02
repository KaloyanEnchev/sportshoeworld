# SportShoeWorld 👟

SportShoeWorld is a Django-based web application designed for managing and showcasing a comprehensive catalog of sports shoes. It features a robust backend, user engagement tools, and a modern management interface.

---

### ✨ Features
* **Catalog Management:** Browse shoes with detailed info (price, description, images).
* **Smart Filtering:** Filter by sport (Basketball, Volleyball, Handball, Football) and gender.
* **User System:** Full registration, login, and review functionality.
* **API Access:** Built-in RESTful API for programmatic integration.
* **Modern Admin:** Responsive and sleek dashboard powered by `django-unfold`.
* **Performance:** Asynchronous task processing via Celery and Redis.

### 🛠 Technologies
* **Backend:** Python 3.8+, Django 5.x, Django REST Framework
* **Task Queue:** Celery & Redis
* **Database:** PostgreSQL (`psycopg2-binary`)
* **Frontend:** HTML5, CSS3
* **UI/UX:** django-unfold

---

### 🚀 Setup Guide

1. **Clone & Navigate**
   ```bash
   git clone [https://github.com/KaloyanEnchev/sportshoeworld.git](https://github.com/KaloyanEnchev/sportshoeworld.git)
   cd SportShoeWorld
Environment SetupBashpython -m venv venv
# macOS/Linux:
source venv/bin/activate   
# Windows:
venv\Scripts\activate      
Install Dependencies
Bashpip install -r requirements.txt
ConfigurationCopy .env.template to .env.Update your Database credentials and Secret Key.Initialize DatabaseBashpython manage.py migrate
python manage.py createsuperuser
Run the ApplicationServer:
python manage.py runserver
Celery Worker: celery -A SportShoeWorld worker -l info
Celery Beat: celery -A SportShoeWorld beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler📖 
