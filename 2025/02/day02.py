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
    ranges = input(file)[0].split(',')

    sum = 0

    for r in ranges:
        start, end = r.split('-')

        for i in range(int(start), int(end)+1):
            n = len(str(i))
            
            if n % 2 == 0: # even
                middle = int(n / 2)
                
                for j in range(middle):
                    if str(i)[j] != str(i)[middle+j]:
                        break
                else:
                    # print(f"Found a duplicate: {i}")
                    sum += i
                
                # ou bien
                # if str(i)[:middle] == str(i)[middle:]:
                #     sum += i
    
    print(f"1st part, sum={sum}")

def second():
    ranges = input(file)[0].split(',')

    sum = 0

    for z,r in enumerate(ranges):
        start, end = r.split('-')

        for i in range(int(start), int(end)+1):
            n = len(str(i))
            
            for j in range(1, int(n/2)+1):
                s = str(i)[:j]
                r = n/j
                if (r.is_integer()):
                    repeated = s * int(r)
                    if repeated == str(i):
                        # print(f"Found a repeat match: {i} -> {repeated}")
                        sum += i
                        break
                # print(f"i={i}, s={s}, r={r}, is integer={r.is_integer()}")

            
                
            
        
        # if z == 1 : break
    
    print(f"2nd part, sum={sum}")
    

first()
second()
# common()