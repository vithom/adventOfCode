import os
import pprint
import re

file = os.path.dirname(__file__)+"/input_example.txt"
file = os.path.dirname(__file__)+"/input.txt"

debug = 0

def input(trim = True):
    with open(file, 'rt') as f:
        lines = f.readlines()
        if trim:
            return [l.replace('\n', '') for l in lines]
        else:
            return lines


def common(w,h):
    m = [[0 for x in range(w)] for y in range(h)]
    
    quadrants = [0, 0, 0, 0]

    for line in input():
        if debug: print(line)
        p,v = re.findall(r"=(-?\d+),(-?\d+)", line)
        if debug: print(p,v)
        
        # position after 100 moves
        final_x = ((int(v[0]) * 100) + int(p[0])) % w 
        final_y = ((int(v[1]) * 100) + int(p[1])) % h
        if debug: print(f"final pos = ({final_x},{final_y})")

        m[final_y][final_x] += 1

    middle = (len(m[0]) // 2, len(m) // 2)
    if debug: print("middle=", middle)

    quadrants = {1:[], 2:[], 3:[], 4:[]}

    quadrants[1] = [ m[y][x] for y in range(0,middle[1]) for x in range(0, middle[0])  if m[y][x] > 0]
    quadrants[2] = [ m[y][x] for y in range(0,middle[1]) for x in range(middle[0]+1, w) if m[y][x] > 0]
    quadrants[3] = [ m[y][x] for y in range(middle[1]+1, h) for x in range(0, middle[0]) if m[y][x] > 0]
    quadrants[4] = [ m[y][x] for y in range(middle[1]+1, h) for x in range(middle[0]+1, w) if m[y][x] > 0]

    if debug: print(quadrants)

    tot = 1
    for t in quadrants.values():
        tot *= sum(t)
    
    print(f"tot1={tot}")

def solve(part):
    quadrants = [0, 0, 0, 0]
    seconds = 100
    robots = []
    dimX = 101
    dimY = 103


    for line in input():
        line = line.strip()
        vals = []
        splitted = line.split("=")
        vals.append(int(splitted[1].split(" ")[0].split(",")[0]))
        vals.append(int(splitted[1].split(" ")[0].split(",")[1]))
        vals.append(int(splitted[2].split(",")[0]))
        vals.append(int(splitted[2].split(",")[1]))
        robots.append(vals)

    for robot in robots:
        posX = robot[0]
        posY = robot[1]
        for s in range(seconds):
            posX += robot[2]
            posY += robot[3]
            if posX >= dimX:
                posX = abs(posX - dimX)
            if posX < 0:
                posX = dimX + posX
            if posY >= dimY:
                posY = abs(posY - dimY)
            if posY < 0:
                posY = dimY + posY

        if posX < dimX // 2:
            if posY < dimY // 2:
                quadrants[0] += 1
            elif posY > dimY // 2:
                quadrants[2] += 1
        elif posX > dimX // 2:
            if posY < dimY // 2:
                quadrants[1] += 1
            elif posY > dimY // 2:
                quadrants[3] += 1

    print("ans: ", quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])

def first():
    # common(11,7)
    common(101,103)
    # solve(1)
        

def second():
    pass

first()
second()