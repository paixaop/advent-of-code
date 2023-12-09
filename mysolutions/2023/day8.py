import re
import math
from itertools import cycle

def parse(data):
    data = data.split("\n")

    instructions = list(data[0])

    network = {}
    start = ""
    for line in data[1:]:       
        match = re.search(r"(\w+)\s+=\s+\((\w+), (\w+)\)", line)
        if match is not None:
            if start == "":
                start = match.group(1)
            network[match.group(1)] = {
                "L": match.group(2),
                "R": match.group(3)
            }

    return {
        "instructions": instructions,
        "network": network,
        "start": start
    }

def parse_b(data):
    data = data.split("\n")

    instructions = list(data[0])

    pattern = r"(\w{3}) = \((\w{3}), (\w{3})\)"
    net = dict()
    for line in data[2:]:
        k, *v = re.fullmatch(pattern, line.rstrip()).groups()
        net[k] = v
    return {
        "instructions": instructions,
        "network": net,
    }

def part_a(data):
    data = parse(data)
    
    total = 0
    node = 'AAA'
    while True:
        for i in data['instructions']:
            node = data['network'][node][i]
            total += 1
            if node == 'ZZZ':
                return total
        
    return total



def count_steps(data, node):
    net = data['network']
    inst = data['instructions']
    for i, lr_idx in enumerate(cycle(map("LR".index, inst)), start=1):
        node = net[node][lr_idx]
        if node.endswith('Z'):
            return i
        
def part_b(data):
    data = parse_b(data)
    net = data['network']
    _node_iter = filter(lambda node: node.endswith('A'), net.keys())
    p2 = math.lcm(*(count_steps(data, node) for node in _node_iter))
    return p2

test_data_part_a = """\
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

test_data_part_b = """\
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


if __name__ == "__main__":
    from mysolutions import common
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 6)
    common.run(part_b, test_data_part_b, data, 6)