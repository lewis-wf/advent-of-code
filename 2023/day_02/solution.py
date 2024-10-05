from generics import *

input = get_input_file("2023/day_02/")


# Part 2

total = 0
for game in input:
    mins = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
    game_split = game.split(":")
    id = game_split[0].split(" ")[1]
    
    sets = game_split[1].split(";")
    for set in sets:
        map = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        pulls = set.split(",")
        for pull in pulls:
            value = pull.strip().split(" ")[0]
            for k,v in map.items():
                if pull.endswith(k):
                    map[k] += int(value)

        for k,v in mins.items():
            if map[k] > mins[k]:
                mins[k] = map[k]
    
    power = mins["blue"] * mins["red"] * mins["green"]
    total += power


print(total)


# Part 1
# limits = {
#             "red": 12,
#             "green": 13,
#             "blue": 14
#         }

# total = 0
# for game in input:
#     possible = True
#     game_split = game.split(":")
#     id = game_split[0].split(" ")[1]
    
#     sets = game_split[1].split(";")
#     for set in sets:
#         map = {
#             "red": 0,
#             "green": 0,
#             "blue": 0
#         }
#         pulls = set.split(",")
#         for pull in pulls:
#             value = pull.strip().split(" ")[0]
#             for k,v in map.items():
#                 if pull.endswith(k):
#                     map[k] += int(value)

#         if any(map[key] > limits[key] for key in map.keys()):
#             possible = False
    
#     if possible:
#         total += int(id)

# print(total)
    
