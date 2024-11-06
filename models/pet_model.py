from typing import Optional

from pydantic import BaseModel, Field


class Tag(BaseModel):
    id: int
    name: Optional[str] = None


class Category(BaseModel):
    id: int
    name: Optional[str] = None


class PetModel(BaseModel):
    id: int
    category: Optional[Category] = None
    name: Optional[str] = None
    photoUrls: Optional[list[str | None]] = None
    tags: Optional[list[Tag]] = None
    status: Optional[str] = None


class PetListModel(BaseModel):
    items: list[PetModel]


class ApiResponseModel(BaseModel):
    code: int
    type: str
    message: str
