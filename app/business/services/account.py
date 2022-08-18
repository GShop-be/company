from uuid import uuid4

from grpc_entities.client import GRPCClient
from db_entities.session_maker import SessionMaker
from repositories.local import LocalRepository

from grpc_metadata.company_to_employees_pb2_grpc import EmployeesServiceStub
from grpc_metadata.company_to_employees_pb2 import UserRequest

from ..models import Account


__all__ = [
    'AccountService'
]


class AccountService:
    def __init__(
        self,
        session_maker: SessionMaker,
        grpc_client: GRPCClient
    ):
        self._session_maker = session_maker
        self._multi_repository = LocalRepository(self._session_maker)
        self._grpc_client = grpc_client

    async def add(self, account_name: str) -> Account:
        account = Account(
            id=uuid4().hex,
            name=account_name
        )

        await self._multi_repository.add(account)

        async with self._grpc_client.begin(EmployeesServiceStub) as stub:
            response = await stub.CreateUser(UserRequest(
                name='test'
            ))


        return account

    async def delete(self, id_: str) -> None:
        account = await self._multi_repository.find_one(Account, Account.id == id_)
        await self._multi_repository.delete(account)

