import os
import re

# file = os.path.dirname(__file__)+"/input_example.txt"
file = os.path.dirname(__file__)+"/input.txt"

debug = True

with open(file, 'rt') as f:
    lines = f.readlines()
    text = "".join(lines)

def common():
    pass
    
def first():
    matches = re.findall(r"mul\(\d+,\d+\)", text)

    # for m in matches:
    #     print(m)
    
    a = [int(x[0]) * int(x[1]) for x in [m.replace("mul", "").replace("(", "").replace(")", "").split(",") for m in matches]]
    total = sum(a)

    print(f"sum = {total}")
        

def second():
    matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)", text)

    #if debug: print(matches)
    
    tot = 0
    enabled = True
    
    for m in matches:
        if m == "do()":
            enabled = True
        elif m == "don't()":
            enabled = False
        elif enabled:
            a,b = [int(x) for x in m.replace("mul", "").replace("(", "").replace(")", "").split(",")]
            tot += a*b
        
    print(tot)

first()
second()