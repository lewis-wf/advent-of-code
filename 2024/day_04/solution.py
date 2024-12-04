from collections import defaultdict
from aoc_tools import *

# row, column
adjacent_cell_offsets = [(-1,0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
diagonal_cell_offsets = [(-1, 1), (1, 1), (1, -1), (-1, -1)] 

def combine_tuple(tup_1: tuple[int, int], tup_2: tuple[int, int]) -> tuple[int, int]:
    return ( tup_1[0] + tup_2[0], tup_1[1] + tup_2[1] )

def get_neighbours(cur_pos: tuple[int, int], input_grid: list[str]) -> dict[tuple[int, int], str]:
    values = defaultdict(tuple)
    for offset in diagonal_cell_offsets:
        new_pos = combine_tuple(cur_pos, offset)
        if new_pos[0] < 0 or new_pos[1] < 0:
            continue
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
    diag_1_match = (neighbours[((-1, 1))] == "M" and neighbours[((1, -1))] == "S") or (neighbours[((-1, 1))] == "S" and neighbours[((1, -1))] == "M")
    diag_2_match = (neighbours[((1, 1))] == "M" and neighbours[((-1, -1))] == "S") or (neighbours[((1, 1))] == "S" and neighbours[((-1, -1))] == "M")
    return 1 if diag_2_match and diag_1_match else 0
            
            
    

def find(input: list[str]) -> int:
    count = 0
    for li, l in enumerate(input):
        for ci, c in enumerate(l):
            if c != "A":
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
    assert find(input) == 9

def real():
    input = get_input_file("2024/day_04/")

    print(find(input))

test()
real()