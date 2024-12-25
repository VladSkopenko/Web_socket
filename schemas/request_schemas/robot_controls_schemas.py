from typing import ClassVar
from typing import Literal
from typing import Union
from uuid import UUID

from pydantic import BaseModel
from pydantic import model_validator


class ContentStartSchema(BaseModel):
    robot_id: UUID
    user_id: UUID


q2 = {
    "command": "robot_controls",
    "payload": {
        "action": "start/stop/pause/settings/schedule",
        "content": {
            "robot_id": 456,
            "user_id": 789,
            "settings": {"speed": 100, "file": "path/to/file"},
            "schedule": {
                "start_time": "2023-01-01 00:00:00",
                "end_time": "2023-01-01 00:00:00",
            },
        },
    },
}
