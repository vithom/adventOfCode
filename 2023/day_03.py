with open("input_03.txt", 'rt') as f:
    lines = f.readlines()

lines_test = ['467..114..',
              '...*......',
              '..35..633.',
              '......#...',
              '617*......',
              '.....+.58.',
              '..592.....',
              '......755.',
              '...$.*....',
              '.664.598..']


def first_step():
    n = list()
    total = 0

    for i, line in enumerate(lines):
        # print(i, line)
        number = 0
        is_part = False
        for j, char in enumerate(line):
            if char.isdigit():
                number = 10 * number + int(char)

                # search for special char neighbors
                for y in [-1, 0, 1]:
                    for x in [-1, 0, 1]:
                        if 0 <= i + y < len(lines) and 0 <= j + x < len(line):
                            ch = lines[i + y][j + x]
                            if not ch.isdigit() and ch != '.' and ch != '\n':
                                is_part = True
            else:
                if number > 0:
                    if is_part:
                        n.append(number)
                        total += number
                    number = 0
                    is_part = False

    print('## first part:')
    print(sum(n))
    print(len(n))
    print(total)

def second_step():
    total = 0
    gears = dict()
    for i, line in enumerate(lines):
        number = 0
        pos = set()
        for j, char in enumerate(line):
            if char.isdigit():
                number = 10 * number + int(char)

                # search for special char '*' neighbors
                for y in [-1, 0, 1]:
                    for x in [-1, 0, 1]:
                        if 0 <= i + y < len(lines) and 0 <= j + x < len(line):
                            ch = lines[i + y][j + x]
                            if ch == '*':
                                pos.add((i+y, j+x))
            else:
                if number > 0:
                    for g in pos:
                        try:
                            gears[g]
                        except:
                            gears[g] = []
                        finally:
                            gears[g].append(number)
                    number = 0
                    pos = set()

    print(gears)
    for k, v in gears.items():
        if len(v) == 2:
            total += v[0] * v[1]

    print('## second part:')
    print(total)


first_step()
second_step()
