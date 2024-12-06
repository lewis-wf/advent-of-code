from enum import Enum
from aoc_tools import *

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

# Rules:
# Move forward (in the direction you're facing) until you either
# reach the edge of the grid, in which case you exit, or a #
# in which case you turn 90 degrees clockwise
# and continue. 
# Get a count of the unique positions visited (set of tuples me thinks).

def find(input):
    starting_loc = ()
    for li, line in enumerate(input):
        if "^" in line:
            for ci, c in enumerate(line):
                if c == "^":
                    starting_loc = (li, ci)
                    break
            break
    guard_route = get_visited(input, starting_loc)
    total = 0
    for pos in guard_route:
        total += check_location(input, starting_loc, pos)
    
    return total

# Code duplication - yuck!
def get_visited(input, starting_loc):
    current_direction = Directions.north
    visited_locations = {starting_loc}
    bounds = {len(input), len(input[0]), -1}
    cur_loc = starting_loc
    complete = False
    while not complete:
        # Move in the current direction
        next_loc = combine_tuple(cur_loc, current_direction.value)
        if next_loc[0] in bounds or next_loc[1] in bounds:
            complete = True
            continue
        if input[next_loc[0]][next_loc[1]] == "#":
            current_direction = Directions.next_dir(current_direction)
            continue
        visited_locations.add(next_loc)
        cur_loc = next_loc
    return visited_locations

def check_location(input, starting_loc, obs) -> int:
    if obs == starting_loc:
        return 0
    
    current_direction = Directions.north
    visited_locations = {(starting_loc, Directions.north)}
    bounds = {len(input), len(input[0]), -1}
    cur_loc = starting_loc
    complete = False

    while not complete:
        # Move in the current direction
        next_loc = combine_tuple(cur_loc, current_direction.value)
        if (next_loc, current_direction) in visited_locations:
            # We're looping!
            return 1
        if next_loc[0] in bounds or next_loc[1] in bounds:
            complete = True
            continue
        if input[next_loc[0]][next_loc[1]] == "#" or next_loc == obs:
            current_direction = Directions.next_dir(current_direction)
            continue
        visited_locations.add((next_loc, current_direction))
        cur_loc = next_loc
    return 0

def test():
    input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

    input = normalise_test_input(input)

    assert find(input) == 6

def real():
    input = get_input_file("2024/day_06/")

    print(find(input))

# test()
real()