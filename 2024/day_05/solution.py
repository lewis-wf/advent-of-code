from collections import defaultdict
from aoc_tools import *

# X|Y
# X before Y
# Second set of data are the lists, in the order of printing
# Order them correctly and then add up all the middle page numbers to get the answer

# My idea is to have a dict (hashmap) for each X with a set of Ys. Then, when you get to a value, you need to check
# that every value before it is NOT in the set. If it IS in the set, you need to move your current value back to 
# before the offending value, and repeat.

# Step 1: create that mapping
# Step 2: identify offending lines correctly

# Step 3: be able to create the correct order

# Step 4: find the middle value
# Step 5: add those up


def find(input):
    dep_map: dict[str, set] = defaultdict(set)
    split_index = 0

    for index, line in enumerate(input):
        if line == "":
            split_index = index
            break
        
        x, y = line.split("|")
        dep_map[x].add(y)
    
    query_lines = [l.split(",") for l in input[split_index+1:]]
    
    corrected_lines = []
    correct_lines = []
    total = 0
    for qline in query_lines:
        correct = True
        nqline = qline.copy()
        for ni, n in enumerate(qline):
            for nni, nn in enumerate(qline[ni:], 1):
                if n in dep_map[nn]:
                    correct = False
                    # nqline[ni] = nn
                    # nqline[nni] = n

        if correct:
            correct_lines.append(qline)
        corrected_lines.append(nqline)

        # total += int(nqline[len(nqline)//2])
    for l in correct_lines:
        total += int(l[len(l)//2])
    return total
    


def test():
    input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

    input = normalise_test_input(input)

    assert find(input) == 143

def real():
    input = get_input_file("2024/day_05/")

    print(find(input))

# test()
real()