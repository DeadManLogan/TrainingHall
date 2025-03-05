import random
import typing

TupleInts = typing.Tuple[int, ...]

def roll_dice(sides: int = 6, dice: int = 1) -> TupleInts:
    return tuple(random.randint(1, sides) for _ in range(dice))