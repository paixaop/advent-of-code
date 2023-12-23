import re
from mysolutions import common

def parse(data):
    return  data.split(",")

def hash(str):
    cvalue = 0

    for c in str:
        cvalue += ord(c)
        cvalue *= 17
        cvalue %= 256
    return cvalue


def part_a(data):
    data = parse(data)

    return sum([hash(s) for s in data])


def part_b(data):
    data = parse(data)
    total = 0

    return total

test_data_part_a = """\
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

test_data_part_b = test_data_part_a


if __name__ == "__main__":
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 1320)
    common.run(part_b, test_data_part_b, data, 0)