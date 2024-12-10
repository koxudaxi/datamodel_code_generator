# generated by datamodel-codegen:
#   filename:  discriminator_literals.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import Literal, Optional, Union

from pydantic import BaseModel, Field


class Type1(BaseModel):
    type_: Literal['a'] = Field('a', title='Type ')


class Type2(BaseModel):
    type_: Literal['b'] = Field('b', title='Type ')


class UnrelatedType(BaseModel):
    info: Optional[str] = Field(
        'Unrelated type, not involved in the discriminated union',
        title='A way to check for side effects',
    )


class Response(BaseModel):
    inner: Union[Type1, Type2] = Field(..., discriminator='type_', title='Inner')
