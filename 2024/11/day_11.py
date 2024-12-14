import os
import time
from functools import cache

# file = os.path.dirname(__file__)+"/input_example.txt"
file = os.path.dirname(__file__)+"/input.txt"

debug = 0

def input(trim = True):
    with open(file, 'rt') as f:
        lines = f.readlines()
        if trim:
            return [l.replace('\n', '') for l in lines]
        else:
            return lines
        


# take to long time for 75 blinks...
def common(nb_of_blink, stones):
    for blink in range(nb_of_blink):
        new_stones = list()

        for s in stones:
            new_stones += new_stone(s)
        
        stones = new_stones
    
    return len(stones)

@cache
def new_stone(s):
    if s == 0:
        return [1]
    
    n = len(str(s))
    if n % 2 == 0:
        return [ int(str(s)[:n//2]), int(str(s)[n//2:]) ]
    
    return [s * 2024]


@cache
def after(stone, blink):
    if blink == 0:
        return 1
    
    res = 0
    for s in new_stone(stone):
        res += after(s, blink-1)
    
    # res = sum([after(s,blink-1) for s in new_stone(stone)])

    return res


def first():
    stones = [int(x) for x in input()[0].split()]

    start = time.perf_counter()
    tot = common(25, stones)
    end = time.perf_counter()

    print(f"tot1 = {tot}", f"execution in {end-start:.6f}")


def second():
    stones = [int(x) for x in input()[0].split()]

    start = time.perf_counter()
    tot = 0
    for s in stones:
        tot += after(s, 75)
    end = time.perf_counter()

    print(f"tot2 = {tot}", f"execution in {end-start:.6f}")

first()
second()