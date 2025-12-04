import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from mylib.input import input

file = os.path.dirname(__file__) + "/input_example.txt"
# file = os.path.dirname(__file__) + "/input_test.txt"
file = os.path.dirname(__file__)+"/input.txt"

# logfile = os.path.dirname(__file__)+"/log_test.txt"

debug = 0

def common():
    pass


def first():
    ground = input(file)
    moves = [(-1,-1), (0,-1), (1,-1),
             (-1,0),         (1,0),
             (-1,1),  (0,1),  (1,1)]
    counter = 0

    for y,line in enumerate(ground):    
        for x,c in enumerate(line):
            count = 0
            if c == '@':
                for mx,my in moves:
                    if y+my < 0 or y+my >= len(ground) or x+mx < 0 or x+mx >= len(line):
                        continue
                    else:
                        if ground[y+my][x+mx] == '@': count += 1
                
                if count < 4:
                    counter += 1

    print(f"1st part, answer = {counter}")

def second():
    ground = input(file)
    moves = [(-1,-1), (0,-1), (1,-1),
             (-1,0),         (1,0),
             (-1,1),  (0,1),  (1,1)]
    counter = 0

    while 1:
        removing = []
        for y,line in enumerate(ground):    
            for x,c in enumerate(line):
                count = 0
                if c == '@':
                    for mx,my in moves:
                        if y+my < 0 or y+my >= len(ground) or x+mx < 0 or x+mx >= len(line):
                            continue
                        else:
                            if ground[y+my][x+mx] == '@': count += 1
                    
                    if count < 4:
                        counter += 1
                        removing.append((x,y))
                        # ground[y] = ground[y][:x-1]+'.'+ground[y][x+1:]
        
        # print(removing)
        for x,y in removing:
            ground[y] = ground[y][:x]+'.'+ground[y][x+1:]

        if len(removing) == 0:
            break

    print(f"2nd part, answer = {counter}")
    

first()
second()
# common()