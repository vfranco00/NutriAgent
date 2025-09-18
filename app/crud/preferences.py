from sqlalchemy.orm import Session
from app.models.preferences import DietaryPreference
from app.schemas.preferences import PreferenceCreate

def create_preference(db: Session, user_id, data: PreferenceCreate) -> DietaryPreference:
    p = DietaryPreference(user_id=user_id, type=data.type, value=data.value)
    db.add(p)
    db.commit()
    db.refresh(p)
    return p

def list_preferences(db: Session, user_id) -> list[DietaryPreference]:
    return db.query(DietaryPreference).filter(DietaryPreference.user_id == user_id).all()