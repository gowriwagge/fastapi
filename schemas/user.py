from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserSchema(BaseModel):
    """Schema for creating a new user."""
    name: str = Field(..., min_length=2, max_length=50, description="Full name of the user")
    email: EmailStr = Field(..., description="Valid email address")
    password: str = Field(..., min_length=8, max_length=128, description="Password with at least 8 characters")
    address: Optional[str] = Field(None, max_length=255, description="User's address")
    phone_number: Optional[str] = Field(
        None, 
        pattern=r"^\+?[1-9]\d{1,14}$",  # ✅ FIX: Use `pattern` instead of `regex`
        description="Valid phone number with optional country code"
    )

class UpdateUserSchema(BaseModel):
    """Schema for updating user details (partial update)."""
    name: Optional[str] = Field(None, min_length=2, max_length=50, description="Updated name")
    email: Optional[EmailStr] = Field(None, description="Updated email address")
    password: Optional[str] = Field(None, min_length=8, max_length=128, description="Updated password")
    address: Optional[str] = Field(None, max_length=255, description="Updated address")
    phone_number: Optional[str] = Field(
        None, 
        pattern=r"^\+?[1-9]\d{1,14}$",  # ✅ FIX: Use `pattern`
        description="Updated phone number with optional country code"
    )

    class Config:
        from_attributes = True  # ✅ Pydantic v2 equivalent for `orm_mode`
