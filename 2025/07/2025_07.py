import os
import sys
from functools import reduce

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from mylib.input import input, input_raw

file = os.path.dirname(__file__) + "/input_example.txt"
# file = os.path.dirname(__file__) + "/input_test.txt"
file = os.path.dirname(__file__)+"/input.txt"

# logfile = os.path.dirname(__file__)+"/log_test.txt"

debug = 0

def common():
    pass

def first():
    splits = 0
    beams = set()

    for line in input(file):
        if line.find('S') != -1:
            beams.add(line.index('S'))
        
        pos = [i for i, c in enumerate(line) if c == '^']
        
        if len(pos) > 0:
            for p in pos:
                if p in beams:
                    splits += 1
                    beams.remove(int(p))
                    beams.add(p-1)
                    beams.add(p+1)

    print(f"1st part, answer = {splits}")


def second():
    cumul = []
    
    for line in input(file):
        # print(f"{line=}")
        if line.find('S') != -1:
            for i,c in enumerate(line):
                if c == '.': cumul.append(0)
                if c == 'S': cumul.append(1)
        
        else:
            pos = [i for i, c in enumerate(line) if c == '^']
            if len(pos) > 0:
                # print(pos)
                for p in pos:
                    if cumul[p] > 0:
                        cumul[p-1] += cumul[p]
                        cumul[p+1] += cumul[p]
                        cumul[p] = 0
        # print(f"cumu='{cumul}'")

    print(f"2nd part, answer = {sum(cumul)}")


common()
first()
second()
