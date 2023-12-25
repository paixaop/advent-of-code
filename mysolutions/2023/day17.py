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



def in_bounds(data, pos):
    (r, c) = pos
    return 0 <= r < len(data) and 0 <= c < len(data[0])

def dijkstra_search(data, start, goal, draw=True):
    if not in_bounds(data, start) or not in_bounds(data, goal):
        return -1
    
    pq = [(0, (start[0], start[1], 0, 0, 0))]
    
    came_from = {}
    came_from[start] = None
    seen = set()
    
    while pq:
        heat_loss, current = heappop(pq)
        (row, col, dr, dc, n) = current
        
        if not in_bounds(data, (row, col)):
            continue
        
        if (row, col) == goal:
            return heat_loss
        
        if current in seen:
            continue
        
        seen.add(current)
        if n < MAX_STRAIGHT and (dr,dc) != (0, 0):
            next_row = row + dr
            next_col = col + dc
            next = (next_row, next_col, dr, dc, n + 1)
            
            if in_bounds(data, (next_row, next_col)):
                next_heat_loss = heat_loss + data[next_row][next_col]
                heappush(pq, (next_heat_loss, next))
            

        neighbors = [(-1, 0), (1 , 0), (0, -1), (0, 1)]
        for ndr, ndc in neighbors:
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                next_row = row + ndr
                next_col = col + ndc
                next = (next_row, next_col, ndr, ndc, 1)
                if in_bounds(data, (next_row, next_col)):
                    next_heat_loss = heat_loss + data[next_row][next_col]
                    heappush(pq, (next_heat_loss, next))
            
    return -1
         
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
    common.run(part_b, test_data_part_b, data, 94)