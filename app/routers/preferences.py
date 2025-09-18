from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db, get_current_user
from app.schemas.preferences import PreferenceCreate, PreferenceOut
from app.crud.preferences import create_preference, list_preferences

router = APIRouter()

@router.post("/", response_model=PreferenceOut)
def create_pref(data: PreferenceCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return create_preference(db, user.id, data)

@router.get("/", response_model=list[PreferenceOut])
def my_prefs(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return list_preferences(db, user.id)