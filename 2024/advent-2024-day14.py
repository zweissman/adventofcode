from ast import literal_eval


def run(part: int, test_suffix: str = "", debug: bool = False):
    y, d = __file__.split("advent-")[1].split("-day")
    file_name = f"{y}/input/{d.strip('.py')}{test_suffix}.txt"

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()
    if test_suffix != "":
        width = 11
        height = 7
    else:
        width = 101
        height = 103

    data = [x.strip() for x in file_data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, width=width, height=height, debug=debug)


def part1(data: list[str], width: int, height: int, debug: bool = False) -> int:
    SECONDS = 100
    grid = [[0] * width for _ in range(height)]
    show(grid, debug)

    for d in data:
        if debug:
            print(d)
        p_str, v_str = d.split()
        p_str = p_str.replace("p=", "")
        v_str = v_str.replace("v=", "")
        p = literal_eval(p_str)
        v = literal_eval(v_str)

        if debug:
            print(p, v)

        x = (p[0] + v[0] * SECONDS) % width
        y = (p[1] + v[1] * SECONDS) % height

        if debug:
            print(x, y)
            print()

        grid[y][x] += 1

    show(grid, debug)

    q1 = 0
    for y in range(0, (len(grid) - 1) // 2):
        q1 += sum([int(x) for x in grid[y][: (len(grid[y]) - 1) // 2]])  # pylint: disable=consider-using-generator

    q2 = 0
    for y in range(0, (len(grid) - 1) // 2):
        q2 += sum([int(x) for x in grid[y][(len(grid[y]) - 1) // 2 + 1 :]])  # pylint: disable=consider-using-generator

    q3 = 0
    for y in range((len(grid) - 1) // 2 + 1, len(grid)):
        q3 += sum([int(x) for x in grid[y][: (len(grid[y]) - 1) // 2]])  # pylint: disable=consider-using-generator

    q4 = 0
    for y in range((len(grid) - 1) // 2 + 1, len(grid)):
        q4 += sum([int(x) for x in grid[y][(len(grid[y]) - 1) // 2 + 1 :]])  # pylint: disable=consider-using-generator

    return q1 * q2 * q3 * q4


def part2(data: list[str], width: int, height: int, debug: bool = False) -> int:
    robots = []

    for d in data:
        p_str, v_str = d.split()
        p_str = p_str.replace("p=", "")
        v_str = v_str.replace("v=", "")
        p = literal_eval(p_str)
        v = literal_eval(v_str)

        robots.append((p, v))

    for seconds in range(1, 10000000):
        grid = [["."] * width for _ in range(height)]

        for p, v in robots:
            x = (p[0] + v[0] * seconds) % width
            y = (p[1] + v[1] * seconds) % height

            grid[y][x] = "X"

        for y, row in enumerate(grid):
            if "XXXXXXXXXXX" in "".join(row):
                show(grid, seconds, debug)
                return seconds
    return 0


def show(grid: list[list], seconds: int, debug: bool = False) -> None:
    if debug:
        print()
        print(seconds)
        for y, row in enumerate(grid):
            print(y, "".join([str(x) if x != 0 else "." for x in row]))


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 12
    # print("Real1: ", run(part=1, debug=False))  # 211692000
    print("Real2: ", run(part=2, debug=True))  # 6587
