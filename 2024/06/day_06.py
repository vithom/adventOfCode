import os

# file = os.path.dirname(__file__)+"/input_example.txt"
file = os.path.dirname(__file__)+"/input.txt"

debug = 0



def input():
    with open(file, 'rt') as f:
        lines = f.readlines()
        return [l.replace('\n', '') for l in lines]

def common():
    pass
    

def first():
    map = input()
    size = (len(map[0]), len(map)) # width, height
    
    pos = [(i,j) for i,l in enumerate(map) for j,c in enumerate(l) if c == "^"][0]
    movements = [(0,-1), (1,0), (0,1), (-1,0)]

    print(pos)
    
    way = 0
    moves = set()
    moves.add(pos)
    while True:
        next_pos = (pos[0]+movements[way][1], pos[1]+movements[way][0])
        if next_pos[0] >= size[1] or next_pos[1] >= size[0] or next_pos[0] < 0 or next_pos[1] < 0:
            print(f"out with next_pos={next_pos}, way={way}")
            break
        next = map[next_pos[0]][next_pos[1]]
        if next == '#':
            print(f"found # @{next_pos}, way={way}")
            way = way + 1 if way + 1 < len(movements) else 0
            next_pos = (pos[0]+movements[way][1], pos[1]+movements[way][0])
        pos = next_pos
        moves.add(pos)
    
    print(f"moves={len(moves)}")

        

def second():
    pass

first()
second()