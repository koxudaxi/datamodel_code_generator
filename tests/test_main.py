from pathlib import Path
from tempfile import TemporaryDirectory

import pytest
from datamodel_code_generator.__main__ import Exit, main
from freezegun import freeze_time

DATA_PATH: Path = Path(__file__).parent / 'data'


@freeze_time('2019-07-26')
def test_main():
    with TemporaryDirectory() as output_dir:
        output_file: Path = Path(output_dir) / 'output.py'
        return_code: Exit = main(
            ['--input', str(DATA_PATH / 'api.yaml'), '--output', str(output_file)]
        )
        assert return_code == Exit.OK
        assert (
            output_file.read_text()
            == '''# generated by datamodel-codegen:
#   filename:  api.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from typing import List, Optional

from pydantic import BaseModel



class Pet(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None


class Pets(BaseModel):
    __root__: List[Pet] = None


class User(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None


class Users(BaseModel):
    __root__: List[User] = None


class Error(BaseModel):
    code: int
    message: str


class api(BaseModel):
    apiKey: Optional[str] = None
    apiVersionNumber: Optional[str] = None


class apis(BaseModel):
    __root__: List[api] = None
'''
        )

    with pytest.raises(SystemExit):
        main()
