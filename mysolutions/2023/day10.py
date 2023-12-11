import re
from mysolutions import common

"""
The pipes are arranged in a two-dimensional grid of tiles:

    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, but your 
      sketch doesn't show what shape the pipe has.
"""

possible_connections = {
    # [ TOP, RIGHT, BOTTOM, LEFT]
    '|' : [['|', 'F', '7'], [], ['|', 'L', 'J'], []],
    '-' : [[], ['-', 'J', '7'], [], ['-', 'F', 'L']],
    'L' : [['|', '7', 'F'], ['-', 'J', '7'], [], []],
    'J' : [['|', '7', 'F'], [], [], ['-', 'F', 'L']],
    '7' : [[], [], ['|', 'J', 'L'], ['-', 'F', 'L']],
    'F' : [[], ['-', 'J', '7'], ['|', 'L', 'J'], []],
}

def find_start(data, char = 'S'):
    for y, line in enumerate(data):
        if char in line:
            x = line.index(char)
            return x, y
    return None

def get_char(data, x, y):
    if 0 <= y < len(data):
        if 0 <= x < len(data[y]): 
            return data[y][x]
    return None

def can_connect(data, x, y, char = ''):
    current = char
    if char == '':
        current = get_char(data, x, y)

    if current is None:
        return None
    
    allowed_connections = possible_connections[current]
    
    if y == 0 and (current in ['|', 'L', 'J']):
        return None
    
    if y == len(data) and (current in ['|', 'F', '7']):
        return None
    
    if x == 0 and (current in ['-', '7', 'J']):
        return None
    
    if x == len(data[y]) and (current in ['-', 'F', 'L']):
        return None

    connections = []
    for i, allowed in enumerate(allowed_connections):
        # i == 0 Above, i == 1 Right, i == 2 Bellow, i == 3 Left
        y1 = y
        x1 = x
        if i == 0 or i == 2:
            y1 = y + (i - 1)
        if i == 1:
            x1 = x + 1
        if i == 3:
            x1 = x - 1

        other_char = get_char(data, x1, y1)
        if other_char in allowed:
            connections.append([x1, y1])
        
    return connections

def connections_start(data, x, y):
    possible = []
    for char in possible_connections.keys():
        connections = can_connect(data, x, y, char)
        if connections is not None:
            if len(connections) == 2:
                possible.append({ "start": char, "connections": connections, "dist": 0 })

    return possible

def loop_coords(data, start_x, start_y):
    x = start_x
    y = start_y
    visited = []
    while True:
        c = can_connect(data, x, y)
        if c is not None:
            if len(c) == 2:
                visited.append([ x, y])
                if c[0] not in visited:    
                    x = c[0][0]
                    y = c[0][1]
                elif c[1] not in visited:
                    x = c[1][0]
                    y = c[1][1]
                else:
                    break
            else:
                raise ValueError(f"{get_char(x, y)} at [{x},{y}] has more than 2 connections")
        
        if x == start_x and y == start_y:
            visited.append([ start_x, start_y])
            return visited
    
    visited.append([ start_x, start_y])
    return visited

def cn_PnPoly(P, V): # P - Point; V - Polygon
  n = len(V)-1
  cn = 0    # the  crossing number counter

  # loop through all edges of the polygon
  i = 0
  # while i<n: # edge from V[i]  to V[i+1]
  for i in range(n):
    # upward crossing or downward crossing
    if (V[i][1] <= P[1] and V[i+1][1] > P[1]) or (V[i][1] > P[1] and V[i+1][1] <= P[1]): 
      # compute  the actual edge-ray intersect x-coordinate
      vt = (P[1]  - V[i][1]) / (V[i+1][1] - V[i][1])
      # if P[0] > (V[i][0] + vt * (V[i+1][0] - V[i][0])): # P.x > intersect - ray toward left
      if P[0] < (V[i][0] + vt * (V[i+1][0] - V[i][0])): # P.x < intersect - ray toward right - original
        cn += 1   # a valid crossing of y=P[1] right of P.x

  #print str(cn)
  return (cn&1)    # 0 if even (out), and 1 if  odd (in)


def part_a(data):
    data = list(map(lambda l: list(l), data.split("\n")))

    x_S, y_S = find_start(data)
    possible = connections_start(data, x_S, y_S)
    data[y_S][x_S] = possible[0]['start']

    loop = loop_coords(data, x_S, y_S)
    return int(len(loop)/2)

    

def part_b(data):
    data = list(map(lambda l: list(l), data.split("\n")))

    x_S, y_S = find_start(data)
    possible = connections_start(data, x_S, y_S)
    data[y_S][x_S] = possible[0]['start']
    count = 0
    loop = loop_length(data, x_S, y_S)
    for y, l in enumerate(data):
        for x, c in enumerate(l):
            p = [x, y] 
            if p not in loop:
                if cn_PnPoly(p, loop) == 0:
                    data[y][x] = 'O'
                else:
                    data[y][x] = 'I'
                    count += 1

    return count

test_data_part_a = """\
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

test_data_part_b = """\
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""


if __name__ == "__main__":
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 8)
    common.run(part_b, test_data_part_b, data, 10)