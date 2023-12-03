import re

def check_line(data, line, start, finish):
    if line < 0 or line >= len(data):
        return False
    
    if start < 0:
        start = 0

    if finish > len(data[line]):
        finish = len(data[line])

    res = re.search(r'[^.\d]', data[line][start:finish])
    return res is not None

def part_a(data):
    data = data.split("\n")
    
    total = 0
    for i in range(len(data)):
        for match in re.finditer(r'(\d+)', data[i]):
        
            num = int(match.group(1))
            start = match.start() - 1
            finish = match.end() + 1

            if check_line(data, i, start, finish) or \
               check_line(data, i - 1, start, finish) or \
               check_line(data, i + 1, start, finish):
                total += num

    return total


def check(data, line, pos):
    if line < 0 or line > len(data):
        return []
    
    gears = []
    for match in re.finditer(r'(\d+)', data[line]):
        num = int(match.group(1))
        if pos >= match.start() - 1 and pos <= match.end():
            gears.append(num)
    
    return gears

def part_b(data):
    data = data.split("\n")
    
    total = 0
    for i in range(len(data)):
        for match in re.finditer(r'\*', data[i]):
            gears = []
            gears += check(data, i, match.start())
            gears += check(data, i - 1, match.start())
            gears += check(data, i + 1, match.start())
            
            if len(gears) == 2:
                total += gears[0] * gears[1]

    return total

test_data_part_a = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

test_data_part_b = test_data_part_a

def test_a():
    assert part_a(test_data_part_a) == 4361
    print("Test of Part A: PASSED")

def test_b():
    assert part_b(test_data_part_b) == 467835
    print("Test of Part B: PASSED")


if __name__ == "__main__":
    day = 3
    year = 2023
    print("\n\nSolutions for {}/{}\n".format(year, day))

    try:
        from aocd import get_data
        data = get_data(day=day, year=year)
    except Exception as e:
        print("Error: {}\n".format(e))
        exit()
    
    test_a()
    print("Part A: {}\n".format(part_a(data)))

    test_b()
    print("Part B: {}\n".format(part_b(data)))
