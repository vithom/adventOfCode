import os

file = os.path.dirname(__file__)+"/input_01_2.txt"

with open(file, 'rt') as f:
    lines = f.readlines()

def part_one():
    floor = 0
    # index = 1

    for c in lines[0]:
        if c == '(':
            floor+=1
        else: # )
            floor-=1

    print(f"1st part: {floor}")

def part_two():
    floor = 0
    index = 1

    for c in lines[0]:
        if c == '(':
            floor+=1
        else: # )
            floor-=1

        if floor == -1:
            break

        index+=1

    print(f"2nd part: {index}")

part_one()
part_two()