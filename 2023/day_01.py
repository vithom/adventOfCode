import os
import re

with open(os.path.dirname(__file__)+"/input_01_2.txt", 'rt') as f:
    lines = f.readlines()


def first_step():
    total = 0
    for line in lines:
        m = re.findall(r'\d', line)
        if m:
            total += int(m[0] + m[-1])
    print(f"1st part: {total}")

def first_step_other_way():
    total = 0
    for line in lines:
        # m = {c: i for i, c in enumerate(line) if c.isdigit()}
        m = [(i, c) for i, c in enumerate(line) if c.isdigit()]

        # print(m)

        total += int(m[0][1] + m[-1][1])
    
    print(f"1st part: {total}")


def second_step():
    total = 0
    for line in lines:
        first = ""
        last = ""
        digits = [d for d in re.finditer(r'\d', line)]
        letters = [l for l in re.finditer("one|two|three|four|five|six|seven|eight|nine", line)]

        if (len(letters) == 0) or (digits[0].start() < letters[0].start()):
            first = digits[0].group(0)
            # print(f"first: {digits[0].group(0)}")
        else:
            # print(f"first: {letters[0].group(0)}")
            for item in zip(["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                            ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
                if item[1] == letters[0].group(0):
                    first = item[0]
                    break

        if (len(letters) == 0) or digits[-1].start() > letters[-1].start():
            last = digits[-1].group(0)
        else:
            for item in zip(["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                            ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
                if item[1] == letters[-1].group(0):
                    last = item[0]
                    break

        total += int(first + last)

    print(f'2nd part: {total} (wrong)')

def second_step_enhanced():
    total = 0
    for line in lines:
        first = ""
        last = ""

        for i, c in enumerate(line):
            if c.isdigit():
                first = c
                break

            for letter in zip(["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                              ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
                if line[i:i + len(letter[1])] == letter[1]:
                    first = letter[0]
                    break

            if first != "":
                break

        # for c in line[::-1]:
        for i, c in enumerate(reversed(line)):
        #for i, c in enumerate(line[::-1]):
            if c.isdigit():
                last = c
                break

            for letter in zip(["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                              ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
                if line[len(line)-i-1:len(line)-i-1 + len(letter[1])] == letter[1]:
                    last = letter[0]
                    break

            if last != "":
                break

        # print(line.strip() + " -> " + first + last)
        total += int(first + last)
    print(f'2nd part: {total}')

first_step()
first_step_other_way()
second_step()
second_step_enhanced()
