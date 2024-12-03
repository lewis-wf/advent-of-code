from aoc_tools import *
import re
from ast import literal_eval 

def find(input) -> int:
    all_matches_pattern = r"mul(\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))"
    
    instructions = []
    for line in input:
        res = re.findall(all_matches_pattern, line)
        instructions.extend(res)
    
    total = 0
    do = True
    for instruct_tup in instructions:
        if instruct_tup[2]:
            do = False
        if instruct_tup[1] and not do:
            do = True
        if instruct_tup[0] and do:
            tup_r = literal_eval(instruct_tup[0])
            total += tup_r[0] * tup_r[1]

    return total
    

def test():
    input = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]

    assert find(input) == 48

def real():
    input = get_input_file("2024/day_03/")

    print(find(input))

# test()
real()