from enum import Enum
import itertools
from math import log
import re

# TODO create a class/way of handling/searching/interacting with a 2D matrix, something which would make the code in 2024/04 easier to write/reason about

adjacent_cell_offsets = [(-1,0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
diagonal_cell_offsets = [(-1, 1), (1, 1), (1, -1), (-1, -1)] 
cross_cell_offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Directions(Enum):
    north = (-1, 0)
    east = (0, 1)
    south = (1, 0)
    west = (0, -1)
    
    @classmethod
    def next_dir(cls, cur_dir):
        dirs = [cls.north, cls.east, cls.south, cls.west]
        index = dirs.index(cur_dir)
        next = index + 1
        if next > len(dirs) -1:
            return dirs[0]
        else:
            return dirs[next]

def is_out_of_bounds(loc: tuple[int, int], bounds: tuple[int, int]) -> bool:
    if loc[0] < 0 or loc[0] >= bounds[0] or loc[1] < 0 or loc[1] >= bounds[1]:
        return True
    return False

def normalise_test_input(input: str) -> list[str]: return [line.strip().replace("\n", "") for line in input.split("\n")]

def get_input_file(dir: str) -> list[str]:
    with open(dir + "input.txt", "r") as f:
        output = f.readlines()
        return [line.strip().replace("\n", "") for line in output]
    
def get_numbers(input: str) -> list[int]:
    pattern = r"-?\d+"
    matches = re.findall(pattern, input)
    return [int(m) for m in matches]

def combine_tuple(tup_1: tuple[int, int], tup_2: tuple[int, int]) -> tuple[int, int]:
    return ( tup_1[0] + tup_2[0], tup_1[1] + tup_2[1] )

def tuple_difference(tup_1: tuple[int, int], tup_2: tuple[int, int]) -> tuple[int, int]:
    return ( tup_1[0] - tup_2[0], tup_1[1] - tup_2[1] )

def flatten(nested_list: list[list]) -> list:
    return list(itertools.chain(*nested_list))

def flip(x: int): return x // -1
def flip_tuple(tup: tuple[int, int]) -> tuple[int, int]:
    return ( tup[0] // -1, tup[1] // -1 )

def is_prime(num):
    for n in range(2,int(num**0.5)+1):
        if num % n == 0:
            return False
    return True

def concat_ints(left: int, right: int) -> int:
    """Efficiently concats two ints [thanks Stack Overflow].
    """
    return 10**int(log(right, 10)+1)*left+right