from .business import Business
from .core import Core

__all__ = [
    'Application'
]


class Application:
    def __init__(self):
        self.core = Core()
        self.business = Business(
            self.core.session_maker,
            self.core.grpc_client,
        )

    async def start(self):
        await self.core.init()

        await self.business.account.add('TEST')
