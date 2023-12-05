import re

def part_a(data):
    data = data.split("\n")
    
    total = 0
    for line in data:
        if line == '':
            break
        chars = [*line]
        items = int(len(chars) / 2)
        compartment_1 = set(chars[:items])
        compartment_2 = set(chars[items:])
        common = list(compartment_1 & compartment_2)[0]

        if common.isupper():
            priority = ord(common) - 38
        else:
            priority = ord(common) - 96

        total += priority
    return total


def part_b(data):
    data = data.split("\n")
    
    total = 0
    elf_group_size = 3
    for i in range(0, len(data), elf_group_size):
        lines = data[i:i+elf_group_size]

        sets = []
        for i in range(elf_group_size):
            sets.append(set([*lines[i]]))
        common = sets[0]
        for i in range(1, elf_group_size):
            common = common & sets[i]

        common = list(common)[0]
        
        if common.isupper():
            priority = ord(common) - 38
        else:
            priority = ord(common) - 96

        total += priority
    return total

test_data_part_a = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

test_data_part_b = test_data_part_a


if __name__ == "__main__":
    from mysolutions import common
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 157)
    common.run(part_b, test_data_part_b, data, 70)