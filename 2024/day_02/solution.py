from aoc_tools import *

def process_line(line) -> tuple[bool, int | None]:
    # Strictly decreasing/increasing
    if not ( all(a > b for a, b in zip(line, line[1:])) or all(a < b for a, b in zip(line, line[1:])) ):
        return False
    for ni, num in enumerate(line):
        if ni == 0:
            continue
        if 0 < abs(num - line[ni-1]) <= 3:
            continue
        else:
            return False
        
    return True

def find(input) -> int:
    lines = [get_numbers(line) for line in input]

    total = 0
    for line in lines:
        # This pattern concats a list for each index in the line list, with every element before i [:i] and every element after i [i+1:] so that we can see if it passes without a given element
        # Much simpler!
        if process_line(line) or any(process_line(line[:i] + line[i+1:]) for i in range(len(line))):
            total += 1
    return total
        
                

def test():
    test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    test_input = normalise_test_input(test_input)

    assert find(test_input) == 4

def real():
    input = get_input_file("2024/day_02/")
    print(find(input))
    
test()
real()
