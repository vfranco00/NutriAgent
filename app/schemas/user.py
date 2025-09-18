from pydantic import BaseModel, EmailStr
import uuid

class UserOut(BaseModel):
    id: uuid.UUID
    name: str
    email: EmailStr

    class Config:
        orm_mode = True