from mysolutions import common
cache = {}
def count(cfg, nums):
    if cfg == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in cfg else 1

    key = (cfg, nums)
    if key in cache:
        return cache[key]
    
    result = 0
    
    if cfg[0] in ".?":
        result += count(cfg[1:], nums)
        
    if cfg[0] in "#?":
        if nums[0] <= len(cfg) and \
           "." not in cfg[:nums[0]] and \
           (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
            result += count(cfg[nums[0] + 1:], nums[1:])

    cache[key] = result
    return result

def part_a(data):
    data = data.splitlines()

    total = 0
    for line in data:
        cfg, nums = line.split()
        nums = tuple(map(int, nums.split(",")))
        total += count(cfg, nums)
    
    return total

def part_b(data):
    data = data.splitlines()

    total = 0
    for line in data:
        cfg, nums = line.split()
        nums = tuple(map(int, nums.split(",")))
        cfg = "?".join([cfg] * 5)
        nums *= 5
        
        total += count(cfg, nums)
    
    return total
test_data_part_a = """\
.??..??...?##. 1,1,3
???.### 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

test_data_part_b = test_data_part_a

if __name__ == "__main__":
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 21)
    common.run(part_b, test_data_part_b, data, 525152)