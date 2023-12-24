import sys
from mysolutions import common

def parse(data):
    data = data.splitlines()

    parsed = []
    for line in data:
        if line:
            parsed.append(list(line))

    return parsed

visited = set()
EAST = 0
SOUTH = 1
WEST = 2
NORTH = 3


def next_step(char, row, col, direction):
    if char == ".":
        if direction == NORTH:
            row -= 1
        elif direction == SOUTH:
            row += 1
        elif direction == WEST:
            col -= 1
        elif direction == EAST:
            col += 1
    elif char == "\\":
        if direction == NORTH:
            direction = WEST
            col -= 1
        elif direction == SOUTH:
            direction = EAST
            col += 1
        elif direction == WEST:
            direction = NORTH
            row -= 1
        elif direction == EAST:
            direction = SOUTH
            row += 1
    elif char == "/":
        if direction == NORTH:
            direction = EAST
            col += 1
        elif direction == SOUTH:
            direction = WEST
            col -= 1
        elif direction == WEST:
            direction = SOUTH
            row += 1
        elif direction == EAST:
            direction = NORTH
            row -= 1
    elif char == '-':
        if direction == EAST:
            col += 1
        elif direction == WEST:
            col -= 1
    elif char == '|':
        if direction == SOUTH:
            row += 1
        elif direction == NORTH:
            row -= 1

    return (row, col, direction)


def beam(contraption, row= 0, col= 0, direction= EAST):
    global visited

    if row >= len(contraption) or row < 0:
        return
    
    if col >= len(contraption[0]) or col < 0:
        return
    
    node = (row, col, direction)
    if node in visited:
        return

    visited.add(node)
    char = contraption[row][col]

    if char in ".\\/":
        row, col, direction = next_step(char, row, col, direction)
        beam(contraption, row, col, direction=direction)

    if char == "|":
        if direction == EAST or direction == WEST:
            beam(contraption, row + 1, col, direction=SOUTH)
            beam(contraption, row - 1, col, direction=NORTH)
        else:
            row, col, direction = next_step(char, row, col, direction)
            beam(contraption, row, col, direction=direction) 

    if char == "-":
        if direction == NORTH or direction == SOUTH:
            beam(contraption, row, col + 1, direction=EAST)
            beam(contraption, row, col - 1, direction=WEST)
        else:
            row, col, direction = next_step(char, row, col, direction)
            beam(contraption, row, col, direction=direction)

    return

def energized():
    global visited

    t = set()
    for item in visited:
        t.add((item[0], item[1]))
    return len(t)

def run_beam(data, row=0, col=0, direction=EAST):
    global visited

    visited = set()
    beam(data, row, col, direction)
    return energized()

def part_a(data):
    data = parse(data)
    
    return run_beam(data)

def part_b(data):
    global visited
    data = parse(data)
    
    total = 0
    for row in range(len(data)):
        e = run_beam(data, row, 0, EAST)
        w = run_beam(data, row, len(data[0]) - 1, WEST)
        total = max([total, e, w])
    
    for col in range(1, len(data[0])):
        s = run_beam(data, 0, col, SOUTH)
        n = run_beam(data, len(data) - 1, col, NORTH)
        total = max([total, s, n])

    return total

test_data_part_a = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""

test_data_part_b = test_data_part_a


if __name__ == "__main__":
    data = common.get_data(__file__)
    sys.setrecursionlimit(10000)
    common.run(part_a, test_data_part_a, data, 46)
    common.run(part_b, test_data_part_b, data, 51)