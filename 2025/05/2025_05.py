import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from mylib.input import input_raw

file = os.path.dirname(__file__) + "/input_example.txt"
# file = os.path.dirname(__file__) + "/input_test.txt"
file = os.path.dirname(__file__)+"/input.txt"

# logfile = os.path.dirname(__file__)+"/log_test.txt"

debug = 0

def common():
    ranges, ingredients = input_raw(file).split("\n\n")
    ranges = ranges.split('\n')
    ingredients = ingredients.strip().split('\n')

    return (ranges,ingredients)


def first(ranges, ingredients):
    freshes = 0

    for i in ingredients:
        for r in ranges:
            min = int(r.split('-')[0])
            max = int(r.split('-')[1])
            if min <= int(i) <= max:
                freshes += 1
                break

    print(f"1st part, answer = {freshes}")

def second(ranges):
    valids = []

    sorted_ranges = sorted(ranges, key=lambda x: int(x.split('-')[0]))

    for r in sorted_ranges:
        s = int(r.split('-')[0])
        e = int(r.split('-')[1])

        # print(f"{s=}, {e=}")

        if len(valids) == 0:
            valids.append((s,e))
            continue

        if s <= valids[-1][1]:
            valids[-1] = (valids[-1][0], max(valids[-1][1], e))
        else:
            valids.append((s,e))
    
    sum = 0
    for v in valids:
        sum += v[1] - v[0] + 1

    print(f"2nd part, answer = {sum}")

r,i = common()
first(r,i)
second(r)
