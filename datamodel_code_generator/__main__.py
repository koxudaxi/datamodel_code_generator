#! /usr/bin/env python

"""
Main function.
"""

import sys
from argparse import ArgumentParser, FileType, Namespace
from datetime import datetime, timezone
from enum import IntEnum
from pathlib import Path
from typing import IO, Any, Optional, Sequence

import argcomplete
from datamodel_code_generator import PythonVersion, enable_debug_message
from datamodel_code_generator.model.pydantic import (
    BaseModel,
    CustomRootType,
    dump_resolve_reference_action,
)


class Exit(IntEnum):
    """Exit reasons."""

    OK = 0
    ERROR = 1


arg_parser = ArgumentParser()
arg_parser.add_argument(
    '--input',
    help='Open API YAML file (default: stdin)',
    type=FileType('rt'),
    default=sys.stdin,
)
arg_parser.add_argument('--output', help='Output file (default: stdout)')
arg_parser.add_argument(
    '--base-class',
    help='Base Class (default: pydantic.BaseModel)',
    type=str,
    default='pydantic.BaseModel',
)
arg_parser.add_argument(
    '--target-python-version',
    help='target python version (default: 3.7)',
    choices=['3.6', '3.7'],
    default='3.7',
)
arg_parser.add_argument('--debug', help='show debug message', action='store_true')


def main(args: Optional[Sequence[str]] = None) -> Exit:
    """Main function."""

    # add cli completion support
    argcomplete.autocomplete(arg_parser)

    if args is None:
        args = sys.argv[1:]

    namespace: Namespace = arg_parser.parse_args(args)

    if namespace.debug:  # pragma: no cover
        enable_debug_message()

    from datamodel_code_generator.parser.openapi import OpenAPIParser

    parser = OpenAPIParser(
        BaseModel,
        CustomRootType,
        base_class=namespace.base_class,
        target_python_version=PythonVersion(namespace.target_python_version),
        text=namespace.input.read(),
        dump_resolve_reference_action=dump_resolve_reference_action,
    )

    result = parser.parse()

    output = Path(namespace.output) if namespace.output is not None else None

    if isinstance(result, str):
        modules = {output: result}
    else:
        if output is None:
            print('Modular references require an output directory')
            return Exit.ERROR
        if output.suffix:
            print('Modular references require an output directory, not a file')
            return Exit.ERROR
        modules = {output.joinpath(*name): body for name, body in result.items()}

    timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    header = f'''\
# generated by datamodel-codegen:
#   filename:  {Path(namespace.input.name).name}
#   timestamp: {timestamp}'''

    file: Optional[IO[Any]]
    for path, body in modules.items():
        if path is not None:
            if not path.parent.exists():
                path.parent.mkdir()
            file = path.open('wt')
        else:
            file = None

        print(header, file=file)
        if body:
            print('', file=file)
            print(body.rstrip(), file=file)

        if file is not None:
            file.close()

    return Exit.OK


if __name__ == '__main__':
    sys.exit(main())
