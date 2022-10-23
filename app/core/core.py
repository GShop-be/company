from db_entities.session_maker import SessionMaker
from db_entities.initilaizer import Initializer
from settings import Settings

from .external_connectors import ExternalConnectors




__all__ = [
    'Core'
]


class Core:
    def __init__(self, metadata):
        self.session_maker = SessionMaker(
            driver='postgresql+asyncpg',
            user=Settings.db.common.user,
            password=Settings.db.common.password,
            host=Settings.db.common.host,
            port=Settings.db.common.port,
            db_name=Settings.db.common.db_name,
            is_async=True
        )
        self._initializer = Initializer(
            self.session_maker,
            metadata,
            Settings.ALEMBIC_CONFIG_PATH
        )

        self.external_connectors = ExternalConnectors()

    async def init(self):
        await self._initializer.initialize()
