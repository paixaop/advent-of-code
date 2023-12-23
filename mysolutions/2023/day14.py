import re
from mysolutions import common

def parse(data):
    data = data.split("\n")

    parsed = []
    for line in data:
        parsed.append(list(line))

    return parsed

def slide_rocks_we(data, row, check= '.', swap= 'O'): 
    while True:
        switch = False
        for i in range(len(data[row]) - 1):
            if data[row][i] == check:
                if data[row][i+1] == swap:
                    data[row][i] = swap
                    data[row][i+1] = check
                    i += 1
                    switch = True
        
        if not switch:
            break

def slide_rocks_ns(data, col, check= '.', swap= 'O'): 
    while True:
        switch = False
        for i in range(len(data) - 1):
            if data[i][col] == check:
                if data[i+1][col] == swap:
                    data[i][col] = swap
                    data[i+1][col] = check
                    i += 1
                    switch = True
        
        if not switch:
            break

def calc_weight(data):
    total = 0
    number_of_rows = len(data)
    for i, row in enumerate(data):
        for j, item in enumerate(row):
            if item == 'O':
                total += number_of_rows - i

    return total

def part_a(data):
    data = parse(data)
    total = 0
    
    south_edge = len(data)
    
    #data = [list(x) for x in zip(*data)]
    for col in range(len(data)):
        #column = remove_column(data, col)
        slide_rocks_ns(data, col)
    total = calc_weight(data)
    return total

def north(data):
    for col in range(len(data)):
        slide_rocks_ns(data, col)

def south(data):
    for col in range(len(data)):
        slide_rocks_ns(data, col, check = 'O', swap = '.')

def west(data):
    for col in range(len(data)):
        slide_rocks_we(data, col)

def east(data):
    for col in range(len(data)):
        slide_rocks_we(data, col, check = 'O', swap = '.')


def part_b(data):
    data = parse(data)
    total = 0
    
    tdata = "\n".join("".join(row) for row in data)
    seen = { tdata }
    loop = [tdata]
    i = 0
    while True:
        i += 1
        north(data)
        west(data)
        south(data)
        east(data)

        tdata = "\n".join("".join(row) for row in data)
        if tdata in seen:
            break

        seen.add(tdata)
        loop.append(tdata)
    
    loop_start = loop.index(tdata)

    data = loop[(1000000000 - loop_start) % (i - loop_start) + loop_start].splitlines()
    total = sum(row.count("O") * (len(data) - r) for r, row in enumerate(data))
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
    common.run(part_b, test_data_part_b, data, 64)