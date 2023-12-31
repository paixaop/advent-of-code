import re

def find_first_digit(str):
    for char in str:
        if char.isdigit():
            return int(char)
    return 0
        
def part_a(data):
    data = data.split()
    accumulator = 0
    for line in data:
        num =  find_first_digit(line) * 10
        num += find_first_digit(reversed(line))    
        accumulator += num

    return accumulator


def part_b(data):
    text_numbers = {
        "one"  : "o1e",
        "two"  : "t2o",
        "three": "t3e",
        "four" : "f4r",
        "five" : "f5e",
        "six"  : "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine" : "n9e"
    }
    for key in text_numbers:
        data = data.replace(key, text_numbers[key])

    return part_a(data)


test_data_part_a = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

test_data_part_b = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

if __name__ == "__main__":
    from mysolutions import common
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 142)
    common.run(part_b, test_data_part_b, data, 281)
    