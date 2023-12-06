import re
import portion as P

def part_a(data):
    data = data.split("\n")
    
    total = 0
    for line in data:
        if line == '':
            break
        match = re.search(r'(\d+)-(\d+),(\d+)-(\d+)', line)
        if match is not None:
            elf_1 = P.closed(int(match.group(1)), int(match.group(2)))
            elf_2 = P.closed(int(match.group(3)), int(match.group(4)))
            i = elf_1 & elf_2
            if i == elf_1 or i == elf_2:
                total += 1 
        
    return total


def part_b(data):
    data = data.split("\n")
    
    total = 0
    for line in data:
        if line == '':
            break
        match = re.search(r'(\d+)-(\d+),(\d+)-(\d+)', line)
        if match is not None:
            elf_1 = P.closed(int(match.group(1)), int(match.group(2)))
            elf_2 = P.closed(int(match.group(3)), int(match.group(4)))
            i = elf_1 & elf_2
            if i    :
                total += 1 
        
    return total

test_data_part_a = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

test_data_part_b = test_data_part_a


if __name__ == "__main__":
    from mysolutions import common
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 2)
    common.run(part_b, test_data_part_b, data, 4)