from db_entities.session_maker import SessionMaker

from .services import AccountService

from ..core import ExternalConnectors


__all__ = [
    'Business'
]


class Business:
    def __init__(
        self,
        session_maker: SessionMaker,
        external_connectors: ExternalConnectors
    ):
        self.account = AccountService(session_maker, external_connectors.external_employees)
