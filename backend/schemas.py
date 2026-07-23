from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class FeatureImportance(BaseModel):
    feature: str
    importance: float

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_admin: bool
    created_at: datetime

    class Config:
        orm_mode = True

# ... [keep existing schemas] ...