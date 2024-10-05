from generics import *

input = get_input_file("2023/day_01/")

# Part 2

num_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

total = 0
for line in input:
    fst = ""
    lst = ""
    cur = ""
    for char in line:
        if char.isdigit():
            lst = char
            if not fst:
                fst = char
        else:
            cur += char
            for k,v in num_dict.items():
                if cur.endswith(k):
                    lst = num_dict[k]
                    if not fst:
                        fst = num_dict[k]

    num = int(fst+lst)
    print(num)
    total += num

print(total)


# Part 1
# total = 0
# for line in input:
#     fst = ""
#     lst = ""
#     for char in line:
#         if char.isdigit():
#             if not fst:
#                 fst = char
#             else:
#                 lst = char
        
#     if not lst:
#         lst = fst
#     num = int(fst+lst)
#     total += num

# print(total)