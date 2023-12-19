from functools import cache
from mysolutions import common
import re

permutations_global = {}

def check_groups(str, groups):
    if str.count('?') > 0:
        return False

    pattern = re.compile(r"(#+)");
    match = pattern.findall(str)
    if match is not None:
        grps = tuple(map(len, match))
        return grps == groups
    return False

def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]

# ???.### 1,1,3
# ??#??#?????#.??????? 9,1,2,3
@cache
def permutation(report, group_sizes, i=0):
    if check_groups(report, group_sizes):
        return 1
    
    if report.count('?') == 0:
        return 0
    
    result = 0
    if report[i] == '?':

        report = replacer(report, '.', i)    
        p = permutation(report, group_sizes, i= i + 1)
        result += p

        report = replacer(report, '#', i)
        p = permutation(report, group_sizes, i= i + 1)
        result += p

    else:
        p = permutation(report, group_sizes, i= i + 1)
        result += p
    return result


def part_a(data):
    data = data.splitlines()

    total = 0
    for line in data:
        damage_records, grp = line.split(" ")
        damage_groups = tuple(common.all_int(grp.split(',')))
        total += permutation(damage_records, damage_groups)
        
    return total


def part_b(data):
    data = data.splitlines()

    total = 0
    for line in data:
        damage_records, grp = line.split(" ")
        damage_groups = common.all_int(grp.split(','))
        total += permutation(damage_records, damage_groups)

    return total

test_data_part_a = """\
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

test_data_part_b = test_data_part_a

if __name__ == "__main__":
    data = common.get_data("/2023/day12.py")

    common.run(part_a, test_data_part_a, data, 21)
    #common.run(part_b, test_data_part_b, data, 525152)