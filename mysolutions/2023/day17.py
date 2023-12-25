from heapq import heappush, heappop 
from mysolutions import common

def parse(data):
    data = data.splitlines()

    parsed = []
    for line in data:
        parsed.append(common.all_int(line))

    return parsed

MAX_STRAIGHT = 3

def aoc17(grid):
    seen = set()
    pq = [(0, 0, 0, 0, 0, 0)]

    while pq:
        hl, r, c, dr, dc, n = heappop(pq)
        
        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            print(hl)
            break

        if (r, c, dr, dc, n) in seen:
            continue

        seen.add((r, c, dr, dc, n))
        
        if n < 3 and (dr, dc) != (0, 0):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                heappush(pq, (hl + grid[nr][nc], nr, nc, dr, dc, n + 1))

        for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                nr = r + ndr
                nc = c + ndc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    heappush(pq, (hl + grid[nr][nc], nr, nc, ndr, ndc, 1))


def get_next(path, current, length= MAX_STRAIGHT):
    arrows = []
    n = 0
    pos = current
    if pos in path:
        (curr_row, curr_col, curr_arrow) = pos
        if (curr_row, curr_col) == (0,0): # at the start
            return [(1, 0, "v"), (0, 1, ">")]
        
        while pos and n < length:
            (r, c, arrow) = pos
            arrows.append(arrow)
            pos = path[pos]
            n += 1

        if n == length:
            if arrows.count(">") == n or arrows.count("<") == n: # Moving horizontally
                return [(curr_row-1, curr_col, "^"), (curr_row+1, curr_col, "v")] # Must go up or down
            elif arrows.count("^") == n or arrows.count("v") == n: # Moving vertically
                return [(curr_row, curr_col-1, "<"), (curr_row, curr_col+1, ">")] # Must go left or right
        
        (prev_row, prev_col, prev_arrow) = path[current]

        if curr_arrow == ">": # Moving right -> can go up, down and right
            return [(curr_row-1, curr_col, "^"), (curr_row+1, curr_col, "v"), (curr_row, curr_col+1, ">")]
        elif curr_arrow == "<": # Moving left -> can go up, down and left
            return [(curr_row-1, curr_col, "^"), (curr_row+1, curr_col, "v"), (curr_row, curr_col-1, "<")]
        elif curr_arrow == "v": # Moving down -> can go down, left and right
            return [(curr_row+1, curr_col, "v"), (curr_row, curr_col-1, "<"), (curr_row, curr_col+1, ">")]
        else: # Moving up -> can go up, left and right
            return [(curr_row-1, curr_col, "^"), (curr_row, curr_col-1, "<"), (curr_row, curr_col+1, ">")]
    return []
    
def in_bounds(data, pos):
    (r, c, _) = pos
    return 0 <= r < len(data) and 0 <= c < len(data[0])

def cost(data, pos):
    if in_bounds(data, pos):
        (r, c, _) = pos
        return data[r][c]
    return 0

def neighbors(data, came_from, pos):
    if not in_bounds(data, pos):
        return []
    results = get_next(came_from, pos)
    return results

def dijkstra_search2(data, start, goal, draw=True):
    start =  (start[0], start[1], "o")
    pq = [(0, start)]
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    
    while pq:
        heat_loss, current = heappop(pq)
        (r, c, _) = current 
        if (r, c) == goal:
            break
        
        goto = get_next(came_from, current)
        neighbors = list(filter(lambda n: in_bounds(data, n), goto))
        for next in neighbors:
            new_cost = cost_so_far[current] + cost(data, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                heappush(pq, (new_cost, next))
                came_from[next] = current
    
    min_cost = 0
    end = start
    for arrow in ["<", ">", "^", "v"]:
        g = (goal[0], goal[1], arrow)
        if g in cost_so_far:
            if end == start or min_cost > cost_so_far[g]:
                min_cost = cost_so_far[g]
                end = g

    if draw:
        draw_path(data, came_from, start, end)

    return cost_so_far[end]

    
def dijkstra_search(data, start, goal, draw=True):
    start =  (start[0], start[1], "o")
    pq = [(0, start)]
    came_from = {}
    came_from[start] = None
    seen = set()
    
    while pq:
        heat_loss, current = heappop(pq)
        (r, c, _) = current 
        if (r, c) == goal:
            min_cost = heat_loss
            break
        
        if current in seen:
            continue
        
        seen.add(current)

        goto = get_next(came_from, current)
        neighbors = list(filter(lambda n: in_bounds(data, n), goto))
        for next in neighbors:
            new_heat_loss = heat_loss + cost(data, next)
            heappush(pq, (new_heat_loss, next))
            came_from[next] = current

    if draw:
        draw_path(data, came_from, start, current)

    return cost_so_far[end]

def draw_path(data, path, start, goal):
    d = []
    for r in range(len(data)):
        d.append(list("." * len(data[0])))
    pos = goal
    while pos != start:
        if pos in path:
            (r, c, a) = pos
            next = path[pos]
            d[r][c] = a
            pos = next

    for row in d: 
        print("".join(list(map(str, row))))
            
def part_a(data):
    data = parse(data)
    total = 0
    start = (0, 0)
    goal = (len(data) - 1, len(data[0]) - 1)
    total = dijkstra_search(data, start, goal)
    #aoc17(data)
    
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