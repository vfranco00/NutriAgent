from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.core.deps import get_db, get_current_user
from app.schemas.food import FoodCreate, FoodOut
from app.crud.food import create_food, get_foods, get_food, delete_food

router = APIRouter()

@router.post("/", response_model=FoodOut)
def create_food_endpoint(data: FoodCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return create_food(db, data)

@router.get("/", response_model=list[FoodOut])
def list_foods(q: str | None = Query(None), db: Session = Depends(get_db), user=Depends(get_current_user)):
    return get_foods(db, q)

@router.get("/{food_id}", response_model=FoodOut)
def get_food_by_id(food_id: str, db: Session = Depends(get_db), user=Depends(get_current_user)):
    f = get_food(db, food_id)
    if not f:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Food not found")
    return f

@router.delete("/{food_id}")
def delete_food_by_id(food_id: str, db: Session = Depends(get_db), user=Depends(get_current_user)):
    ok = delete_food(db, food_id)
    if not ok:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Food not found")
    return {"deleted": True}