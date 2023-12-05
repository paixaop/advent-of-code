import re
from functools import reduce

def process(data):
    data = data.split("\n\n")
    elfs = list(map(lambda l: map(lambda x: int(x), l.split()), data))

    sums = list(
        map(lambda elf: 
            reduce(lambda a, e: a + e, elf), 
            elfs))
    sums.sort(reverse = True)
    return sums

def part_a(data):
    return process(data)[0]

def part_b(data):
    sums = process(data)
    return sums[0] + sums[1] + sums[2]

test_data_part_a = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

test_data_part_b = test_data_part_a

def test_a():
    assert part_a(test_data_part_a) == 24000
    print("Test of Part A: PASSED")

def test_b():
    assert part_b(test_data_part_b) == 45000
    print("Test of Part B: PASSED")


if __name__ == "__main__":
    match = re.search(r'(\d{4}).day(\d+)\.py$', __file__)
    if match is None: 
        raise Exception('Need folder to be year\dayN.py')
    
    day = int(match.group(2))
    year = int(match.group(1))
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
