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
    sum = 0
    for bank in input(file):
        # print(bank)
        c_temp = 0
        i_first = 0
        for i,c in enumerate(bank):
            if int(c) > c_temp:
                c_temp = int(c)
                i_first = i
            if int(c) == 9 or i == len(bank)-2:
                break
        
        second = max(bank[i_first+1:])
        
        sum += int(str(c_temp)+second)
        # print(f"{c_temp=}, {i_first=}, {second=}")

    print(f"1st part, answer = {sum}")

def second():
    sum = 0
    for bank in input(file):
        # print(bank)
        index = 0
        battery = ''

        for k in range(11,-1,-1):
            n = 0
            # print(k)
            for i in range(index, len(bank) - k):
                num = int(bank[i])
                if n < num:
                    n = num
                    index = i+1
            
            battery += str(n)
        
        # print(f"{battery=}")
        sum += int(battery)
        

        
        
        # sum += int(str(c_temp)+second)
        # print(f"{c_temp=}, {i_first=}, {second=}")

    print(f"2nd part, answer = {sum}")
    

first()
second()
# common()