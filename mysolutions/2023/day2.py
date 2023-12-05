import re

possible_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def get_games(str):
    result = re.search(r"Game (\d+)", str)
    if result is None:
        return None, None

    game_id = int(result.group(1))
    games = str[str.find(':')+2::].split(';')
    return game_id, games

def part_a(data):
    data = data.split("\n")
    pattern = re.compile(r"(\d+) (\w+)")

    valid_game_sum = 0
    valid_game = False
    for line in data:
        game_id, games = get_games(line)
        if game_id is None:
            break

        for g in games:
            valid_game = True

            for match in pattern.finditer(g):
                count = int(match.group(1))
                cube = match.group(2)
                if count > possible_cubes[cube]:
                    valid_game = False
                    break

            if valid_game is False:
                break

        if valid_game:
            valid_game_sum += game_id

    return valid_game_sum

def part_b(data):
    data = data.split("\n")
    pattern = re.compile(r"(\d+) (\w+)")

    power_game_sum = 0
    for line in data:
        game_id, games = get_games(line)
        if game_id is None:
            break

        min_number_of_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for g in games:
            for match in pattern.finditer(g):
                count = int(match.group(1))
                cube = match.group(2)
                if min_number_of_cubes[cube] < count:
                    min_number_of_cubes[cube] = count

        game_power = min_number_of_cubes['red'] * min_number_of_cubes['green'] * min_number_of_cubes['blue'] 
        power_game_sum += game_power

    return power_game_sum

test_data_part_a = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

test_data_part_b = test_data_part_a


if __name__ == "__main__":
    from mysolutions import common
    data = common.get_data(__file__)

    common.run(part_a, test_data_part_a, data, 8)
    common.run(part_b, test_data_part_b, data, 2286)
    