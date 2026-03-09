# AuthX — Authentication & Authorization Service

A production-style authentication backend built with FastAPI and PostgreSQL.

## Tech Stack
- FastAPI
- PostgreSQL + SQLAlchemy
- JWT Authentication (python-jose)
- OAuth2 Password Flow
- Passlib (bcrypt)
- Role Based Access Control

## Features
- Secure user registration with bcrypt password hashing
- JWT access token generation
- Refresh token system for session renewal
- Protected routes using dependency injection
- Role based access control (Admin/User)

## Setup
```bash
git clone https://github.com/venkatasainivas/authx-authentication-service.git
cd authx-authentication-service

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

Create `.env` file:
```env
DATABASE_URL=postgresql://username:password@localhost:5432/authx_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Run server:
```bash
uvicorn main:app --reload
```

## API Endpoints
- POST /auth/register → Register new user
- POST /auth/login → Login and receive tokens
- POST /auth/refresh → Generate new access token
- GET /auth/users/me → Get current user (Protected)
- GET /auth/admin/dashboard → Admin only route

## API Docs
http://127.0.0.1:8000/docs

## License
MIT
