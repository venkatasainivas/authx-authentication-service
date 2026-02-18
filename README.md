# AuthX – Authentication & Authorization Service
![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.129.0-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

AuthX is a production-style authentication backend built using FastAPI and PostgreSQL. It provides secure user registration, JWT-based authentication, refresh tokens, and role-based access control (RBAC) using a clean and modular architecture.

## 🚀 Features

- Secure user registration with bcrypt password hashing  
- OAuth2 password flow login  
- JWT access token generation  
- Refresh token system for session renewal  
- Protected routes using dependency injection  
- Role-Based Access Control (Admin/User)  
- PostgreSQL database integration  
- SQLAlchemy ORM  
- Clean layered backend architecture  

## 🛠 Tech Stack

- Python  
- FastAPI  
- PostgreSQL  
- SQLAlchemy  
- JWT (python-jose)  
- Passlib (bcrypt)  
- OAuth2 Password Flow  

## 🔐 Authentication Flow

1. User registers with email and password  
2. Password is securely hashed using bcrypt  
3. User logs in using OAuth2 password flow  
4. Short-lived access token is generated  
5. Long-lived refresh token is generated  
6. Protected routes require valid JWT  
7. Admin routes require role-based authorization  

## 📂 Project Structure

authx/  
├── app/  
│   ├── api/          # Route definitions  
│   ├── core/         # Security & token logic  
│   ├── db/           # Database connection  
│   ├── models/       # SQLAlchemy models  
│   ├── schemas/      # Pydantic schemas  
├── main.py           # Application entry point  
├── requirements.txt  
└── README.md  

## 🧪 API Endpoints

- POST /auth/register → Register new user  
- POST /auth/login → Login & receive tokens  
- GET /auth/users/me → Get current user (Protected)  
- GET /auth/admin/dashboard → Admin-only route  
- POST /auth/refresh → Generate new access token  

## ⚙️ Setup

1. Clone repository  
git clone https://github.com/YOUR_USERNAME/authx-authentication-service.git  
cd authx-authentication-service  

2. Create virtual environment  
python -m venv venv  

3. Activate (Windows)  
venv\Scripts\activate  

4. Install dependencies  
pip install -r requirements.txt  

5. Create .env file  
DATABASE_URL=postgresql://username:password@localhost:5432/authx_db  
SECRET_KEY=your_secret_key  
ALGORITHM=HS256  
ACCESS_TOKEN_EXPIRE_MINUTES=30  

6. Run server  
uvicorn main:app --reload  

Open Swagger UI:  
http://127.0.0.1:8000/docs  

## 🧠 What This Project Demonstrates

- Secure password management  
- Token-based authentication (JWT)  
- Refresh token implementation  
- Role-based authorization  
- Dependency injection in FastAPI  
- Clean backend service architecture  

## 📄 License

MIT License
