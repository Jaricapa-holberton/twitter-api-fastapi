# Python
from uuid import UUID
from datetime import date, datetime
from typing import Optional

# Pydantic
from pydantic import BaseModel
from pydantic import Field, EmailStr


class User(BaseModel):
    user_id: UUID = Field(..., alias="id")
    email: EmailStr = Field(..., example="Jhon@doe.com")
    first_name: str = Field(..., min_length=2, max_length=50, example="John")
    last_name: str = Field(..., min_length=2, max_length=50, example="Doe")
    birthday: Optional[date] = Field(default=None)


class UserIn(User):
    password: str = Field(..., min_length=8, max_length=30)


class UserOut(User):
    pass


class Tweet(BaseModel):
    tweet_id: UUID = Field(..., alias="Tweet id")
    content: str = Field(..., min_length=2, max_length=240, example="Hello World")
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: UserIn = Field(..., alias="User")
