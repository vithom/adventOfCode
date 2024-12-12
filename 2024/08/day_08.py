import os
from collections import defaultdict
from itertools import permutations

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

def common():
    map = input()
    size = (len(map[0]), len(map)) # width, height

    antennas = defaultdict(list)

    for h,l in enumerate(map):
        for w,c in enumerate(l):
            if c == '.': continue
            antennas[c].append( (w,h) )

    return size, antennas
    

def first():
    (width, height), antennas = common()

    if debug: print(width, height, antennas)
    antinodes = set()
    for ant in antennas.values():
        for a,b in permutations(ant, 2):
            delta = (b[0] - a[0], b[1]- a[1])
            pos1 = a[0] - delta[0], a[1] - delta[1]
            pos2 = b[0] + delta[0], b[1] + delta[1]
            if 0 <= pos1[0] < width and 0 <= pos1[1] < height: antinodes.add(pos1)
            if 0 <= pos2[0] < width and 0 <= pos2[1] < height: antinodes.add(pos2)
    
    print(f"tot1 = {len(antinodes)}")
        

def second():
    (width, height), antennas = common()

    antinodes = set()

    for ant in antennas.values():
        for a,b in permutations(ant, 2):
            delta = (b[0] - a[0], b[1]- a[1])

            antinodes.add(a)
            antinodes.add(b)
            
            out = False
            i = 1
            while not out:
                pos1 = a[0] - i*delta[0], a[1] - i*delta[1]
                if 0 <= pos1[0] < width and 0 <= pos1[1] < height:
                    antinodes.add(pos1)
                    i += 1
                else:
                    out = True
            
            out = False
            i = 1
            while not out:
                pos2 = b[0] + i*delta[0], b[1] + i*delta[1]
                if 0 <= pos2[0] < width and 0 <= pos2[1] < height:
                    antinodes.add(pos2)
                    i += 1
                else:
                    out = True
    
    print(f"tot2 = {len(antinodes)}")

first()
second()