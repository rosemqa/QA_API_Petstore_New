from pydantic import BaseModel, EmailStr, Field


class UserModel(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int


class ApiResponseModel(BaseModel):
    code: int
    type: str
    message: str


class AuthHeadersModel(BaseModel):
    x_expires_after: str = Field(..., alias='X-Expires-After')
    x_rate_limit: int = Field(..., alias='X-Rate-Limit')
