import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from mylib.input import input

file = os.path.dirname(__file__) + "/input_example.txt"
# file = os.path.dirname(__file__) + "/input_test.txt"
file = os.path.dirname(__file__)+"/input.txt"

logfile = os.path.dirname(__file__)+"/log_test.txt"

debug = 0

def common():
    dial = 50
    pass1 = 0
    pass2 = 0

    for move in input(file):
        n = int(move[1:])
        print(f"move({move} -> dial={dial})")
        
        for i in range(n):
            dial += 1 if move[0] == 'R' else -1
            if dial < 0 or dial > 99:
                dial = ((dial % 100) + 100) % 100
            
            if dial == 0: pass2 += 1
            
        if dial == 0: pass1 += 1
    
    print(f"1st part, password is {pass1}")
    print(f"2nd part, password is {pass2}")


def first():
    password = 0
    dial = 50

    for move in input(file):
        n = int(move[1:])
        way = move[0]

        if way == "R":
            dial += n
            while dial > 99:
                dial = dial - 100
        else: # "L"
            dial -= n
            while dial < 0:
                dial = dial + 100
        
        if dial == 0:
            password += 1
        
        # print(way, n, dial, password)
    
    print(f"1st part, password is {password}")

def second():
    dial = 50
    password = 0

    for move in input(file):
        n = int(move[1:])
        # print(f"move({move} -> dial={dial})")
        
        for i in range(n):
            dial += 1 if move[0] == 'R' else -1
            if dial < 0 or dial > 99:
                dial = ((dial % 100) + 100) % 100
            
            if dial == 0: password += 1
    
    print(f"2nd part, password is {password}")
    

first()
second()
# common()