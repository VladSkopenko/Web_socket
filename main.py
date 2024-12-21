from abc import ABC
from abc import abstractmethod
from typing import Dict
from typing import Type


class CommandHandler(ABC):
    @abstractmethod
    async def handle(self, payload, websocket, user, **kwargs):
        pass

    @abstractmethod
    async def validate_payload(self, payload):
        pass


class UpdateDataHandler(CommandHandler):
    async def handle(self, payload, websocket, user, **kwargs):
        data_type = payload.get("data_type")
        content = payload.get("content")
        print(f"Updating data: {data_type} with content: {content}")

    async def validate_payload(self, payload):
        pass


class AuthenticateHandler(CommandHandler):
    async def handle(self, payload, websocket, user, **kwargs):
        pass

    async def validate_payload(self, payload):
        pass


class ExecuteRobotHandler(CommandHandler):
    async def handle(self, payload, websocket, user, **kwargs):
        robot_id = payload.get("robot_id")
        print(f"Executing robot  with ID: {robot_id}")

    async def validate_payload(self, payload):
        pass


class MessageHandler(CommandHandler):
    async def handle(self, payload, websocket, user, **kwargs):
        message = payload.get("message")
        print(f"Sending message: {message}")

    async def validate_payload(self, payload):
        pass


class CommandHandlerFactory:
    handlers: Dict[str, Type[CommandHandler]] = {
        "profile_controls": UpdateDataHandler,
        "robot_controls": ExecuteRobotHandler,
        "authenticate_controls": AuthenticateHandler,
        "message_controls": MessageHandler,
    }

    @classmethod
    def get_handler(cls, command) -> CommandHandler:
        handler_class = cls.handlers.get(command)
        if handler_class is None:
            raise ValueError(f"Unknown command: {command}")
        return handler_class()
