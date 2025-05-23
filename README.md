# 📱 Android App Review & Reward Portal

[![Built with Django](https://img.shields.io/badge/Built%20With-Django-092E20?logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/API-DRF-blue?logo=django)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Live App](https://img.shields.io/badge/Live%20Demo-Click%20Here-brightgreen?logo=render)](https://app-recomendations.onrender.com/)

---

## 🌐 Live Demo

* 🔗 [Visit Live Application](https://app-recomendations.onrender.com/)
* 🎥 [Watch Screencast (Google Drive)](https://drive.google.com/file/d/1I88LOEasbHKovdw5GiG1JrWLEVLgAoTd/view?usp=sharing)

---

## 📌 Project Overview

A Django-based reward portal that allows:

* 👨‍💼 **Admins** to add Android apps, assign points, and verify user tasks
* 👤 **Users** to complete app download tasks and upload screenshots for points
* 📀 Drag-and-drop UI for screenshot proof
* 📊 Dashboard for tracking tasks and points

---

## ⚙️ Tech Stack

| Category        | Technology                    |
| --------------- | ----------------------------- |
| Language        | Python 3.9+                   |
| Backend         | Django, Django REST Framework |
| Authentication  | session based                 |
| Database        | SQLite3                       |
| Frontend        | Django Templates + JS         |
| Media Uploads   | Drag-and-drop uploader        |
| Deployment      | Render                        |
| Dev Environment | VSCode                        |

---

## 🚀 Deployment on Render

Follow these steps to deploy the Django app to [Render](https://render.com):

### 1. Prepare your project

* Ensure `requirements.txt` is up to date:

  ```bash
  pip freeze > requirements.txt
  ```
* Create a `Procfile` with the following content:

  ```bash
  web: gunicorn your_project_name.wsgi
  ```
* Make sure `gunicorn` is added to `requirements.txt`
* In `settings.py`, add:

  ```python
  ALLOWED_HOSTS = ['.onrender.com']
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
  ```

### 2. Push to GitHub/GitLab

Push your complete project to a Git repository.

### 3. Create a New Web Service on Render

* Go to [Render Dashboard](https://dashboard.render.com/)
* Click **New → Web Service**
* Connect your repo
* Set environment:

  * **Build Command:**

    ```bash
    pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate
    ```
  * **Start Command:**

    ```bash
    gunicorn your_project_name.wsgi
    ```
  * **Environment Variables:**

    * `DJANGO_SETTINGS_MODULE=your_project_name.settings`
    * `PYTHON_VERSION=3.9`

### 4. Set Up Static Files

Ensure `staticfiles` is being served correctly. Add WhiteNoise to `MIDDLEWARE`:

```python
MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
  ...
]
```

And in `settings.py`:

```python
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### 5. Deploy and Test

Render will build and deploy your service. Use the generated URL to access your app.

---

## 🧪 Problem Set 1 – Regex Extraction

**Objective:** Extract all numbers with orange background (from "orders" JSON).

```python
import re

text = '''{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}'''

ids = re.findall(r'"id":(\d+)', text)
ids = [int(i) for i in ids]
print(ids)
```

**Output:**

```python
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 648, 649, 650, 651, 652, 653]
```

---

## 🧠 Problem Set 3 – Written Questions

### 🔄 A. Periodic Task Scheduler – Choice & Justification

* **Tool Chosen:** `Celery + django-celery-beat`

* **Why?**

  * Seamless integration with Django
  * Supports asynchronous and periodic tasks
  * Reliable for production with Redis/RabbitMQ as brokers

* **Scalability:**

  * Easily scales horizontally using multiple workers
  * Monitorable via Flower, Prometheus

* **Challenges:**

  * Needs proper configuration for production deployments
  * Error handling must be manually defined

* **At Scale Recommendations:**

  * Use **Apache Airflow** or **Temporal.io** for complex and dependency-based workflows

---

### ⚖️ B. Flask vs Django – Use Case Comparison

| Criteria       | Flask                           | Django                         |
| -------------- | ------------------------------- | ------------------------------ |
| Type           | Microframework                  | Full-stack Framework           |
| Best For       | Lightweight APIs, microservices | Complex web apps, admin panels |
| Features       | Minimal out-of-the-box          | Batteries-included             |
| Learning Curve | Shallow                         | Moderate                       |
| Use Case       | Quick POCs, custom workflows    | Admin-heavy apps, faster MVPs  |

**Summary:**

* ✅ Choose **Flask** for flexibility and minimal setup
* ✅ Choose **Django** for structure, rapid development, and built-in components
