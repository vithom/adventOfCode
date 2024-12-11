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
    return [( int(l.split(':')[0]), list(map(int, l.split(':')[1].split())) ) for l in input()]

def evaluate(res, values, acc, third = False):
    if len(values) == 0:
        return res == acc
    else:
        if third:
            return evaluate(res, values[1:], values[0] * acc, True) or evaluate(res, values[1:], values[0] + acc, True) or evaluate(res, values[1:], int(str(acc) + str(values[0])), True )
        else:
            return evaluate(res, values[1:], values[0] * acc) or evaluate(res, values[1:], values[0] + acc)
    

def first():
    equations = common()

    tot = 0
    for res, values in equations:
        if  evaluate(res, values[2:], values[0] * values[1]) or evaluate(res, values[2:], values[0] + values[1]):
            tot += res

    print(f"tot_1 = {tot}")

def second():
    equations = common()

    tot = 0
    for res, values in equations:
        if evaluate(res, values[2:], values[0] * values[1], True) \
        or evaluate(res, values[2:], values[0] + values[1], True) \
        or evaluate(res, values[2:], int(str(values[0]) + str(values[1])), True):
            tot += res

    print(f"tot_2 = {tot}")

first()
second()