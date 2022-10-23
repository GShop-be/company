from .business import Business, Base
from .business.services.account.requests import NewAccountRequest
from .core import Core

__all__ = [
    'Application'
]


class Application:
    def __init__(self):
        self.core = Core(Base.metadata)
        self.business = Business(
            self.core.session_maker,
            self.core.external_connectors,
        )

    async def start(self):
        await self.core.init()

        await self.business.account.add(NewAccountRequest(
            account_name='test12',
            super_user_name='test_super_user',
            super_user_email='test@test.ru',
            password='test',
            repeated_password='test'
        ))
