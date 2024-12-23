from typing import ClassVar
from typing import Literal
from typing import Union

from pydantic import BaseModel
from pydantic import model_validator


class ContentLoginSchema(BaseModel):
    username: str
    organization: str
    password: str


class ContentChangePasswordSchema(BaseModel):
    password: str


class AuthenticationPayload(BaseModel):
    action: Literal["login", "change_password"]
    content: Union[ContentLoginSchema, ContentChangePasswordSchema]

    ACTION_TO_CONTENT_MODEL: ClassVar[dict[str, type]] = {
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



