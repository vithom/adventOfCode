# file = "input_example.txt"
file = "input_01.txt"

with open(file, 'rt') as f:
    lines = f.readlines()

def common():
    list1 = []
    list2 = []

    for line in lines:
        tab = line.split()
        list1.append(int(tab[0]))
        list2.append(int(tab[1]))
    
    return (list1, list2)
    

def first():
    list1, list2 = common()

    distances = []
        
    if len(list1) == len(list2):
        while(len(list1) > 0):
            a = min(list1)
            b = min(list2)
            distances.append(abs(a-b))

            list1.remove(a)
            list2.remove(b)
        
        print(distances)

        s = sum(distances)

        print(f"final sum: {s}")
        

def second():
    list1, list2 = common()
    
    similarity = []

    for i in list1:
        similarity.append(i * list2.count(i))

    print(similarity)

    score = sum(similarity)
    
    print(f"final similarity score: {score}")

first()
second()