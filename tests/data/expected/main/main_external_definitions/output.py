# generated by datamodel-codegen:
#   filename:  external_definitions_root.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from pydantic import BaseModel, constr


class ElegantName(BaseModel):
    __root__: constr(min_length=3)


class Person(BaseModel):
    name: ElegantName
