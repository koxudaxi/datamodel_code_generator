# generated by datamodel-codegen:
#   filename:  modular.yaml
#   timestamp: 1985-10-26T08:21:00+00:00

from __future__ import annotations

from collections.abc import Sequence
from typing import Optional

from pydantic import BaseModel

from .. import Id, OptionalModel


class Tea(BaseModel):
    flavour: Optional[str] = None
    id: Optional[Id] = None
    self: Optional[Tea] = None
    optional: Optional[Sequence[OptionalModel]] = None


class TeaClone(BaseModel):
    flavour: Optional[str] = None
    id: Optional[Id] = None
    self: Optional[Tea] = None
    optional: Optional[Sequence[OptionalModel]] = None


class List(BaseModel):
    __root__: Sequence[Tea]


Tea.update_forward_refs()
