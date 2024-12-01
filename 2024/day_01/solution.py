from aoc_tools import *

def find(input) -> int:
    left_list = []
    right_list = []
    for sec in input:
        split_sec = sec.split("   ")
        left_list.append(split_sec[0])
        right_list.append(split_sec[1])
    
    left_list.sort()
    right_list.sort()
    
    total_distance = 0
    for i, num in enumerate(left_list):
        distance = abs( int(num) - int(right_list[i]) ) 
        total_distance += distance
    
    return total_distance

def test():
    test_input = """3   4
4   3
2   5
1   3
3   9
3   3"""
    test_input = [line.strip().replace("\n", "") for line in test_input.split("\n")]
    assert find(test_input) == 11

def real():
    input = get_input_file("2024/day_01/")
    print(find(input))

# test()
real()
