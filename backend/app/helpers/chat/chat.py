"""Chat helpers."""

import re
from typing import Callable, Union

from app.helpers.chat.constructions import CONSTRUCTIONS


def transfrom_operand(operand: str) -> Union[str, int, bool]:
    """Transforms operand."""
    result = operand.strip()

    if result.isdigit():
        result = int(result)

    elif result in ['True', 'true', 'Yes', 'yes', 'T', 't', 'N', 'n']:
        result = True

    elif result in ['False', 'false', 'No', 'no', 'F', 'f', 'N', 'n']:
        result = False

    elif result.startswith('"') and result.endswith('"'):
        result = result[1:-1]

    return result


def perform_operation(operation: Callable, *args):
    """Perform operation using provided operands."""
    return operation(*args)


def parse_command(command: str) -> dict:
    """Parses command."""
    command = command.strip()

    for regex, operation in CONSTRUCTIONS:
        parsed = re.match(regex, command)
        if parsed:
            operands = [parse_command(operand) for operand in parsed.groups()]
            return perform_operation(operation, *operands)

    return transfrom_operand(command)
