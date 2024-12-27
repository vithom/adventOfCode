import os

# test for adding a global lib
#
# sys.path.append(os.path.join(os.getcwd(), 'mylib'))
# from input import input, input_raw

# file = os.path.dirname(__file__)+"/input_example.txt"
file = os.path.dirname(__file__)+"/input.txt"

debug = 0

def dprint(*var):
    if debug: print(*var)

def input(trim = True):
    with open(file, 'rt') as f:
        lines = f.readlines()
        if trim:
            return [l.replace('\n', '') for l in lines]
        else:
            return lines

def common():
    pass
    

def first():
    pass
        

def second():
    pass

first()
second()