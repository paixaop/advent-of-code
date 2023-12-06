import re
import portion as P

def parse(data):
    data = data.split("\n")
    stacks = []
    moves = []
    
    for line in data:
        match = re.search(r'\[', line)
        if match is not None:
            for i, box in enumerate([*line[1::4]]):
                if len(stacks) < i + 1:
                    stacks.append([])
                if box != ' ':
                    stacks[i].append(box)
        
        
        match = re.search(r'move (\d+) from (\d+) to (\d+)', line)
        if match is not None:
            moves.append({
                "boxes": int(match.group(1)),
                "from": int(match.group(2)) - 1,
                "to": int(match.group(3)) - 1
            })

    for i, s in enumerate(stacks):
        s.reverse()
    return {
        "stacks": stacks,
        "moves": moves
    }

def move(stacks, n, from_stack, to_stack):
    for i in range(n):
        box = stacks[from_stack].pop()
        stacks[to_stack].append(box)
    return stacks

def create_mover_9001(stacks, n, from_stack, to_stack):
    boxes = stacks[from_stack][-n:]
    del stacks[from_stack][-n:]
    stacks[to_stack] += boxes

def part_a(data):
    data = parse(data)
    stacks = data['stacks']
    moves = data['moves']

    for m in moves:
        move(stacks, m['boxes'], m['from'], m['to'])
    
    str = ''
    for s in stacks:
        str += s[-1]
    return str


def part_b(data):
    data = parse(data)
    stacks = data['stacks']
    moves = data['moves']

    for m in moves:
        create_mover_9001(stacks, m['boxes'], m['from'], m['to'])
    
    str = ''
    for s in stacks:
        str += s[-1]
    return str

test_data_part_a = """\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

test_data_part_b = test_data_part_a


if __name__ == "__main__":
    from mysolutions import common
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 'CMZ')
    common.run(part_b, test_data_part_b, data, 'MCD')