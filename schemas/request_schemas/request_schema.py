from typing import ClassVar
from typing import Literal
from typing import Union

from pydantic import BaseModel
from pydantic import model_validator

from schemas.request_schemas.authenticate_controls import AuthenticationPayload
from schemas.request_schemas.profile_controls_schemas import ProfileControlsPayload


class RequestSchema(BaseModel):
    command: Literal[
        "authenticate_controls",
        "profile_controls",
        "robot_controls",
        "message_controls",
    ]
    payload: Union[AuthenticationPayload, ProfileControlsPayload]

    COMMAND_TO_PAYLOAD_MODEL: ClassVar[dict[str, type]] = {
        "authenticate_controls": AuthenticationPayload,
        "profile_controls": ProfileControlsPayload,
    }

    @model_validator(mode="before")
    @classmethod
    def validate_payload(cls, values):
        command = values.get("command")
        payload = values.get("payload")

        if not isinstance(payload, dict):
            raise ValueError("Payload must be a dictionary.")

        payload_model = cls.COMMAND_TO_PAYLOAD_MODEL.get(command)
        if payload_model is None:
            raise ValueError(f"Unsupported command: {command}")
        payload_model(**payload)

        return values


if __name__ == "__main__":
    q1 = {
        "command": "authenticate_controls",
        "payload": {
            "action": "login",
            "content": {
                "username": "admin",
                "organization": "Acme Inc.",
                "password": "secret",
            },
        },
    }

    request = RequestSchema(**q1)
    print(request)
