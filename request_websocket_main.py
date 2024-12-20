from typing import Literal

from pydantic import BaseModel

q3 = {
    "command": "authenticate_controls",
    "payload": {
        "action": "change_password",
        "content": {"username": "admin",
                    "organization": "Acme Inc.",
                    "password": "secret",
                    }
    },
}


class PayloadModel(BaseModel):
    action: Literal["login", "change_password"]
    content: dict


class RequestSchema(BaseModel):
    command: str
    payload: PayloadModel


class RequestWebSocket:

    @staticmethod
    def generate_request_data(command, action, user_id, settings=None, schedule=None):
        requests_body = {
            "command": command,
            "payload": {
                "action": action,
                "content": {"user_id": user_id, "settings": settings, "schedule": None}
            }
        }
        RequestSchema.model_validate(requests_body)
        return requests_body


if __name__ == "__main__":
    a = RequestWebSocket.generate_request_data(q3["command"], q3["payload"])
    print(type(a))
