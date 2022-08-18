from db_entities.session_maker import SessionMaker

from grpc_entities.client import GRPCClient

from .services import AccountService


__all__ = [
    'Business'
]


class Business:
    def __init__(
            self,
            session_maker: SessionMaker,
            grpc_client: GRPCClient
    ):
        self.account = AccountService(session_maker, grpc_client)
