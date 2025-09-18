from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.auth import SignupIn, LoginIn, TokenOut
from app.schemas.user import UserOut
from app.core.security import get_password_hash, verify_password, create_access_token
from app.core.deps import get_db
from app.crud.user import get_user_by_email, create_user

router = APIRouter()

@router.post("/signup", response_model=UserOut)
def signup(data: SignupIn, db: Session = Depends(get_db)):
    if get_user_by_email(db, data.email):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email já cadastrado")
    user = create_user(db, name=data.name, email=data.email, hashed_password=get_password_hash(data.password))
    return user


@router.post("/login", response_model=TokenOut)
def login(data: LoginIn, db: Session = Depends(get_db)):
    user = get_user_by_email(db, data.email)
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
    token = create_access_token(user.email)
    return TokenOut(access_token=token)