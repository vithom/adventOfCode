import math
import numpy as np

with open("input_06.txt", 'rt') as f:
    lines = f.readlines()
# lines = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
# 'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
# 'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
# 'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
# 'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
# 'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']

def first_step():
    times = [int(x) for x in lines[0].split(':')[1].split()]
    distances = [int(x) for x in lines[1].split(':')[1].split()]

    total = 1
    win = [0, 0, 0, 0]
    for i in range(len(win)):
        for t in range(times[i]) :
            d = t * (times[i] - t)
            if d > distances[i]:
                win[i] += 1
        total *= win[i]

    print(f"first step: {total=}")

def second_step():

    times = [x for x in lines[0].split(':')[1].split()]
    distances = [x for x in lines[1].split(':')[1].split()]

    time = int("".join(times))
    distance = int("".join(distances))

    win = 0
    for t in range(time):
        d = t * (time - t)
        if d > distance:
            win += 1

    print(f"second step: {win=}")


first_step()
second_step()
