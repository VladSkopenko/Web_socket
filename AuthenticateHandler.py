from abc import ABC
from abc import abstractmethod
from typing import Any
from schemas.auth_schema import AuthControlsPayloadSchema


class CommandHandler(ABC):
    @abstractmethod
    async def handle_action(self, payload: Any, websocket, user) -> dict:
        pass


class AuthenticateHandler(CommandHandler):

    def __init__(self):
        self.AUTHENTICATE = {
            "login": self.login,
            "change_password": self.change_password,
        }

    async def handle_action(self, payload: AuthControlsPayloadSchema, websocket, user) -> dict:
        handler = self.AUTHENTICATE.get(payload.action)
        if handler is None:
            return {"status": "error", "message": f"Action '{payload.action}' is not supported"}

        return await handler(payload, websocket, user)

    @staticmethod
    async def change_password(payload, websocket, user) -> dict:
        ...

    @staticmethod
    async def login(self, payload, websocket, user) -> dict:
        ...
