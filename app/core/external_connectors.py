from communications.grpc import GRPCClient


__all__ = [
    'ExternalConnectors'
]


class ExternalConnectors:

    def __init__(self):
        self.external_employees = GRPCClient()
