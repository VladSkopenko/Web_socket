from typing import Literal

from pydantic import BaseModel


class ProfileControlsPayload(BaseModel):
    """
    це пустишка просто для чека
    """

    action: Literal["view_profile", "update_profile"]
    content: dict
