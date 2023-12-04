import re

with open("input_02.txt", 'rt') as f:
    lines = f.readlines()

def first_step():
    total = 0
    for line in lines:
        game = line.split(':')

        sets = game[1].split(';')
        for s in sets:
            gNo = re.search("(\d+) green", s)
            bNo = re.search("(\d+) blue", s)
            rNo = re.search("(\d+) red", s)
            print(s, gNo.group(1), bNo.group(1), rNo.group(1))

        total += game[0]

first_step()