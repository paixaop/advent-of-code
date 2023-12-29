from mysolutions import common

def parse(data):
    data = data.splitlines()

    parsed = []
    for line in data:
        parsed.append(list(line))

    return parsed

def get_start(data):
    start = None
    for r, row in enumerate(data):
        try:
            c = row.index('S')
            start = (r, c)
            break
        except ValueError:
            pass
    
    return start

def count_steps(data):
    count = 0
    for r, row in enumerate(data):
        for c, char in enumerate(row):
            if char == "O":
                count += 1
    return count

def take_step(data):
    steps_taken = []
    for r, row in enumerate(data):
        for c, char in enumerate(row):
            if char in "SO":
                steps_taken.append((r, c))

    for step in steps_taken:    
        r, c = step
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if data[r][c] == 'O' or  data[r][c] == 'S':
                data[r][c] = '.'
            if 0 <= r + dr < len(data) and 0<= c + dc < len(row):
                if data[r + dr][c + dc] != '#':
                    data[r + dr][c + dc] = 'O'

    return data

def part_a(data):
    data = parse(data)
    total = 0
    start = get_start(data)
    if not start:
        return 0
        
    for i in range(64):
        take_step(data)
    total = count_steps(data)
    return total


def part_b(data):
    data = parse(data)
    total = 0

    return total

test_data_part_a = """\
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""

test_data_part_b = test_data_part_a


if __name__ == "__main__":
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 42)
    common.run(part_b, test_data_part_b, data, 0)