from datetime import datetime
from pydantic import BaseModel


class OrderModel(BaseModel):
    id: int
    petId: int
    quantity: int
    shipDate: datetime
    status: str
    complete: bool


class ApiResponseModel(BaseModel):
    code: int
    type: str
    message: str
