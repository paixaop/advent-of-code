from heapq import heappush, heappop 
from mysolutions import common

def parse(data):
    data = data.splitlines()

    parsed = []
    for line in data:
        parsed.append(common.all_int(line))

    return parsed

MAX_STRAIGHT = 3

def get_next(path, current, length= MAX_STRAIGHT):
    rows = set()
    cols = set()
    n = 0
    pos = current
    if pos in path:
        if pos == (0,0): # at the start
            return [(1, 0), (0, 1)]
        
        (curr_row, curr_col) = pos
        while pos and n < length:
            (r, c) = pos
            rows.add(r)
            cols.add(c)
            pos = path[pos]
            n += 1
        if n == length:
            if len(rows) == 1: # Moving horizontally
                return [(curr_row-1, curr_col), (curr_row+1, curr_col)] # Must go up or down
            elif len(cols) == 1: # Moving vertically
                return [(curr_row, curr_col-1), (curr_row, curr_col+1)] # Must go left or right
        
        (prev_row, prev_col) = path[current]

        if prev_row == curr_row: # Moving horizontally
            if prev_col < curr_col: # Moving right -> can go up, down and right
                return [(curr_row-1, curr_col), (curr_row+1, curr_col), (curr_row, curr_col+1)]
            else: # Moving left -> can go up, down and left
                return [(curr_row-1, curr_col), (curr_row+1, curr_col), (curr_row, curr_col-1)]
        elif prev_col == curr_col: # Moving vertically
            if prev_row < curr_row: # Moving down -> can go down, left and right
                return [(curr_row+1, curr_col), (curr_row, curr_col-1), (curr_row, curr_col+1)]
            else: # Moving up -> can go up, left and right
                return [(curr_row-1, curr_col), (curr_row+1, curr_col), (curr_row, curr_col-1)]
    return []
    
def in_bounds(data, pos):
    (r, c) = pos
    return 0 <= r < len(data) and 0 <= c < len(data[0])

def cost(data, pos):
    if in_bounds(data, pos):
        (r, c) = pos
        return data[r][c]
    return 0

def neighbors(data, came_from, pos):
    if not in_bounds(data, pos):
        return []
    neighbors = get_next(came_from, pos)
    results = filter(lambda n: in_bounds(data, n), neighbors)
    return list(results)

    
def dijkstra_search(data, start, goal, draw=True):
    pq = [(0, start)]
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while pq:
        _, current = heappop(pq)       
        if current == goal:
            break
        
        goto = neighbors(data, came_from, current)
        for next in goto:
            new_cost = cost_so_far[current] + cost(data, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                heappush(pq, (new_cost, next))
                came_from[next] = current
    
    if draw:
        draw_path(data, came_from, start, goal)

    return cost_so_far[goal]

def draw_path(data, path, start, goal):
    d = []
    for r in range(len(data)):
        d.append(list("." * len(data[0])))
    pos = goal
    while pos != start:
        if pos in path:
            (r, c) = pos
            next = path[pos]
            (rn, cn) = next
            if r == rn:
                if c > cn:
                    d[r][c]='>'
                else:
                    d[r][c]='<'
            elif c == cn:
                if r > rn:
                    d[r][c]='v'
                else:
                    d[r][c]='^'
            #d[r][c] = "#"
            pos = next

    for row in d: 
        print("".join(list(map(str, row))))
            
def part_a(data):
    data = parse(data)
    total = 0
    start = (0, 0)
    goal = (len(data) - 1, len(data[0]) - 1)
    total = dijkstra_search(data, start, goal)
    
    return total


def part_b(data):
    data = parse(data)
    total = 0

    return total

test_data_part_a = """\
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""

test_data_part_b = test_data_part_a


if __name__ == "__main__":
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 102)
    common.run(part_b, test_data_part_b, data, 0)