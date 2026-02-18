from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.security import create_refresh_token


from app.db.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user
)

router = APIRouter(prefix="/auth", tags=["Authentication"])


# ==============================
# REGISTER
# ==============================
@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):

    # Check if email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash password
    hashed_pwd = hash_password(user.password)

    # Create new user
    new_user = User(
        email=user.email,
        hashed_password=hashed_pwd
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# ==============================
# LOGIN (OAuth2 Form)
# ==============================
@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    # Find user by email (username field carries email)
    db_user = db.query(User).filter(User.email == form_data.username).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Verify password
    if not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Create JWT token
    access_token = create_access_token(data={"sub": db_user.email})
    refresh_token = create_refresh_token(data={"sub": db_user.email})
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
}


# ==============================
# PROTECTED ROUTE
# ==============================
@router.get("/users/me")
def read_users_me(current_user: User = Depends(get_current_user)):

    return {
        "id": current_user.id,
        "email": current_user.email,
        "role": current_user.role,
        "is_active": current_user.is_active
    }

from app.core.security import require_admin


@router.get("/admin/dashboard")
def admin_dashboard(current_user: User = Depends(require_admin)):

    return {
        "message": "Welcome Admin",
        "email": current_user.email
    }


from jose import jwt, JWTError
from app.core.security import SECRET_KEY, ALGORITHM


@router.post("/refresh")
def refresh_token(refresh_token: str, db: Session = Depends(get_db)):

    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")

        if email is None:
            raise HTTPException(status_code=401, detail="Invalid refresh token")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    new_access_token = create_access_token(data={"sub": user.email})

    return {
        "access_token": new_access_token,
        "token_type": "bearer"
    }
