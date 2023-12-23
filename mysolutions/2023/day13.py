from mysolutions import common

def parse(data):
    data = data.split("\n")

    parsed = []
    pattern = []
    for line in data:
        if not line:
            parsed.append(pattern)
            pattern = []
        else:
            l = list(line)
            pattern.append(l)

    if pattern:
        parsed.append(pattern)
    return parsed

def find_row(pattern):

    for row in range(1, len(pattern)):
        above = pattern[:row][::-1]
        bellow = pattern[row:]

        above = above[:len(bellow)]
        bellow = bellow[:len(above)]

        if above == bellow:
            return row
    return 0

def find_row_smudges(pattern, smudges = 0):

    for row in range(1, len(pattern)):
        above = pattern[:row][::-1]
        bellow = pattern[row:]
        
        above = above[:len(bellow)]
        bellow = bellow[:len(above)]

        diff = 0
        for x, y in zip(above, bellow):
            for a, b in zip(x, y):
                if a != b:
                    diff += 1
        
        if diff == 1:
            return row
    return 0

def part_a(data):
    data = parse(data)
    total = 0

    for pattern in data:
        horizontal = find_row(pattern)
        vertical = find_row(list(zip(*pattern)))
        total += vertical + 100 * horizontal

    return total


def part_b(data):
    data = parse(data)
    total = 0

    for pattern in data:
            horizontal = find_row_smudges(pattern, smudges=1)
            vertical = find_row_smudges(list(zip(*pattern)), smudges=1)
            total += vertical + 100 * horizontal

    return total

test_data_part_a = """\
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

test_data_part_b = test_data_part_a

if __name__ == "__main__":
    data = common.get_data(__file__)

    common.run(part_a, test_data_part_a, data, 405)
    common.run(part_b, test_data_part_b, data, 400)