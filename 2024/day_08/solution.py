from collections import defaultdict
import itertools
from aoc_tools import *

# Rules:
# Freqs are single digits or letters. Case matters - a != A
# This is about finding 'antinodes' which are exactly in line
# with two antennas of the same frequency, but only in the line where the antenna are
# exactly twice as far away as the other

# Me:
# I think this is another fancy offset Q - find the offset between each unique pair
# of paired antenna, find their offset, then apply that offset
# on each side/direction (when in bounds). Add those locations to set, get the  length
# of the set.
# The first step is to get the position of each letter into dict.
# Then find each pair
# then offsets
# then offsets + 1 step in each direction
# then see if we match the test!

def gen_nodes(start_pos: tuple[int, int], offset: tuple[int, int], bounds: tuple[int, int]) -> list[tuple]:
    nodes = []
    nxt_pos = start_pos
    while True:
        nxt_pos = combine_tuple(nxt_pos, offset)
        if is_out_of_bounds(nxt_pos, bounds):
            return nodes
        nodes.append(nxt_pos)

def find(input):
    input_grid = [list(l) for l in input]
    bounds = (len(input), len(input[0]))
    antenna_map: dict[str, list[tuple[int, int]]] = defaultdict(list)

    for ri, r in enumerate(input_grid):
        for ci, c in enumerate(r):
            if c == ".":
                continue
            antenna_map[c].append((ri, ci))

    pairs_map = {k: list(itertools.permutations(v, 2)) for k,v in antenna_map.items()}
    pairs_list: list[tuple[tuple[int, int], tuple[int, int]]] = flatten(pairs_map.values())

    antinodes: set[tuple[int, int]] = set()
    for pair in pairs_list:
        diff = tuple_difference(pair[0], pair[1])
        pos_nodes = gen_nodes(pair[0], diff, bounds)
        neg_nodes = gen_nodes(pair[1], flip_tuple(diff), bounds)
        antinodes.update(pos_nodes+neg_nodes+list(pair))

    # print(len(antinodes), antinodes)
    return len(antinodes)


def test():
    input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

    input = normalise_test_input(input)

    assert find(input) == 34

def real():
    input = get_input_file("2024/day_08/")

    print(find(input))

# test()
real()