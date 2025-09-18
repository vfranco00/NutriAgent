from pydantic import BaseModel
import uuid

class PreferenceCreate(BaseModel):
    type: str
    value: str

class PreferenceOut(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    type: str
    value: str
    class Config:
        from_attributes = True