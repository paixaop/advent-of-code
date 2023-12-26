from mysolutions import common
import re
DIRECTIONS = {
    "U": (-1,  0),
    "D": ( 1,  0),
    "L": ( 0, -1),
    "R": ( 0,  1)
}

def parse(data):
    data = data.splitlines()

    parsed = []
    pattern = re.compile(r"(\w) (\d+) \((#[0-9a-fA-F]+)\)")
    for line in data:
        m = re.findall(pattern, line)
        if m:
            m = m[0]
            parsed.append({
                "dir" : m[0],
                "length": int(m[1]),
                "color": m[2]
            })
        
    return parsed

# e.g. corners = [(2.0, 1.0), (4.0, 5.0), (7.0, 8.0)]
def area(corners):
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return int(area)

def area2(vertices):
    n = len(vertices) # of corners
    a = 0.0
    for i in range(n):
        j = (i + 1) % n
        a += abs(vertices[i][0] * vertices[j][1]-vertices[j][0] * vertices[i][1])
    result = a / 2.0
    return result

def shoelace_area(vertices):
    n = len(vertices)
    a1,a2 = 0,0
    for j in range(n-1):
        a1 += vertices[j][0] * vertices[j+1][1]
        a2 += vertices[j][1] * vertices[j+1][0]
    l=abs(a1-a2)/2
    return l

def part_a(data):
    data = parse(data)
    total = 0
    r = 0
    c = 0
    polygon = [(0, 0)]
    trench_lengh = 0
    for dig in data:
        dr, dc = DIRECTIONS[dig["dir"]]
        r += dig["length"] * dr
        c += dig["length"] * dc
        trench_lengh += dig["length"]
        polygon.append((r, c))

    area = int(shoelace_area(polygon)) + trench_lengh // 2 + 1
    
    return area


def part_b(data):
    data = parse(data)
    total = 0

    return total

test_data_part_a = """\
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

test_data_part_b = test_data_part_a


if __name__ == "__main__":
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 62)
    common.run(part_b, test_data_part_b, data, 0)