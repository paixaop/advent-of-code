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


if __name__ == "__main__":
    from mysolutions import common
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 24000)
    common.run(part_b, test_data_part_b, data, 45000)
    
