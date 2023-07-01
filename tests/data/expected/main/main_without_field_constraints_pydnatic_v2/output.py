# generated by datamodel-codegen:
#   filename:  api_constrained.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import List, Optional, Union, Set

from pydantic import AnyUrl, BaseModel, Field, confloat, conint, constr, RootModel


class Pet(BaseModel):
    id: conint(ge=0, le=9223372036854775807)
    name: constr(max_length=256)
    tag: Optional[constr(max_length=64)] = None


class Pets(RootModel):
    root: Set[Pet] = Field(..., max_length=10, min_length=1)


class UID(RootModel):
    root: conint(ge=0)


class Phone(RootModel):
    root: constr(min_length=3)


class User(BaseModel):
    id: conint(ge=0)
    name: constr(max_length=256)
    tag: Optional[constr(max_length=64)] = None
    uid: UID
    phones: Optional[List[Phone]] = Field(None, max_items=10)
    fax: Optional[List[constr(min_length=3)]] = None
    height: Optional[Union[conint(ge=1, le=300), confloat(ge=1.0, le=300.0)]] = None
    weight: Optional[Union[confloat(ge=1.0, le=1000.0), conint(ge=1, le=1000)]] = None
    age: Optional[conint(le=200, gt=0)] = None
    rating: Optional[confloat(le=5.0, gt=0.0)] = None


class Users(RootModel):
    root: List[User]


class Id(RootModel):
    root: str


class Rules(RootModel):
    root: List[str]


class Error(BaseModel):
    code: int
    message: str


class Api(BaseModel):
    apiKey: Optional[str] = Field(
        None, description='To be used as a dataset parameter value'
    )
    apiVersionNumber: Optional[str] = Field(
        None, description='To be used as a version parameter value'
    )
    apiUrl: Optional[AnyUrl] = Field(
        None, description="The URL describing the dataset's fields"
    )
    apiDocumentationUrl: Optional[AnyUrl] = Field(
        None, description='A URL to the API console for each API'
    )


class Apis(RootModel):
    root: List[Api]


class Event(BaseModel):
    name: Optional[str] = None


class Result(BaseModel):
    event: Optional[Event] = None
