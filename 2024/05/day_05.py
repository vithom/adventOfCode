import os
from collections import defaultdict

from itertools import combinations

# file = os.path.dirname(__file__)+"/input_example.txt"
file = os.path.dirname(__file__)+"/input.txt"

debug = 0

with open(file, 'rt') as f:
    lines = f.readlines()

def common():
    sep = lines.index('\n')
    
    rules = lines[:sep]
    updates = lines[sep+1:]

    return ( [[int(n) for n in r.split('|')] for r in rules],
             [[int(n) for n in u.split(',')] for u in updates] )
    

def first():
    rules, updates = common()

    tot = 0
    for update in updates:
        valid = True
        for a,b in combinations(update, 2):
            for r in rules:
                if b == r[0] and a == r[1]:
                    valid = False
                    break
            
            if not valid:
                break
        else:
            # print(f"good update: {update}")
            tot += update[len(update)//2]
    
    print(f"tot1={tot}")

def second():
    rules, updates = common()

    wrongs = []
    for update in updates:
        valid = True
        for a,b in combinations(update, 2):
            for r in rules:
                if b == r[0] and a == r[1]:
                    valid = False
                    break
            
            if not valid:
                # print(f"wrong update: {update}")
                wrongs.append(update)
                break
    
    # print(wrongs)

    tot = 0
    for w in wrongs:        
        new = reorder(w, rules)
        tot += new[len(new)//2]
    
    print(f"tot2={tot}")



def reorder(tab, rules):
    if len(tab) < 1:
        return tab
    
    a, *rest = tab
    
    before = [b for b in rest for r in rules if b == r[0] and a == r[1]]
    after = [b for b in rest if b not in before]

    return(reorder(before, rules) + [a] + reorder(after, rules))

first()
second()