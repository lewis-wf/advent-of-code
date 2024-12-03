import re

normalise_test_input = lambda input: [line.strip().replace("\n", "") for line in input.split("\n")]

def get_input_file(dir: str) -> list[str]:
    with open(dir + "input.txt", "r") as f:
        output = f.readlines()
        return [line.strip().replace("\n", "") for line in output]
    
def get_numbers(input: str) -> list[int]:
    pattern = r"[1-9][0-9]*|0"
    matches = []
    for match in re.findall(pattern, input):
        matches.append(int(match))
    return matches
