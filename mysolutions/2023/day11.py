import math
from mysolutions import common


def get_row(data, row):
    return data[row]

def get_column(data, col):
    column = []
    for row in data:
        column.append(row[col])
    return column

def get_number_of_columns(data):
    return len(data[0])

def get_number_of_rows(data):
    return len(data)

def parse(data):
    data = list(map(lambda l: list(l), data.split("\n")))
    i = 0
    empty_columns = []
    while i < get_number_of_columns(data):
        column = get_column(data, i)
        if '#' not in column:
            empty_columns.append(i)
        i += 1

    i = 0
    empty_rows = []
    while i < get_number_of_rows(data):
        row = get_row(data, i)
        if '#' not in row:
            empty_rows.append(i)
        i += 1

    return {
        "universe": data,
        "empty_rows": empty_rows,
        "empty_columns": empty_columns,
    }

def count_empties(empties, cord):
    count = 0
    for x in empties:
        if x < cord:
            count += 1
        else:
            break

    return count

def expand(empties, cord, expand_factor):
    count = count_empties(empties, cord)
    if count != 0:
        return cord + count * expand_factor - count
    return cord

def get_galaxy_coords(data, expand_factor):
    galaxies = []
    for y, row in enumerate(data["universe"]):
        y = expand(data['empty_rows'], y, expand_factor)
        for x, char in enumerate(row):
            if char == '#':
                x = expand(data['empty_columns'], x, expand_factor)
                galaxies.append((x, y))

    return galaxies

def distance(p1, p2):
    dx = abs((p2[0] - p1[0]))
    dy = abs((p2[1] - p1[1]))
    return dx + dy

def calc_distance(data, expand_factor):
    data = parse(data)
    galaxies = get_galaxy_coords(data, expand_factor)

    total = 0
    for i, p1 in enumerate(galaxies):
        for p2 in galaxies[i + 1:]:
            total += distance(p1, p2)

    return total

def part_a(data):
    return calc_distance(data, 2)


def part_b(data):
    return calc_distance(data, 1000000)

test_data_part_a = """\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

test_data_part_b = test_data_part_a


if __name__ == "__main__":
    data = common.get_data(__file__)

    common.run(part_a, test_data_part_a, data, 374)
    common.run(part_b, test_data_part_b, data, 82000210)