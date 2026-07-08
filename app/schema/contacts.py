from pydantic import BaseModel , Field , field_validator
from typing import Optional
from enum import Enum

class Category(str , Enum):
    personal = "personal"
    work = "work"
    family = "family"


class ContactCreate(BaseModel):
    first_name : str = Field(min_length=1, max_length=50)
    last_name : str = Field(min_length=1, max_length=50)
    email : str
    phone : Optional[str] = Field(default=None,min_length=10, max_length=15)
    category : Category

    @field_validator("email")
    @classmethod
    def email_must_contain(cls , v):
        if "@" not in v:
            raise ValueError("must be a valid email address")
        return v
    
class ContactUpdate(BaseModel):
    first_name : Optional[str] = Field(default=None,min_length=1, max_length=50)
    last_name : Optional[str] = Field(default=None,min_length=1, max_length=50)
    email : Optional[str] = None
    phone : Optional[str] = Field(default=None,min_length=10, max_length=15)
    category : Optional[Category] = None

    @field_validator("email")
    @classmethod
    def email_must_contain(cls , v):
        if "@" not in v:
            raise ValueError("must be a valid email address")
        return v

class ContactResponse(BaseModel):
    id: int
    first_name : str
    last_name : str 
    email : str
    phone : Optional[str]
    category : Category
    created_at: str
