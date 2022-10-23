from pydantic import BaseModel, EmailStr

__all__ = [
    'NewAccountRequest'
]


class NewAccountRequest(BaseModel):
    account_name: str
    super_user_name: str
    super_user_email: EmailStr
    password: str
    repeated_password: str
