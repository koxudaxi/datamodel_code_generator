import shutil
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Mapping

import pytest
from _pytest.capture import CaptureFixture
from _pytest.tmpdir import TempdirFactory
from datamodel_code_generator.__main__ import Exit, main
from freezegun import freeze_time

DATA_PATH: Path = Path(__file__).parent / 'data'
TIMESTAMP = '1985-10-26T01:21:00-07:00'


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

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, UrlStr


class Pet(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None


class Pets(BaseModel):
    __root__: List[Pet]


class User(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None


class Users(BaseModel):
    __root__: List[User]


class Id(BaseModel):
    __root__: str


class Rules(BaseModel):
    __root__: List[str]


class Error(BaseModel):
    code: int
    message: str


class api(BaseModel):
    apiKey: Optional[str] = None
    apiVersionNumber: Optional[str] = None
    apiUrl: Optional[UrlStr] = None
    apiDocumentationUrl: Optional[UrlStr] = None


class apis(BaseModel):
    __root__: List[api]


class Event(BaseModel):
    name: Optional[str] = None


class Result(BaseModel):
    event: Optional[Event] = None
'''
        )

    with pytest.raises(SystemExit):
        main()


@freeze_time('2019-07-26')
def test_main_base_class():
    with TemporaryDirectory() as output_dir:
        output_file: Path = Path(output_dir) / 'output.py'
        return_code: Exit = main(
            [
                '--input',
                str(DATA_PATH / 'api.yaml'),
                '--output',
                str(output_file),
                '--base-class',
                'custom_module.Base',
            ]
        )
        assert return_code == Exit.OK
        assert (
            output_file.read_text()
            == '''# generated by datamodel-codegen:
#   filename:  api.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import UrlStr

from custom_module import Base


class Pet(Base):
    id: int
    name: str
    tag: Optional[str] = None


class Pets(Base):
    __root__: List[Pet]


class User(Base):
    id: int
    name: str
    tag: Optional[str] = None


class Users(Base):
    __root__: List[User]


class Id(Base):
    __root__: str


class Rules(Base):
    __root__: List[str]


class Error(Base):
    code: int
    message: str


class api(Base):
    apiKey: Optional[str] = None
    apiVersionNumber: Optional[str] = None
    apiUrl: Optional[UrlStr] = None
    apiDocumentationUrl: Optional[UrlStr] = None


class apis(Base):
    __root__: List[api]


class Event(Base):
    name: Optional[str] = None


class Result(Base):
    event: Optional[Event] = None
'''
        )

    with pytest.raises(SystemExit):
        main()


@freeze_time('2019-07-26')
def test_target_python_version():
    with TemporaryDirectory() as output_dir:
        output_file: Path = Path(output_dir) / 'output.py'
        return_code: Exit = main(
            [
                '--input',
                str(DATA_PATH / 'api.yaml'),
                '--output',
                str(output_file),
                '--target-python-version',
                '3.6',
            ]
        )
        assert return_code == Exit.OK
        assert (
            output_file.read_text()
            == '''# generated by datamodel-codegen:
#   filename:  api.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from typing import List, Optional

from pydantic import BaseModel, UrlStr


class Pet(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None


class Pets(BaseModel):
    __root__: List['Pet']


class User(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None


class Users(BaseModel):
    __root__: List['User']


class Id(BaseModel):
    __root__: str


class Rules(BaseModel):
    __root__: List[str]


class Error(BaseModel):
    code: int
    message: str


class api(BaseModel):
    apiKey: Optional[str] = None
    apiVersionNumber: Optional[str] = None
    apiUrl: Optional[UrlStr] = None
    apiDocumentationUrl: Optional[UrlStr] = None


class apis(BaseModel):
    __root__: List['api']


class Event(BaseModel):
    name: Optional[str] = None


class Result(BaseModel):
    event: Optional['Event'] = None
'''
        )

    with pytest.raises(SystemExit):
        main()


@pytest.mark.parametrize(
    'expected',
    [
        {
            (
                '__init__.py',
            ): '''\
# generated by datamodel-codegen:
#   filename:  modular.yaml
#   timestamp: 1985-10-26T08:21:00+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from . import models


class Id(BaseModel):
    __root__: str


class Error(BaseModel):
    code: int
    message: str


class Result(BaseModel):
    event: Optional[models.Event] = None
''',
            (
                'models.py',
            ): '''\
# generated by datamodel-codegen:
#   filename:  modular.yaml
#   timestamp: 1985-10-26T08:21:00+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, Optional, Union

from pydantic import BaseModel


class Species(Enum):
    dog = 'dog'
    cat = 'cat'
    snake = 'snake'


class Pet(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None
    species: Optional[Species] = None


class User(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None


class Event(BaseModel):
    name: Optional[Union[str, float, int, bool, Dict[str, Any]]] = None
''',
            (
                'collections.py',
            ): '''\
# generated by datamodel-codegen:
#   filename:  modular.yaml
#   timestamp: 1985-10-26T08:21:00+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, UrlStr

from . import models


class Pets(BaseModel):
    __root__: List[models.Pet]


class Users(BaseModel):
    __root__: List[models.User]


class Rules(BaseModel):
    __root__: List[str]


class api(BaseModel):
    apiKey: Optional[str] = None
    apiVersionNumber: Optional[str] = None
    apiUrl: Optional[UrlStr] = None
    apiDocumentationUrl: Optional[UrlStr] = None


class apis(BaseModel):
    __root__: List[api]
''',
            (
                'foo',
                '__init__.py',
            ): '''\
# generated by datamodel-codegen:
#   filename:  modular.yaml
#   timestamp: 1985-10-26T08:21:00+00:00
''',
            (
                'foo',
                'bar.py',
            ): '''\
# generated by datamodel-codegen:
#   filename:  modular.yaml
#   timestamp: 1985-10-26T08:21:00+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class Thing(BaseModel):
    attributes: Optional[Dict[str, Any]] = None


class Thang(BaseModel):
    attributes: Optional[List[Dict[str, Any]]] = None


class Clone(Thing):
    pass
''',
        }
    ],
)
def test_main_modular(
    tmpdir_factory: TempdirFactory, expected: Mapping[str, str]
) -> None:
    """Test main function on modular file."""

    output_directory = Path(tmpdir_factory.mktemp('output'))

    input_filename = DATA_PATH / 'modular.yaml'
    output_path = output_directory / 'model'

    with freeze_time(TIMESTAMP):
        main(['--input', str(input_filename), '--output', str(output_path)])

    for key, value in expected.items():
        result = output_path.joinpath(*key).read_text()
        assert result == value


def test_main_modular_no_file() -> None:
    """Test main function on modular file with no output name."""

    input_filename = DATA_PATH / 'modular.yaml'

    assert main(['--input', str(input_filename)]) == Exit.ERROR


def test_main_modular_filename(tmpdir_factory: TempdirFactory) -> None:
    """Test main function on modular file with filename."""

    output_directory = Path(tmpdir_factory.mktemp('output'))

    input_filename = DATA_PATH / 'modular.yaml'
    output_filename = output_directory / 'model.py'

    assert (
        main(['--input', str(input_filename), '--output', str(output_filename)])
        == Exit.ERROR
    )


@pytest.mark.parametrize(
    'expected',
    [
        '''\
# generated by datamodel-codegen:
#   filename:  api.yaml
#   timestamp: 1985-10-26T08:21:00+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, UrlStr


class Pet(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None


class Pets(BaseModel):
    __root__: List[Pet]


class User(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None


class Users(BaseModel):
    __root__: List[User]


class Id(BaseModel):
    __root__: str


class Rules(BaseModel):
    __root__: List[str]


class Error(BaseModel):
    code: int
    message: str


class api(BaseModel):
    apiKey: Optional[str] = None
    apiVersionNumber: Optional[str] = None
    apiUrl: Optional[UrlStr] = None
    apiDocumentationUrl: Optional[UrlStr] = None


class apis(BaseModel):
    __root__: List[api]


class Event(BaseModel):
    name: Optional[str] = None


class Result(BaseModel):
    event: Optional[Event] = None
'''
    ],
)
def test_main_no_file(capsys: CaptureFixture, expected: str) -> None:
    """Test main function on non-modular file with no output name."""

    input_filename = DATA_PATH / 'api.yaml'

    with freeze_time(TIMESTAMP):
        main(['--input', str(input_filename)])

    captured = capsys.readouterr()
    assert captured.out == expected
    assert not captured.err


@pytest.mark.parametrize(
    'expected',
    [
        '''\
# generated by datamodel-codegen:
#   filename:  api.yaml
#   timestamp: 1985-10-26T08:21:00+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, UrlStr


class Pet(BaseModel):  # 1 2, 1 2, this is just a pet
    id: int
    name: str
    tag: Optional[str] = None


class Pets(BaseModel):
    __root__: List[Pet]


class User(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None


class Users(BaseModel):
    __root__: List[User]


class Id(BaseModel):
    __root__: str


class Rules(BaseModel):
    __root__: List[str]


class Error(BaseModel):
    code: int
    message: str


class api(BaseModel):
    apiKey: Optional[str] = None
    apiVersionNumber: Optional[str] = None
    apiUrl: Optional[UrlStr] = None
    apiDocumentationUrl: Optional[UrlStr] = None


class apis(BaseModel):
    __root__: List[api]


class Event(BaseModel):
    name: Optional[str] = None


class Result(BaseModel):
    event: Optional[Event] = None
'''
    ],
)
def test_main_custom_template_dir(capsys: CaptureFixture, expected: str) -> None:
    """Test main function with custom template directory."""

    input_filename = DATA_PATH / 'api.yaml'
    custom_template_dir = DATA_PATH / 'templates'
    extra_template_data = DATA_PATH / 'extra_data.json'

    with freeze_time(TIMESTAMP):
        main(
            [
                '--input',
                str(input_filename),
                '--custom-template-dir',
                str(custom_template_dir),
                '--extra-template-data',
                str(extra_template_data),
            ]
        )

    captured = capsys.readouterr()
    assert captured.out == expected
    assert not captured.err


@freeze_time('2019-07-26')
def test_pyproject():
    with TemporaryDirectory() as output_dir:
        output_dir = Path(output_dir)
        pyproject_toml = Path(DATA_PATH) / "project" / "pyproject.toml"
        shutil.copy(pyproject_toml, output_dir)
        output_file: Path = output_dir / 'output.py'
        return_code: Exit = main(
            ['--input', str(DATA_PATH / 'api.yaml'), '--output', str(output_file)]
        )
        assert return_code == Exit.OK
        assert (
            output_file.read_text()
            == '''# generated by datamodel-codegen:
#   filename:  api.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import (
    annotations,
)

from typing import (
    List,
    Optional,
)

from pydantic import (
    BaseModel,
    UrlStr,
)


class Pet(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None


class Pets(BaseModel):
    __root__: List[Pet]


class User(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None


class Users(BaseModel):
    __root__: List[User]


class Id(BaseModel):
    __root__: str


class Rules(BaseModel):
    __root__: List[str]


class Error(BaseModel):
    code: int
    message: str


class api(BaseModel):
    apiKey: Optional[
        str
    ] = None
    apiVersionNumber: Optional[
        str
    ] = None
    apiUrl: Optional[
        UrlStr
    ] = None
    apiDocumentationUrl: Optional[
        UrlStr
    ] = None


class apis(BaseModel):
    __root__: List[api]


class Event(BaseModel):
    name: Optional[str] = None


class Result(BaseModel):
    event: Optional[
        Event
    ] = None
'''
        )

    with pytest.raises(SystemExit):
        main()
