# Python
from uuid import UUID
from datetime import date, datetime
from typing import Optional

# Pydantic
from pydantic import BaseModel, Field, EmailStr

class UserBase(BaseModel):

    id: UUID = Field(...,)

    email: EmailStr = Field(...,)


class User(UserBase):

    first_name: str = Field(...,
                            title='First name',
                            min_length=2,
                            max_length=50,
                            example='John',)

    last_name: str = Field(...,
                           title='Last name',
                           min_length=2,
                           max_length=50,
                           example='Doe',)

    birth_date: Optional[date] = Field(default=None,
                                       title='Birth date',
                                       example='2021-01-01',)


class UserLogin(UserBase):

    password: str = Field(...,
                          min_length=8,
                          max_length=64,
                          example='password',)


class Tweet(BaseModel):

    id: UUID = Field(...)

    content: str = Field(...,
                         min_length=1,
                         max_length=256,)

    created_at: datetime = Field(default=datetime.now(),
                                title='Creation date',
                                example='2020-01-01T00:00:00Z',)

    updated_at: Optional[datetime] = Field(default=None,
                                           title='Last update date',
                                           example='2020-01-01T00:00:00Z',)

    created_by: User = Field(...,
                             title='User who created the tweet',)
