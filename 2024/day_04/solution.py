from collections import defaultdict
from aoc_tools import *

# row, column
adjacent_cell_offsets = [(-1,0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
letters = ["X", "M", "A", "S"]

def combine_tuple(tup_1: tuple[int, int], tup_2: tuple[int, int]) -> tuple[int, int]:
    return ( tup_1[0] + tup_2[0], tup_1[1] + tup_2[1] )

def get_neighbours(cur_pos: tuple[int, int], input_grid: list[str]) -> dict[tuple[int, int], str]:
    values = defaultdict(tuple)
    for offset in adjacent_cell_offsets:
        new_pos = combine_tuple(cur_pos, offset)
        try:
            char = input_grid[new_pos[0]][new_pos[1]]
            values[offset] = char
        except IndexError:
            continue
    return values

def follow_offset(start_pos: tuple[int, int], offset: tuple[int, int], input_grid: list[str]) -> bool:
    # Just do this manually, nothing clever yet
    should_be_a = combine_tuple(start_pos, offset)
    should_be_s = combine_tuple(should_be_a, offset)
    if any(v < 0 for v in should_be_a+should_be_s):
        return False
    try:
        if input_grid[should_be_a[0]][should_be_a[1]] == "A" and input_grid[should_be_s[0]][should_be_s[1]] == "S":
            return True
    except IndexError:
        return False
    return False

def dig(cur_pos: tuple[int, int], input_grid: list[str]) -> int:
    neighbours = get_neighbours(cur_pos, input_grid)
    # The current issue is that it's counting all matches. Actually, we know that the only matches are those which are EITHER diagonal or next to you. That means if you
    # find a match on a given offset then the match has to continue for another 2 offsets: X -> (0, 1) -> M -> (0, 1) -> A -> (0, 1) -> S
    count = 0
    for n_offset in neighbours:
        if neighbours[n_offset] == "M":
            n_pos = combine_tuple(cur_pos, n_offset)
            if follow_offset(start_pos=n_pos, offset=n_offset, input_grid=input_grid):
                count += 1
    return count
            
            
    

def find(input: list[str]) -> int:
    # Order is XMAS, so each letter needs to border one of those,  in that order (starting with X)
    # If we hit an S, and one of its offsets hits A, then we can start digging in that direction. We move our offset 'root' to that, do the process again, until we either complete the word 
    # or fail, in which case we reset to the root.
    # This 'moving' of root is virtual, though, right? So it's actually about offsets of offsets; if we go down one, find a valid next letter, then we go forward one that's just an additional offset.
    count = 0
    for li, l in enumerate(input):
        for ci, c in enumerate(l):
            if c != "X":
                continue
            current_pos = (li, ci)
            count += dig(current_pos, input)
    return count




def test():
    input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
    input = normalise_test_input(input)
    assert find(input) == 18

def real():
    input = get_input_file("2024/day_04/")

    print(find(input))

# test()
real()