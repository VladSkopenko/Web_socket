from typing import Literal
from typing import Union

from pydantic import BaseModel
from pydantic import model_validator
from pydantic.v1 import root_validator


class ContentLoginSchema(BaseModel):
    username: str
    organization: str
    password: str


class ContentChangePasswordSchema(BaseModel):
    password: str


class PayloadModelAuthenticateControls(BaseModel):
    action: Literal["login", "change_password"]
    content: Union[ContentLoginSchema, ContentChangePasswordSchema]

    ACTION_TO_CONTENT_MODEL = {
        "login": ContentLoginSchema,
        "change_password": ContentChangePasswordSchema,
    }

    @model_validator(mode="before")
    @classmethod
    def validate_content(cls, values):
        action = values.get("action")
        content = values.get("content")

        if not isinstance(content, dict):
            raise ValueError("Content must be a dictionary.")

        content_model = cls.ACTION_TO_CONTENT_MODEL.get(action)
        if not content_model:
            raise ValueError(f"Unsupported action: {action}")

        content_model(**content)
        return values


class ProfileControlsPayload(BaseModel):
    """
    це пустишка просто для чека
    """

    action: Literal["view_profile", "update_profile"]
    content: dict


class RequestSchema(BaseModel):
    command: Literal[
        "authenticate_controls",
        "profile_controls",
        "robot_controls",
        "message_controls",
    ]
    payload: Union[PayloadModelAuthenticateControls, ProfileControlsPayload]

    COMMAND_TO_PAYLOAD_MODEL = {
        "authenticate_controls": PayloadModelAuthenticateControls,
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
            "action": "change_password",
            "content": {
                "username": "admin",
                "organization": "Acme Inc.",
                "password": "secret",
            },
        },
    }

    request = RequestSchema(**q1)
