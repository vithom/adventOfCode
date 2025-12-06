import os
import sys
from functools import reduce

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from mylib.input import input, input_raw

file = os.path.dirname(__file__) + "/input_example.txt"
# file = os.path.dirname(__file__) + "/input_test.txt"
file = os.path.dirname(__file__)+"/input.txt"

# logfile = os.path.dirname(__file__)+"/log_test.txt"

debug = 0

def common():
    lines = input(file)
    ops = lines.pop().split()

    return lines, ops

def first(lines, ops):
    print(ops)
    acc = []

    for l, line in enumerate(lines):
        for i,n in enumerate(line.split()):
            if l == 0:
                acc.append(int(n))
                continue
            if ops[i] == "*": acc[i] *= int(n)
            if ops[i] == "+": acc[i] += int(n)

    print(f"1st part, answer = {sum([x for x in acc])}")


def second():
    lines = input_raw(file).split('\n')[:-1]
    # print(lines)
    acc = []

    nums = []
    for n in range(len(lines[0])-1, -1, -1):
        number = ""
        op = ""
        for l in lines:
            c = l[n]

            if c in ["*", "+"]:
                op = c
            else:
                number += c

        if number == ' ' * len(lines):
            nums = []
        else:
            nums.append(int(number))

        # print(f"{nums=}")


        if op != "":
            # print(f'{op=}')
            if op == "+": acc.append(sum([x for x in nums]))
            if op == "*": acc.append(reduce(lambda x,y: x*y, [x for x in nums]))

        # print(acc)

    print(f"2nd part, answer = {sum([x for x in acc])}")


lines, ops = common()
first(lines, ops)
second()
