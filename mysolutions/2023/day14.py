import re
from mysolutions import common

def parse(data):
    data = data.split("\n")

    parsed = []
    for line in data:
        parsed.append(list(line))

    return parsed

def slide_rocks(column):
    
    while True:
        switch = False
        for i in range(len(column) - 1):
            if column[i] == '.':
                if column[i+1] == 'O':
                    column[i] = 'O'
                    column[i+1] = '.'
                    i += 1
                    switch = True
        
        if not switch:
            break
    
    total = 0
    for i in range(len(column)):
        if column[i] == 'O':
            total += len(column) - i

    return total


def remove_column(ll, n):
    c = []
    for row in ll:
        for i, col in enumerate(row):
            if i == n:
                c.append(col)
    return c


def part_a(data):
    data = parse(data)
    total = 0
    
    south_edge = len(data)
    for col in range(len(data[0])):
        column = remove_column(data, col)
        total += slide_rocks(column)
        
    return total


def part_b(data):
    data = parse(data)
    total = 0

    return total

test_data_part_a = """\
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

test_data_part_b = test_data_part_a


if __name__ == "__main__":
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 136)
    common.run(part_b, test_data_part_b, data, 0)