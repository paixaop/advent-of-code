import re
import math

def part_a(data):
    data = data.split("\n")
    
    total = 0
    for line in data:
        match = re.search(r': ([^|]+)\|(.*)', line)
        if match is not None:
            winning = set(match.group(1).split())
            i_have = set(match.group(2).split())
            matches = i_have.intersection(winning)

            if len(matches) > 0:
                total += int(math.pow(2, len(matches) - 1))

    return total

def process(copies, cards, c):
    copies.append(c)
    if cards[c] > 0: 
        for j in range(c + 1, c + 1 + cards[c]):
            copies = process(copies, cards, j)

    return copies

def part_b(data):
    data = data.split("\n")

    total = 0
    copies = []
    cards = dict()
    for line in data:
        match = re.search(r'Card\s+(\d+): ([^|]+)\|(.*)', line)
        if match is not None:
            card = int(match.group(1))
            winning = set(match.group(2).split())
            i_have = set(match.group(3).split())
            matches = i_have.intersection(winning)
            cards[card] = len(matches)
    
    for c in cards:
        copies = process(copies, cards, c)

    copies.sort()
    return len(copies)

test_data_part_a = """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

test_data_part_b = test_data_part_a


if __name__ == "__main__":
    from mysolutions import common
    data = common.get_data(__file__)

    common.run(part_a, test_data_part_a, data, 13)
    common.run(part_b, test_data_part_b, data, 30)
    