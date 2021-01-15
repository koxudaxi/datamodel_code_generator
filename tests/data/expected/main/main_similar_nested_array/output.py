# generated by datamodel-codegen:
#   filename:  similar_nested_array.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, List, Optional, Union

from pydantic import BaseModel


class Model(BaseModel):
    __root__: Any


class Datum(BaseModel):
    keyA: Optional[str] = None


class ObjectA(BaseModel):
    data: Optional[List[Datum]] = None


class Datum1(BaseModel):
    keyB: Optional[str] = None


class ObjectB(BaseModel):
    data: Optional[List[Datum1]] = None


class KeyCItem(BaseModel):
    nestedA: Optional[str] = None


class KeyCItem1(BaseModel):
    nestedB: Optional[str] = None


class ObjectC(BaseModel):
    keyC: Optional[Union[KeyCItem, KeyCItem1]] = None


class KeyCItem2(BaseModel):
    nestedA: Optional[str] = None


class KeyCItem3(BaseModel):
    nestedB: Optional[str] = None


class KeyCEnum(Enum):
    dog = 'dog'
    cat = 'cat'
    snake = 'snake'


class KeyCEnum1(Enum):
    orange = 'orange'
    apple = 'apple'
    milk = 'milk'


class ObjectD(BaseModel):
    keyC: Optional[List[Union[KeyCItem2, KeyCItem3, KeyCEnum, KeyCEnum1]]] = None
