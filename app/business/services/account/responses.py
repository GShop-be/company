from pydantic import BaseModel, EmailStr

__all__ = [
    'NewAccountResponse',
    'SuperUserData',
    'AccountData'
]


class AccountData(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True


class SuperUserData(BaseModel):
    name: str
    email: EmailStr
    role: str

    class Config:
        orm_mode = True


class NewAccountResponse(BaseModel):
    account_data: AccountData
    super_user_data: SuperUserData


