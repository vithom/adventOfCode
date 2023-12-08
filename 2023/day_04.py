import math
import numpy as np

with open("input_04.txt", 'rt') as f:
    lines = f.readlines()
# lines = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
# 'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
# 'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
# 'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
# 'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
# 'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']

def first_step():
    total = 0
    copies = np.ones(len(lines), dtype=int)
    for line in lines:
        card = line.split(':')[1]
        winningNbs = card.split('|')[0].split()
        gamingNbs = card.split('|')[1].split()

        found = 0
        for n in gamingNbs:
            if n in winningNbs:
                found += 1
        # print(f"found {found} numbers")

        if found >= 0:
            total += int(math.exp2(found-1))

    print(f"first step: {total=}")

def second_step():
    total = 0
    copies = np.ones(len(lines), dtype=int)
    for line in lines:
        card = line.split(':')[1]
        winningNbs = card.split('|')[0].split()
        gamingNbs = card.split('|')[1].split()

        found = 0
        for n in gamingNbs:
            if n in winningNbs:
                found += 1
        #print(f"found {found} numbers")

        if found > 0:
            copies[1:found+1] += copies[0]

        total += copies[0]
        copies = copies[1:]

    print(f"second step: {total=}")


first_step()
second_step()
