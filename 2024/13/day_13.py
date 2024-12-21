import os
import sys
import itertools

import re

# file = os.path.dirname(__file__)+"/input_example.txt"
file = os.path.dirname(__file__)+"/input.txt"

debug = 0

def input(trim = True):
    with open(file, 'rt') as f:
        lines = f.read().strip().split("\n\n")
        # if trim:
        #     return [l.replace('\n', '') for l in lines]
        # else:
        #     return lines
    return lines

def common(offset = 0):
    blocks = input()

    results = []
    for block in blocks:
        lines = block.split('\n')

        r = list(itertools.chain.from_iterable([map(int,re.findall(r"\d+", line)) for line in lines]))

        if offset > 0:
            r[4] += offset
            r[5] += offset

        if debug: print(r)
        results.append(solveEquation(*r))

    return results
    
    
    

# ax + by = c
# dx + ey = f
# x = (f*b - e*c) / (d*b - e*a)
# y = (c - a*x) / b
def solveEquation(a,d,b,e,c,f):
    x = (f*b - e*c) / (d*b - e*a)
    y = (c - a*x) / b
    if debug: print(f"equation solved = {x},{y}")
    return (x,y)

    

def first():
    results = common()

    tot = sum([r[0]*3+r[1] for r in results if r[0] <= 100 and (r[0]*2%2 == 0) and r[1] <= 100 and (r[1]*2%2 == 0)])
    
    print(f"tot1={int(tot)}")
        

def second():
    results = common(10000000000000)

    tot = sum([ r[0]*3+r[1] for r in results if (r[0]*2%2 == 0) and (r[1]*2%2 == 0)])

    print(f"tot2={int(tot)}")

first()
second()