import os

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
    pass

def find_trails_number(map, point, previous = None, arrivals = None):
    elevation = int(map[point[1]][point[0]])
    
    if previous is not None:
        if elevation != previous + 1: return 0
    
    if elevation == 9:
        if arrivals is None:
            return 1
        else:
            if point in arrivals:
                return 0
            else:
                arrivals.add(point)
                return 1

    next = [(point[0]+p[0], point[1]+p[1]) for p in [(0,-1), (0,1), (1,0), (-1,0)] if 0 <= point[0]+p[0] < len(map[0]) and 0 <= point[1]+p[1] < len(map)]
    
    if debug: print(f"next={next}")
    
    return sum([find_trails_number(map, n, elevation, arrivals) for n in next])
    

def first():
    map = input()
    trailheads = [(x,y) for y,l in enumerate(map) for x,c in enumerate(l) if c == '0']

    if debug: print(f"trailheads = {trailheads}")

    tot = sum([find_trails_number(map, t, arrivals=set()) for t in trailheads])

    print(f"tot1 = {tot}")
        

def second():
    map = input()
    trailheads = [(x,y) for y,l in enumerate(map) for x,c in enumerate(l) if c == '0']

    tot = sum([find_trails_number(map, t) for t in trailheads])

    print(f"tot2 = {tot}")


first()
second()