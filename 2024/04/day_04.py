import os

# file = os.path.dirname(__file__)+"/input_example.txt"
file = os.path.dirname(__file__)+"/input.txt"

debug = 0

with open(file, 'rt') as f:
    lines = f.readlines()

def common():
    pass
    

def first():
    sum = 0
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "X":
                print(f"found X @({i},{j})")
                
                if line[j+1:j+4] == "MAS":
                    print(f"  - found XMAS ->")
                    sum += 1

                if j > 2:
                    if line[j-3:j] == "SAM":
                        print(f"  - found XMAS <-")
                        sum += 1

                
                if i < len(lines)-3:
                    if (lines[i+1][j] + lines[i+2][j] + lines[i+3][j]) == "MAS":
                        print(f"  - found XMAS |")
                        sum += 1
                    
                    if j > 2:
                        if (lines[i+1][j-1] + lines[i+2][j-2] + lines[i+3][j-3]) == "MAS":
                            print(f"  - found XMAS /")
                            sum += 1

                    if j < (len(line)-4):
                        if (lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3]) == "MAS":
                            print(f"  - found XMAS diagonally \\")
                            sum += 1

                
                if i > 2:
                    if (lines[i-1][j] + lines[i-2][j] + lines[i-3][j]) == "MAS":
                        print(f"  - found XMAS vertically |^")
                        sum += 1

                    if j > 2:
                        if (lines[i-1][j-1] + lines[i-2][j-2] + lines[i-3][j-3]) == "MAS":
                            print(f"  - found XMAS diagonally ^\\")
                            sum += 1
                    
                    if j < len(line)-4:
                        if (lines[i-1][j+1] + lines[i-2][j+2] + lines[i-3][j+3]) == "MAS":
                            print(f"  - found XMAS diagonally ^/")
                            sum += 1
    
    print(f"sum = {sum}")


def second():
    sum = 0
    for i in range(1,len(lines)-1):
        line = lines[i]
        for j in range(1, len(line)-1):
            if line[j] == 'A':
                if ( (lines[i-1][j-1] == "M" and lines[i+1][j+1] == "S") \
                    or (lines[i-1][j-1] == "S" and lines[i+1][j+1] == "M") ) \
                    and \
                    ( (lines[i-1][j+1] == "M" and lines[i+1][j-1] == "S") \
                     or (lines[i-1][j+1] == "S" and lines[i+1][j-1] == "M") ):
                    print(f"found 'X' @({i},{j})")
                    sum += 1
    
    print(f"sum = {sum}")

first()
second()