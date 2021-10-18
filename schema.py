from typing import Optional, List

from pydantic import BaseModel
from pydantic import HttpUrl


class ShortenUrl(BaseModel):
    url: HttpUrl


class CreatShortenUrl(BaseModel):
    original_url: str
    short_link: str


class User(BaseModel):
    email: str
    id: int
    is_active: bool


class CreateUser(BaseModel):
    email: str
    password: str


class CreateUserResponse(BaseModel):
    success: bool
    data: Optional[User]


class CreateUserListResponse(BaseModel):
    success: bool
    data: List[User]
