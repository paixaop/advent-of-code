import re
from mysolutions import common
from more_itertools import chunked

def parse(data):
    #data = data.split()
    return list(data)

def part_a(data):
    data = parse(data)
    total = 0

    start = 0
    while start < len(data) - 4:
        chunk = data[start:start+4]
        if all(chunk.count(c) == 1 for c in chunk):
            return start + 4
        start += 1

    return 0


def part_b(data):
    data = parse(data)
    total = 0

    start = 0
    while start < len(data) - 14:
        chunk = data[start:start+14]
        if all(chunk.count(c) == 1 for c in chunk):
            return start + 14
        start += 1

    return 0

test_data_part_a = """\
mjqjpqmgbljsphdztnvjfqwrcgsmlb"""

test_data_part_b = test_data_part_a


if __name__ == "__main__":
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 7)
    common.run(part_b, test_data_part_b, data, 19)