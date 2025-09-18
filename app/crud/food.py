from sqlalchemy.orm import Session
from app.models.food import Food
from app.schemas.food import FoodCreate

def create_food(db: Session, data: FoodCreate) -> Food:
    f = Food(**data.dict())
    db.add(f)
    db.commit()
    db.refresh(f)
    return f

def get_foods(db: Session, q: str | None = None) -> list[Food]:
    query = db.query(Food)
    if q:
        query = query.filter(Food.name.ilike(f"%{q}%"))
    return query.order_by(Food.name.asc()).all()

def get_food(db: Session, food_id):
    return db.query(Food).get(food_id)

def delete_food(db: Session, food_id) -> bool:
    f = db.query(Food).get(food_id)
    if not f:
        return False
    db.delete(f)
    db.commit()
    return True