import os
import re
import sys
import itertools

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from mylib.input import input, input_raw

file = os.path.dirname(__file__) + "/input_example.txt"
# file = os.path.dirname(__file__) + "/input_test.txt"
file = os.path.dirname(__file__)+"/input.txt"

# logfile = os.path.dirname(__file__)+"/log_test.txt"

debug = 0

def common():
    sum = 0

    for line in input(file):
        parts = line.split()

        lights = parts[0]
        joltages = parts[-1]
        buttons = parts[1:-1]

        max_iter = 10

        print(f"{lights=},{buttons=}")
        for r in range(1, max_iter):
            for c in itertools.combinations_with_replacement(buttons, r):
                # print(f"combination: {c}")

                btns = list(itertools.chain.from_iterable([x[1:-1].split(",") for x in c]))
                
                l = (len(lights) - 2) * "."

                continue_loop = True

                for b in btns:
                    i = int(b)

                    if l[i] == ".": l = l[:i] + "#" + l[i+1:]
                    elif l[i] == "#": l = l[:i] + "." + l[i+1:]


                print(f"with {c}: push {btns} res={l}")
                if f"[{l}]" == lights:
                    print(f"{i}: {b} -> {l}, found={f"[{l}]" == lights} with r={r}")
                    sum += r
                    continue_loop = False
                    break
                
                if not continue_loop:
                    break
            if not continue_loop:
                break
        else:
            print("not found")
    
    print(f"1st part, answer = {sum}")

def first():
    print(f"1st part, answer = ")


def second():
    print(f"2nd part, answer = ")


common()
first()
# second()
