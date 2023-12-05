import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def bold(s):
    return bcolors.BOLD + str(s) + bcolors.ENDC

def yellow(s):
    return bcolors.WARNING + str(s) + bcolors.ENDC

def green(s):
    return bcolors.OKGREEN + str(s) + bcolors.ENDC


def get_data(file):    
    match = re.search(r'(\d{4}).day(\d+)\.py$', file)
    if match is None: 
        raise Exception('bad folder structure')
    
    day = int(match.group(2))
    year = int(match.group(1))
    print(f"\n\nSolutions for {bcolors.BOLD}{year}/{day}{bcolors.ENDC}\n")

    try:
        from aocd import get_data
        data = get_data(day=day, year=year)
    except Exception as e:
        print("Error: {}\n".format(e))
        exit()

    return data

def run(func, test_data, data, value):
    assert func(test_data) == value
    print(f"Test of Part A: {green("PASSED")}")
    print(f"Part A Solution: {yellow(func(data))}\n")