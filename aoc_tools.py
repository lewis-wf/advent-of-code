import re

def normalise_test_input(input: str) -> list[str]: return [line.strip().replace("\n", "") for line in input.split("\n")]

def get_input_file(dir: str) -> list[str]:
    with open(dir + "input.txt", "r") as f:
        output = f.readlines()
        return [line.strip().replace("\n", "") for line in output]
    
def get_numbers(input: str) -> list[int]:
    pattern = r"-?\d+"
    matches = re.findall(pattern, input)
    return [int(m) for m in matches]
