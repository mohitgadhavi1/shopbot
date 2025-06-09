## 📚 Documentation

- [Assignment Details](docs/assignment.md)
- [Architecture Overview](docs/architecture.md)

# 🛍️ ShopBot

ShopBot is a full-stack e-commerce prototype built with **Django REST Framework**, **React (Vite)**, and **Supabase PostgreSQL**. It supports user authentication, secure API access, and dummy product listings.

---

## 🌍 Live Deployment

- **Frontend:** [https://shopbot-frontend.vercel.app](https://shopbot-frontend.vercel.app)
- **Backend (API):** [https://shopbot-jla9.onrender.com](https://shopbot-jla9.onrender.com)
- **Database:** [Supabase](https://supabase.com) (PostgreSQL managed)

---

## 🐛 Known Limitations/ Bugs / Issues

1. **Server Downtime**  
   The backend server may be temporarily unavailable due to usage limits on the free trial version of the Render hosting platform.

2. **Limited Product Search**  
   Search functionality currently supports limited text matching, as product data is still being revised and improved.

3. **Missing Product Images**  
   Some product images may not load because external image support from Unsplash has been revoked or restricted. 

🔍 **Please refer to the **Issues**[https://github.com/mohitgadhavi1/shopbot/issues](https://github.com/mohitgadhavi1/shopbot/issues) section of this project for an up-to-date list of known bugs, enhancements, and feature requests.

## 🔧 Features

### 🧠 Backend (Django + DRF)
- **User authentication** (Signup, Login) using JWT
- **Protected product APIs** (`/api/products/`)
- **Connected to Supabase PostgreSQL** via Django
- Dummy product data stored in Supabase
- Hosted on **Render**

### 🎨 Frontend (React + Vite)
- Modern, fast UI with Tailwind CSS
- Secure form validation with password strength meter
- Communicates with backend over HTTPS
- Hosted on **Vercel**

---

## 🗃️ Data Storage – Supabase

All data is stored in a **Supabase PostgreSQL** instance:

- 🧑‍💻 `users` table → stores registered users (via Django auth)
- 📦 `products` table → stores product data from your Django model
- Supabase URL and keys configured via environment variables

> Django connects to Supabase using its PostgreSQL connection string in `DATABASES` setting.

---


---

## ⚙️ Setup Instructions

### 1. Clone the project

```bash
git clone https://github.com/your-username/shopbot.git
cd shopbot

/backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Apply migrations and load dummy data
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

/frontend
cd frontend
npm install
npm run dev


🔐 API Endpoints
Endpoint  Method  Auth  Description
/api/auth/signup/  POST  ❌  Register a new user
/api/auth/login/  POST  ❌  Login and get token
/api/products/  GET  ✅  Get all products

🧪 Dummy Product Data
100 products are auto-populated via a Python script using Product.objects.create(...) and saved in Supabase. Product model includes:

python
Copy
Edit
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    original_price = models.FloatField()
    image = models.URLField()
    rating = models.FloatField()
    reviews = models.IntegerField()
    category = models.CharField(max_length=100)
    description = models.TextField()


⚠️ Notes
Ensure HTTPS is used both for frontend and backend to avoid mixed-content errors.

If you see DisallowedHost, update ALLOWED_HOSTS in Django settings.

If Vercel shows 401 Unauthorized, ensure JWT token is being passed correctly in headers.

🧾 Deployment
Render (backend):

Connect GitHub repo

Use deploy hook or automatic build on push

Add environment variables via Render dashboard

Vercel (frontend):

Set VITE_API_URL to Render URL

Enable HTTPS support




