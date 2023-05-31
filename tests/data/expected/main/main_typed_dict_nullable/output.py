# generated by datamodel-codegen:
#   filename:  nullable.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import List, NotRequired, Optional, TypedDict


class Cursors(TypedDict):
    prev: str
    next: NotRequired[Optional[str]]
    index: float
    tag: NotRequired[Optional[str]]


class TopLevel(TypedDict):
    cursors: Cursors


class Info(TypedDict):
    name: str


class User(TypedDict):
    info: Info


class Api(TypedDict):
    apiKey: NotRequired[Optional[str]]
    apiVersionNumber: NotRequired[Optional[str]]
    apiUrl: NotRequired[Optional[str]]
    apiDocumentationUrl: NotRequired[Optional[str]]


Apis = Optional[List[Api]]


class EmailItem(TypedDict):
    author: str
    address: str
    description: NotRequired[Optional[str]]
    tag: NotRequired[Optional[str]]


Email = List[EmailItem]


Id = int


Description = Optional[str]


Name = Optional[str]


Tag = str


class Notes(TypedDict):
    comments: NotRequired[List[str]]
