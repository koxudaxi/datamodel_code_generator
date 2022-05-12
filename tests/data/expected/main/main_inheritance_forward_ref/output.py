# generated by datamodel-codegen:
#   filename:  inheritance_forward_ref.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class DogBase(BaseModel):
    name: Optional[str] = Field(None, title='Name')
    woof: Optional[bool] = Field(True, title='Woof')


class PersonBase(BaseModel):
    name: Optional[str] = Field(None, title='Name')


class PersonsBestFriend(BaseModel):
    people: Optional[List[Person]] = Field(None, title='People')
    dogs: Optional[List[Dog]] = Field(None, title='Dogs')
    dog_base: Optional[DogBase] = None
    dog_relationships: Optional[DogRelationships] = None
    person_base: Optional[PersonBase] = None
    person_relationships: Optional[PersonRelationships] = None


class DogRelationships(BaseModel):
    people: Optional[List[Person]] = Field(None, title='People')


class PersonRelationships(BaseModel):
    people: Optional[List[Person]] = Field(None, title='People')


class Dog(DogBase, DogRelationships):
    pass


class Person(PersonBase, PersonRelationships):
    pass


PersonsBestFriend.update_forward_refs()
DogRelationships.update_forward_refs()
PersonRelationships.update_forward_refs()
Dog.update_forward_refs()
Person.update_forward_refs()
