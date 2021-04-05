"""Chat commands."""

from random import randint


def ternary(condition, first_opernad, second_operand):
    """Same as `first_operand if condition else second_operand`"""
    return first_opernad if condition else second_operand


def readable_ternary(first_opernad, condition, second_operand):
    """Same as `first_operand if condition else second_operand`"""
    return ternary(condition, first_opernad, second_operand)


def random(start: int, end: int) -> int:
    """Same as `random.randint(start, end)`"""
    return randint(start, end)


def roll(sides: int) -> int:
    """Same as `random.randint(1, sides)`"""
    return random(1, sides)


def roll_n(times: int, sides: int) -> int:
    """Rolls dice multiple times."""
    return sum(roll(sides) for _ in range(times))


def coin() -> str:
    """Flips a coin."""
    result = roll(9999)
    return 'heads' if result > 5000 else 'tails' if result < 5000 else 'edge'
