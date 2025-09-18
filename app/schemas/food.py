from pydantic import BaseModel
import uuid

class FoodBase(BaseModel):
    name: str
    category: str | None = None
    kcal_per_100g: float | None = None
    protein_g: float | None = None
    fat_g: float | None = None
    carbs_g: float | None = None

class FoodCreate(FoodBase):
    pass

class FoodOut(FoodBase):
    id: uuid.UUID
    class Config:
        from_attributes = True