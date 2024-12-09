FILE_NAME = "2023/input/02.txt"


def run(part: int, test_run: bool = False, debug: bool = False):
    if test_run:
        file = FILE_NAME.replace(".txt", "-test.txt")
    else:
        file = FILE_NAME

    with open(file, encoding="utf-8") as f:
        file_data = f.readlines()

    data = [x.strip() for x in file_data]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def part1(data: list[str], debug: bool = False) -> int:
    results = 0

    RED = 12
    GREEN = 13
    BLUE = 14

    for line in data:
        if debug:
            print(line)
        game_id_str, games = line.split(":")
        game_id = int(game_id_str.replace("Game ", ""))
        game_list = games.split(";")

        valid_game = True
        for game in game_list:
            red, blue, green = 0, 0, 0
            cube_list = game.strip().split(",")

            for cube in cube_list:
                if "red" in cube:
                    cube = cube.replace("red", "")
                    red = int(cube.strip())
                elif "blue" in cube:
                    cube = cube.replace("blue", "")
                    blue = int(cube.strip())
                elif "green" in cube:
                    cube = cube.replace("green", "")
                    green = int(cube.strip())

            if debug:
                print(red, blue, green)
            if red > RED or green > GREEN or blue > BLUE:
                valid_game = False
                if debug:
                    print(f"{game_id} Invalid game")
                break
        if not valid_game:
            continue

        if debug:
            print(f"{game_id} Valid game")
        results += game_id

    return results


def part2(data: list[str], debug: bool = False) -> int:  # pylint: disable=duplicate-code
    results = 0

    for line in data:
        line = line.strip()
        if debug:
            print(line)
        game_id_str, games = line.split(":")
        game_id = int(game_id_str.replace("Game ", ""))
        if debug:
            print(f"{game_id=}")
        game_list = games.split(";")

        red, blue, green = 0, 0, 0
        for game in game_list:
            cube_list = game.strip().split(",")

            for cube in cube_list:
                if "red" in cube:
                    cube = cube.replace("red", "")
                    red = max(red, int(cube.strip()))
                elif "blue" in cube:
                    cube = cube.replace("blue", "")
                    blue = max(blue, int(cube.strip()))
                elif "green" in cube:
                    cube = cube.replace("green", "")
                    green = max(green, int(cube.strip()))

            if debug:
                print(red, blue, green)

        results += red * blue * green

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # 8
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 2551
    print("Test2: ", run(part=2, test_run=True, debug=True))  # 2286
    # print("Real2: ", run(part=2, test_run=False, debug=False))  # 62811
