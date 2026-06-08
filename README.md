# URLShortener

A full-featured URL shortening web application built with Django. Users can register, log in, and create short links with optional custom keys, expiration dates, and QR code generation — all tracked with click analytics.

---

## Features

- **Custom user model** — email-based authentication (no username required)
- **User registration, login, and logout**
- **Short URL creation** — base62 key generation for compact, unique links
- **Custom short keys** — optionally choose your own slug
- **Expiration dates** — set a date after which a link becomes inactive
- **Click count tracking** — see how many times each link has been visited
- **Edit and delete** short URLs from your personal dashboard
- **QR code generation** — generate and display a QR code for any short URL
- **Django admin panel** — full admin control over users and URLs

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.12 |
| Framework | Django 6.x |
| Database | PostgreSQL |
| Config | python-decouple |
| Frontend | Bootstrap 5 (CDN) |
| QR Codes | qrcode, Pillow |

---



## Setup and Installation

->> Clone repository

```bash
git clone https://github.com/Mandip698/Project_5CS024.git
```

->> Create a Virtual environment using

```bash
python -m venv env
```

->> Activate Virtual environment using

-> For Windows

```bash
env\Scripts\activate
```

-> For Mac/Linux

```bash
source env\bin\activate
```

->> Install all requirements using

```bash
pip install -r requirements.txt
```

->> Initialize models using

```bash
python manage.py makemigrations
python manage.py migrate
```

->> Create admin user using

```bash
python manage.py createsuperuser
```

->> Start Web App using

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---


## How to Use

1. **Register** — create an account at `/register/` using your email and password.
2. **Log in** — sign in at `/login/`.
3. **Dashboard** — view all your short URLs, click counts, and expiration status at `/dashboard/`.
4. **Create a link** — click "Create URL", enter the destination URL, and optionally set a custom short key and expiration date.
5. **Visit a short link** — navigate to `http://127.0.0.1:8000/<short-key>/` to be redirected to the original URL.
6. **QR code** — click the QR icon on any link in your dashboard to generate a scannable QR code.
7. **Edit or delete** — manage your links directly from the dashboard.
8. **Admin panel** — access `/admin/` with your superuser credentials to manage all users and URLs.

---

