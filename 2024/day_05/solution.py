from collections import defaultdict
from aoc_tools import *

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
    total = 0
    for qline in query_lines:
        nqline = []
        while len(nqline) < len(qline):
            lnqline = len(nqline)
            for ni, n in enumerate([v for v in qline if v not in nqline]):
                if lnqline == 0:
                    if any(n in dep_map[nn] for nn in qline[ni:]):
                        continue
                    nqline.append(n)
                else:
                    for vi, v in enumerate(nqline):
                        if n in dep_map[v]:
                            continue
                        nqline.insert(vi, n)
                        break
                    if vi == len(nqline) -1:
                        nqline.append(n)

        if nqline != qline:
            corrected_lines.append(nqline)
            total += int(nqline[len(nqline)//2])

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

    assert find(input) == 123

def real():
    input = get_input_file("2024/day_05/")

    print(find(input))

# test()
real()