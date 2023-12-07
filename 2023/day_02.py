import re

with open("input_02.txt", 'rt') as f:
    lines = f.readlines()

def first_step():
    total = 0
    for line in lines:
        stop = False

        game = line.split(':')
        gameNo = re.search('Game (\d+)', game[0])
        #print(gameNo.group(1))

        sets = game[1].split(';')
        for s in sets:
            gNo = re.search("(\d+) green", s)
            bNo = re.search("(\d+) blue", s)
            rNo = re.search("(\d+) red", s)

            if gNo and int(gNo.group(1)) > 13:
                stop = True
                break
            if bNo and int(bNo.group(1)) > 14:
                stop = True
                break
            if rNo and int(rNo.group(1)) > 12:
                stop = True
                break

            #print(s, gNo.group(1), bNo.group(1), rNo.group(1))
        if stop:
            continue
        total += int(gameNo.group(1))

    print(f"first step: {total=}")

def second_step():
    total = 0
    for line in lines:
        cubes = {'greens':0, 'blues':0, 'reds':0}
        for s in line.split(':')[1].split(';'):
            gNo = re.search("(\d+) green", s)
            bNo = re.search("(\d+) blue", s)
            rNo = re.search("(\d+) red", s)

            if gNo and int(gNo.group(1)) > cubes['greens']: cubes['greens'] = int(gNo.group(1))
            if bNo and int(bNo.group(1)) > cubes['blues']: cubes['blues'] = int(bNo.group(1))
            if rNo and int(rNo.group(1)) > cubes['reds']: cubes['reds'] = int(rNo.group(1))

        total += cubes['greens'] * cubes['blues'] * cubes['reds']

    print(f"second step: {total=}")

first_step()
second_step()