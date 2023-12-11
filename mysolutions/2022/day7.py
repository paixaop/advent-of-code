import re
from mysolutions import common
"""
/
/a DIR
/a/e DIR
/a/e/i FILE 584
/a/f FILE 29116
/a/g FILE 
/a/h.lst FILE
"""
def parse(data):
    data = data.split("\n")

    file_system = { "/": {} }
    dir_level = 0
    cur_dir = ['/']

    for line in data:
        match = re.search(r"\$ cd (.+))")
        if match is not None:
            cd_arg = match.group(1)
            cur_dir.append(cd_arg) 

        match = re.search(r"\$ ls")
        if match is not None:
            ls_Arg = match.group(1)

        match = re.search(r"dir (\w+))")
        if match is not None:
            dir_name = match.group(1)

        match = re.search(r"(\d+) (.+)")
        if match is not None:
            dir_name = match.group(1)
            file_name = match.group(2)

    return {}

def part_a(data):
    data = parse(data)
    total = 0
    
    return total


def part_b(data):
    data = parse(data)
    total = 0

    return total

test_data_part_a = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

test_data_part_b = test_data_part_a


if __name__ == "__main__":
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 0)
    common.run(part_b, test_data_part_b, data, 0)