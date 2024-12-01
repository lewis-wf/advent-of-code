from aoc_tools import *
from collections import Counter

def find(input) -> int:
    left_list = []
    right_list = []
    for sec in input:
        split_sec = get_numbers(sec)
        left_list.append(split_sec[0])
        right_list.append(split_sec[1])
    
    r_count = Counter(right_list)
    total_similarity = 0

    for l_num in left_list:
        total_similarity += l_num * r_count[l_num]

    
    return total_similarity

def test():
    test_input = """3   4
4   3
2   5
1   3
3   9
3   3"""
    test_input = [line.strip().replace("\n", "") for line in test_input.split("\n")]
    assert find(test_input) == 31

def real():
    input = get_input_file("2024/day_01/")
    print(find(input))

# test()
real()
