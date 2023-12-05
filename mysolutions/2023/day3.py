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


if __name__ == "__main__":
    from mysolutions import common
    data = common.get_data(__file__)

    common.run(part_a, test_data_part_a, data, 4361)
    common.run(part_b, test_data_part_b, data, 467835)
