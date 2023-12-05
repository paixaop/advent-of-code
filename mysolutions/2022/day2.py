import re

match = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

i_win = {
    "A": "C",
    "B": "A",
    "C": "B"
}

scores = {
    "A": 1,
    "B": 2,
    "C": 3,
    "WIN": 6,
    "LOSE": 0,
    "DRAW": 3
}

def score(elf, me):
    s = scores[me]
    if i_win[me] == elf:
        s += scores["WIN"]
    elif elf == me:
        s += scores["DRAW"]
    else: 
        s += scores["LOSE"]
    return s

def part_a(data):
    data = data.split("\n")
    
    total = 0
    for line in data:
        if line == '':
            break

        elf, me = line.split()
        total += score(elf, match[me])

    return total


outcome = {
    "X": "LOSE",
    "Y": "DRAW",
    "Z": "WIN"
}

options = {
    "LOSE": {
        "A": "C",
        "B": "A",
        "C": "B"
    },
    "DRAW": {
        "A": "A",
        "B": "B",
        "C": "C"
    },
    "WIN": {
        "A": "B",
        "B": "C",
        "C": "A"
    },
}

def part_b(data):
    data = data.split("\n")
    
    total = 0
    for line in data:
        if line == '':
            break

        elf, action = line.split()
        result = outcome[action]
        me = options[result][elf]

        total += score(elf, me)

    return total

test_data_part_a = """\
A Y
B X
C Z
"""

test_data_part_b = test_data_part_a


if __name__ == "__main__":
    from mysolutions import common
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 15)
    common.run(part_b, test_data_part_b, data, 12)