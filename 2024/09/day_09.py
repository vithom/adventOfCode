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
    pass



def first():
    disk = input()[0]
    
    layout = []
    file = True
    idx = 0
    
    for c in disk:
        for i in range(int(c)):
            layout.append( (file, idx) )
        if file: idx += 1
        file = not file
    
    if debug: print(disk)
    if debug: print(layout)

    reversed_idx = len(layout) - 1
    
    for i,a in enumerate(layout):
        if a[0]: # is a file
            continue
        else: # is free-space
            while not layout[reversed_idx][0]:
                reversed_idx -= 1
            
            if reversed_idx < i:
                break
                
            layout[i] = (True, layout[reversed_idx][1])
            layout[reversed_idx] = (False, 0)

    if debug: print("end:",layout)

    tot = sum(i*e[1] for i,e in enumerate(layout) if e[0])
    print(f"tot1={tot}")
        

def second():
    disk = input()[0]

    layout = []
    file = True
    idx = 0
    
    for c in disk:
        if int(c) > 0: layout.append( (file, idx, int(c)) )
        if file: idx += 1
        file = not file
    
    if debug: print(layout)

    if layout[-1][0]: idx = layout[-1][1]
    else: idx = layout[-2][1]

    for fileNo in range(idx, 0, -1):
        next = False
        
        for i, e in reversed(list(enumerate(layout))):
            if e[0] and e[1] == fileNo:
                break # found file        
        if debug: print(i, e)

        for j in range(i):
            f = layout[j]

            if not f[0] and f[2] >= e[2]:
                layout[j] = (True, fileNo, e[2])
                
                layout[i] = (False, 0, e[2])
                # check neighbours
                
                if i < len(layout)-1:
                    y = layout[i+1]
                    
                    if not y[0]:
                        layout[i] = (False, 0, layout[i][2] + y[2])
                        layout.pop(i+1)
                
                if i > 0:
                    x = layout[i-1]

                    if not x[0]:
                        layout[i] = (False, 0, layout[i][2] + x[2])
                        layout.pop(i-1)

                if f[2] - e[2] > 0:
                    layout.insert(j+1, (False, 0, f[2] - e[2]) )
                
                break
    
    if debug: print(layout)

    idx = 0
    tot = 0
    for i,e in enumerate(layout):
        for j in range(e[2]):
            if e[0]:
                tot += e[1] * idx
            idx += 1
    
    print(f"tot2={tot}")
    

first()
second()