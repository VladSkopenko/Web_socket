from typing import ClassVar
from typing import Literal
from typing import Union

from pydantic import BaseModel
from pydantic import model_validator


class ProfileControlsPayload(BaseModel):
    """
    це пустишка просто для чека
    """

    action: Literal["view_profile", "update_profile"]
    content: dict
