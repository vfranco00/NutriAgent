from sqlalchemy.orm import Session
from app.models.user import User

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, name: str, email: str, hashed_password: str) -> User:
    u = User(name=name, email=email, hashed_password=hashed_password)
    db.add(u)
    db.commit()
    db.refresh(u)
    return u