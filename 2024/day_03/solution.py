from aoc_tools import *
import re
from ast import literal_eval 

def find(input) -> int:
    regex_pattern = r"mul(\(\d{1,3},\d{1,3}\))"

    mults = []
    for line in input:
        res = re.findall(regex_pattern, line)
        mults.extend(res)
    
    total = 0
    for r in mults:
        tup_r = literal_eval(r)
        total += tup_r[0] * tup_r[1]

    return total
    

def test():
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    assert find(input) == 161

def real():
    input = get_input_file("2024/day_03/")

    print(find(input))

# test()
real()