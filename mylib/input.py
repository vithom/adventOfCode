import os

def input(file, trim = True):
    with open(file, 'rt') as f:
        lines = f.readlines()
        if trim:
            return [l.replace('\n', '') for l in lines]
        else:
            return lines

def input_raw(file):
    with open(file, 'r') as f:
        content = f.read()
    
    return content