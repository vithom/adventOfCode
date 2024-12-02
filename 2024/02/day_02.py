from itertools import pairwise
import os

# file = os.path.dirname(__file__)+"/input_example.txt"
file = os.path.dirname(__file__)+"/input.txt"

debug = 0

with open(file, 'rt') as f:
    lines = f.readlines()

def common():
    pass

def isSafe(levels):
    previous = levels[0]
    cumul = 0

    for i in range(1,len(levels)):
        # 2nd rule
        if not (1 <= abs(levels[i] - previous) <= 3):
            break

        cumul += 1 if levels[i] > previous else -1

        previous = levels[i]
    else:
        # 1st rule
        if abs(cumul) == (len(levels) -1 ):
            return True
        
    return False


def first():
    sum = 0
    
    for line in lines:
        levels = [int(x) for x in line.split()]

        if isSafe(levels):
            sum += 1

    print(f"sum = {sum}")

def second():
    sum = 0
    
    for line in lines:
        levels = [int(x) for x in line.split()]

        if not isSafe(levels):
            for i in range(len(levels)):
                levels_trunc = levels[:i] + levels[i+1:]
                
                if isSafe(levels_trunc):
                    sum += 1
                    break
        else:
            sum += 1
    
    print(f"sum2 = {sum}")
            

first()
second()