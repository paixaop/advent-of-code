import re

def part_a(data):
    data = data.split("\n")
    
    total = 0
    # for line in data:

    return total


def part_b(data):
    data = data.split("\n")

    total = 0
    # for line in data:

    return total

test_data_part_a = """\
"""

test_data_part_b = test_data_part_a

def test_a():
    assert part_a(test_data_part_a) == 4361
    print("Test of Part A: PASSED")

def test_b():
    assert part_b(test_data_part_b) == 467835
    print("Test of Part B: PASSED")


if __name__ == "__main__":
    day = 4
    year = 2023
    print("\n\nSolutions for {}/{}\n".format(year, day))

    try:
        from aocd import get_data
        data = get_data(day=day, year=year)
    except Exception as e:
        print("Error: {}\n".format(e))
        exit()
    
    test_a()
    print("Part A: {}\n".format(part_a(data)))

    test_b()
    print("Part B: {}\n".format(part_b(data)))
