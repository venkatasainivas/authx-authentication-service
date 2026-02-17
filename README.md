# AuthX – Authentication & Authorization Service
![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.129.0-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

AuthX is a secure authentication backend built using FastAPI and PostgreSQL.  
It provides user registration, login, password hashing, and JWT-based authentication using a clean and modular architecture.

---

## Features

- User registration with secure password hashing (bcrypt)
- Login with credential verification
- JWT-based access token generation
- PostgreSQL database integration
- SQLAlchemy ORM for database operations
- Environment-based configuration
- Clean layered project structure

---

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT (python-jose)
- Passlib (bcrypt)
- Alembic (planned for migrations)

---

## Project Structure

```
authx/
│
├── app/
│   ├── api/          # Route definitions
│   ├── core/         # Security & configuration
│   ├── db/           # Database connection
│   ├── models/       # SQLAlchemy models
│   ├── schemas/      # Pydantic schemas
│   ├── services/     # Business logic (future scope)
│   └── utils/
│
├── main.py           # Application entry point
├── .env              # Environment variables (not committed)
├── requirements.txt  # Dependencies
└── README.md
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/venkatasainivas/authx-authentication-service.git
cd authx-authentication-service
```

### 2. Create virtual environment

```
python -m venv venv
```

### 3. Activate virtual environment (Windows)

```
venv\Scripts\activate
```

### 4. Install dependencies

```
pip install -r requirements.txt
```

### 5. Create a `.env` file in the root directory

```
DATABASE_URL=postgresql://sainivas:password@localhost:5432/authx_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 6. Run the server

```
uvicorn main:app --reload
```

### 7. Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## Authentication Flow

1. Register a user  
2. Password is securely hashed using bcrypt  
3. Login verifies credentials  
4. JWT access token is generated  
5. Token is sent in the `Authorization: Bearer <token>` header for protected routes  

---

## Future Enhancements

- JWT protected routes  
- Refresh token system  
- Role-based access control (RBAC)  
- Docker containerization  
- Production deployment setup  

