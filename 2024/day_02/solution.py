from aoc_tools import *

def find(input) -> int:
    lines = [get_numbers(line) for line in input]

    min = 1
    max = 3
    total = 0
    for line in lines:
        valid = True
        increasing = False
        for ni, num in enumerate(line):
            if ni == 0:
                continue
            if ni == 1:
                increasing = True if num > line[ni-1] else False
                condition = () if increasing else (num < line[ni-1])
            if 0 < abs(num - line[ni-1]) <= 3:
                if increasing and num > line[ni-1]:
                    continue
                elif not increasing and num < line[ni-1]:
                    continue
                else:
                    valid = False
                    break
            else:
                valid = False
                break
        if valid:
            total += 1
    return total
        
                

def test():
    test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    test_input = [line.strip().replace("\n", "") for line in test_input.split("\n")]

    assert find(test_input) == 2

def real():
    input = get_input_file("2024/day_02/")
    print(find(input))
    
# test()
real()
