from aoc_tools import *

def recur_check(target, cur_total, index, nums) -> bool:
    if index == len(nums):
        return cur_total == target
    
    addition = recur_check(target, cur_total + nums[index], index + 1, nums)
    concat = recur_check(target, concat_ints(cur_total, nums[index]), index + 1, nums)

    if cur_total == 0:
        cur_total = 1
    
    multiplication = recur_check(target, cur_total * nums[index], index + 1, nums)
    return addition or multiplication or concat

def find(input):
    total = 0
    for line in input:
        nums = get_numbers(line)
        target = nums[0]
        options = nums[1:]
        # Recursive addition/multiplication
        if recur_check(target, 0, 0, options):
            total += target

    return total



def test():
    input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

    input = normalise_test_input(input)

    assert find(input) == 11387

def real():
    input = get_input_file("2024/day_07/")

    print(find(input))

# test()
real()