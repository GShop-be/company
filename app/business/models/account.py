from sqlalchemy import Column, String

from .base import Base


__all__ = [
    'Account'
]


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)

