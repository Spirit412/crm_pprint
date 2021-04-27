from typing import Optional, List

from pydantic import BaseModel, Field, validator
from datetime import datetime


class UserSchema(BaseModel):
    # id: str = Field(None, )
    email: str = Field(..., description='почта пользователя')
    name: str = Field(..., description='имя пользователя')
    created_on: datetime = Field(None, description='дата создания пользователя')
    updated_on: datetime = Field(None, description='дата обновления данных пользователя')
    is_active: bool = Field(None, description='вкл/откл пользователь')
    role_user: Optional['RoleSchema']
    description: str = Field(None, description='описание')

    class Config:
        orm_mode = True


class RoleSchema(BaseModel):
    # id: str
    role: str
    description: str = Field(None, description='описание')

    # 
    class Config:
        orm_mode = True


class AuthUserSchema(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    token: str


class LoginUserSchema(BaseModel):
    email: str
    name: str
    role_user: Optional['RoleSchema']
    description: str = Field(None, description='описание')
    token: str

    class Config:
        orm_mode = True


class MeSchema(BaseModel):
    email: str
    name: str
    role_user: Optional['RoleSchema']
    description: str = Field(None, description='описание')

    class Config:
        orm_mode = True


class AuthUserSchema(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "email": "1test@test.ru",
                "password": "123456"
            }
        }


class RegUserSchema(BaseModel):
    email: str = Field(..., )
    name: str
    password: str
    description: str = Field(None, description='описание')

    @validator('email')
    def name_must_contain_space(cls, v):
        if '@' not in v:
            raise ValueError('must contain a @')
        return v

    class Config:
        # orm_mode = True

        schema_extra = {
            "example": {
                "email": "1test@test.ru",
                "name": "1test_reg",
                "password": "123456",
                "description": "1 тест"
            }
        }



