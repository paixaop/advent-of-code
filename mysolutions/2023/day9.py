import re
from mysolutions import common


def process(data):
    j = 0
    history = [ data ]
    while True:
        delta = [b - a for a, b in zip(history[j], history[j][1:])]
        history.append(delta)
        j += 1

        if all(val == 0 for val in delta):
            history[j].append(0)

            for i in range(j, 0, -1):
                history[i-1].append(history[i-1][-1] + history[i][-1])

            return history[0][-1] 



def part_a(data):
    data = data.split("\n")
    
    total = 0
    for line in data:
        history = common.all_int(line.split())
      
        total += process(history)

    return total


def part_b(data):
    data = data.split("\n")

    total = 0
    for line in data:
        history = common.all_int(line.split())[::-1]
      
        total += process(history)  
    

    return total

test_data_part_a = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

test_data_part_b = test_data_part_a


if __name__ == "__main__":
    from mysolutions import common
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 114)
    common.run(part_b, test_data_part_b, data, 2)