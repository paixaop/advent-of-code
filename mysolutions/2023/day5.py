import re
import portion as P

def parse(data):
    blocks = data.split('\n\n')
    parsed_data = dict()
    
    parsed_data["maps"] = [] 
    for block in blocks:
        match = re.search(r"seeds: ([\d\s]+)", block)
        if match is not None:
            parsed_data['seeds'] = list(map(int, match.group(1).split()))
        
        match = re.search(r"([\w-]+) map:\n(.*)", block, re.S)
        if match is not None:
            sdmap = match.group(1)
            ranges = match.group(2).split('\n')
            maps = []
            for r in ranges:
                destination, source, size =  map(int, r.split())
                maps.append({
                    "start":source, 
                    "finish": source + size, 
                    "add": destination - source
                })
            parsed_data["maps"].append(maps)
    
    return parsed_data

def get_map(mapping, k):
    for m in mapping:
        if m['start'] <= k < m['finish']:
            return  k + m['add']
    return k

def part_a(data):
    parsed_data = parse(data)
    
    total = 0
    locations = 99999999999999999999999999999999
    for seed in parsed_data['seeds']:
        mapping = seed
        for maps in parsed_data['maps']:
            mapping = get_map(maps, mapping)
        if mapping < locations:
            locations = mapping

    return locations

all_ranges = []


# Thank you to [Wayoshi](https://www.reddit.com/user/Wayoshi/) for a brilliant solution
# Without his help I was trying to iterate all values not realizing that 
# the input dataset had millions to test...
# Next time look at the input!
def check_ranges(maps, p, rule):
    if rule == 7:
        # We applied all 7 mappins save the last one which is the location
        all_ranges.append(p)
        return 
        
    # Check/apply mapping rules
    # Using the intervals so we can check and apply rules without iterating the values
    for m in maps[rule]:
        # Calculate the source range of the rule
        p2 = P.closedopen(m['start'], m['finish'])

        # Intersect both ranges to see if the passed values in argument p 
        # are included in range p2?
        intersection = p & p2

        # if intersection is empty then no mapping is needed and 
        # argument p is left unchanged as per the problem instructions
        if intersection.empty != True:

            # Intersection is not empty we have to map the source values 
            # to the destination using range 'add'
            check_ranges(maps, 
                P.closedopen(
                    intersection.lower + m['add'], 
                    intersection.upper + m['add']), 
                rule + 1)

            # Now check the values that were not in this range 
            # but could be in another or will be left unchanged
            # for the next rule
            p -= p2

            if p.empty:
                # we've processed all numbers in p
                break
    if p:
        # No mappings were done on this range, just pass it 
        # to the next mapping rule
        check_ranges(maps, p, rule + 1)
    

def part_b(data):
    parsed_data = parse(data)
    global all_ranges

    all_ranges = []
    for i in range(0, len(parsed_data['seeds']), 2):
        start, size = parsed_data['seeds'][i:i+2]
        
        seed = P.closedopen(start, start + size)
        check_ranges(parsed_data['maps'], seed, 0)
    
    locations = list(map(lambda r: r.lower, all_ranges))
    return min(locations)

test_data_part_a = """\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

test_data_part_b = test_data_part_a



if __name__ == "__main__":
    from mysolutions import common
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 35)
    common.run(part_b, test_data_part_b, data, 46)