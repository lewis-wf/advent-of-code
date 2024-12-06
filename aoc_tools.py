from enum import Enum
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
