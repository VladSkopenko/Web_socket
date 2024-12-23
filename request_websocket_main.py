from typing import Literal

from pydantic import BaseModel

q3 = {
    "command": "authenticate_controls",
    "payload": {
        "action": "change_password" or "login",
        "content": {
            "username": "admin",
            "organization": "Acme Inc.",
            "user_id": 789,
            "password": "secret",
        },
    },
}


class ContentModel(BaseModel):
    username: str
    organization: str
    password: str


class PayloadModel(BaseModel):
    action: Literal["login", "change_password"]
    content: dict


class CommandSchema(BaseModel):
    command: Literal[
        "authenticate_controls",
        "profile_controls",
        "robot_controls",
        "message_controls",
    ]


class RequestSchema(BaseModel):
    command: CommandSchema
    payload: PayloadModel


class RequestWebSocket:

    @staticmethod
    def generate_request_data(command, payload):
        requests_body = {
            "command": command,
            "payload": payload,
        }
        RequestSchema.model_validate(requests_body)
        return requests_body


if __name__ == "__main__":
    a = RequestWebSocket.generate_request_data(q3["command"], q3["payload"])
    print(type(a))
