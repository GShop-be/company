from uuid import uuid4

from communications.errors import BaseError
from communications.grpc import GRPCClient
from db_entities.session_maker import SessionMaker
from repositories.local import LocalRepository

from grpc_metadata.company_to_employees_pb2_grpc import EmployeesServiceStub
from grpc_metadata.company_to_employees_pb2 import SuperUserRequest

from .requests import NewAccountRequest
from .responses import NewAccountResponse, SuperUserData, AccountData

from ...models import Account


__all__ = [
    'AccountService'
]


class AccountService:
    def __init__(
        self,
        session_maker: SessionMaker,
        external_employees: GRPCClient
    ):
        self._session_maker = session_maker
        self._multi_repository = LocalRepository(self._session_maker)
        self._external_employees = external_employees

    async def add(self, request: NewAccountRequest) -> NewAccountResponse | BaseError:
        account = Account(
            id=uuid4().hex,
            name=request.account_name
        )

        #await self._multi_repository.add(account)

        super_user, error = await self._external_employees.call(
            EmployeesServiceStub,
            'CreateSuperUser',
            request=SuperUserRequest(
                name=request.super_user_name,
                email=request.super_user_email,
                password=request.password,
                repeat_password=request.repeated_password
            ),
            metadata={'account-id': account.id},
            attach_default_metadata=False
        )

        if error:
            raise error

        return NewAccountResponse(
            account_data=AccountData.from_orm(account),
            super_user_data=SuperUserData.from_orm(super_user),
        )

    async def delete(self, id_: str) -> None:
        account = await self._multi_repository.find_one(Account, Account.id == id_)
        await self._multi_repository.delete(account)

