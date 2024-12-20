import json
from dataclasses import dataclass
from typing import Literal

from pydantic import BaseModel


@dataclass
class StatusCode:
    SUCCESS = "success"
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


class StatusCodeSchema(BaseModel):
    status: Literal["success", "error", "warning", "info"]


class ResponseSchema(BaseModel):
    status: StatusCodeSchema
    message: str
    data: dict = None


class ResponseWebSocket:
    @staticmethod
    def success(message: str, data: dict = None):
        response_body = {
            "command": "message_controls",
            "message": message,
            "status": StatusCode.SUCCESS.value,
            "data": data
        }
        ResponseSchema.model_validate(response_body)
        return json.dumps(response_body)

    @staticmethod
    def error(message: str, data: dict = None):
        response_body = {
            "command": "message_controls",
            "message": message,
            "status": StatusCode.ERROR.value,
            "data": data
        }
        ResponseSchema.model_validate(response_body)
        return json.dumps(response_body)

    @staticmethod
    def warning(message: str, data: dict = None):
        response_body = {
            "command": "message_controls",
            "message": message,
            "status": StatusCode.WARNING.value,
            "data": data
        }
        ResponseSchema.model_validate(response_body)
        return json.dumps(response_body)

    @staticmethod
    def info(message: str, data: dict = None):
        response_body = {
            "command": "message_controls",
            "message": message,
            "status": StatusCode.INFO.value,
            "data": data
        }
        ResponseSchema.model_validate(response_body)
        return json.dumps(response_body)
