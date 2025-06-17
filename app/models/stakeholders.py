from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class StakeholderSignup(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)
    user_id: Optional[str] = Field(None, description="- set after authentication")
    role: Optional[str] = Field(None, description="defaults to 'user' if not specified")
    
class LoginPayload(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    message: str
    access_token: str
    refresh_token: str
    user: dict
    expires_in: int