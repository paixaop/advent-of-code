import re
from functools import reduce
import math

def part_a(data):
    data = data.split('\n')
    total = 0
    times = list(map(int,data[0][5:].split()))
    distance = list(map(int,data[1][9:].split()))

    # iterate races
    good_races = []
    for race in range(len(times)):
        new_records = 0
        
        for button_time in range(times[race]):
            travel_time = times[race] - button_time
            travel_distance = travel_time * button_time
            if travel_distance > distance[race]:
                new_records += 1

        good_races.append(new_records)

    return reduce(lambda x, y: x * y, good_races)


def part_b(data):
    data = data.split('\n')
    total = 0
    time = int(data[0][5:].replace(" ", ""))
    distance = int(data[1][9:].replace(" ", ""))

    # iterate races
    good_races = []
    s1 = int((time + math.sqrt(pow(time, 2) - 4 * distance))/2)
    s2 = int((time - math.sqrt(pow(time, 2) - 4 * distance))/2)

    return s1 - s2

def part_b_brute_force(data):
    data = data.split('\n')
    total = 0
    times = int(data[0][5:].replace(" ", ""))
    distance = int(data[1][9:].replace(" ", ""))

    # iterate races
    good_races = []
    new_records = 0    
    for button_time in range(times):
        travel_time = times - button_time
        travel_distance = travel_time * button_time
        if travel_distance > distance:
            new_records += 1

    good_races.append(new_records)

    return reduce(lambda x, y: x * y, good_races)

test_data_part_a = """\
Time:      7  15   30
Distance:  9  40  200"""

test_data_part_b = test_data_part_a



if __name__ == "__main__":
    from mysolutions import common
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 288)
    common.run(part_b, test_data_part_b, data, 71503)
    #common.run(part_b_brute_force, test_data_part_b, data, 71503)