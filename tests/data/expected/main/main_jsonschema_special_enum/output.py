# generated by datamodel-codegen:
#   filename:  special_enum.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel


class ModelEnum(Enum):
    True_ = True
    False_ = False
    field_ = ''
    field__1 = '\n'
    field__ = '\r\n'
    field__2 = '\t'
    field__3 = '\b'
    field__4 = '\\'


class Model(BaseModel):
    __root__: Optional[ModelEnum] = None
