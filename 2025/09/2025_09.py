import os
import sys
import itertools

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
    tiles = input(file)

    surfaces = []

    for tile in itertools.combinations(tiles, 2):
        t1 = tile[0].split(',')
        t2 = tile[1].split(',')

        surfaces.append((abs(int(t1[0]) - int(t2[0])) + 1) * (abs(int(t1[1]) - int(t2[1])) + 1))
        # print(tile, surface)

    print(f"1st part, answer = {max(surfaces)}")


def second():
    print(f"2nd part, answer = ")


# common()
first()
# second()
