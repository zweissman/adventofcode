from copy import deepcopy

FILE_NAME = "2024/input/06.txt"


def run(part: int, test_run: bool = False, debug: bool = False) -> int:
    if test_run:
        file = FILE_NAME.replace(".txt", "-test.txt")
    else:
        file = FILE_NAME

    with open(file, encoding="utf-8") as f:
        data_raw = f.readlines()

    data = [list(x.strip()) for x in data_raw]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def show(grid: list[list[str]], debug: bool = False) -> None:
    if debug:
        print()
        for y, row in enumerate(grid):
            print(y, "".join([str(x) for x in row]))


def part1(data: list[list[str]], debug: bool = False) -> int:
    results = 1
    x, y = find_start(data, debug)

    d = data[y][x]

    return results + move(data, x, y, d, debug)


def move(data: list[list[str]], x: int, y: int, d: str, debug: bool) -> int:
    results = 0
    iterations = 0

    dx, dy = get_dir(d)

    data[y][x] = "X"

    while True:
        if iterations > 200:
            return -1

        if debug:
            print(results, d, x, y)
        show(data, debug)
        new_x = x + dx
        new_y = y + dy

        if new_x < 0 or new_x >= len(data[0]) or new_y < 0 or new_y >= len(data):
            return results

        if data[new_y][new_x] == "#":
            d = get_next_dir(d)
            dx, dy = get_dir(d)

        else:
            x = new_x
            y = new_y

            if data[y][x] == ".":
                results += 1

            if data[y][x] != "X":
                data[y][x] = "X"
                iterations = 0

            else:
                iterations += 1


def get_dir(d: str) -> tuple[int, int]:
    if d == "^":
        return 0, -1
    if d == "V":
        return 0, 1
    if d == "<":
        return -1, 0
    if d == ">":
        return 1, 0

    return 0, 0


def get_next_dir(d: str) -> str:
    if d == "^":
        return ">"
    if d == "V":
        return "<"
    if d == "<":
        return "^"
    if d == ">":
        return "V"

    return ""


def part2(data: list[list[str]], debug: bool = False) -> int:
    results = 0
    start_x, start_y = find_start(data, debug)

    start_data = deepcopy(data)
    start_dir = data[start_y][start_x]

    move(data, start_x, start_y, start_dir, debug)

    for y, row in enumerate(data):
        print(y, results)
        for x, _ in enumerate(row):
            if x == start_x and y == start_y:
                continue

            if data[y][x] == "X":
                new_data = deepcopy(start_data)
                new_data[y][x] = "#"

                test_results = part1(new_data, debug=False)

                if test_results == 0:
                    results += 1
                    if debug:
                        print(results, f"Found loop with obstacle at ({x},{y})")

    return results


def find_start(grid: list[list[str]], debug: bool) -> tuple[int, int]:
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if value in ("<>^V"):
                if debug:
                    print(f"Found start at ({x},{y})")

                return (x, y)

    return (-1, -1)


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # 41
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 4663
    # print("Test2: ", run(part=2, test_run=True, debug=True))  # 6
    print("Real2: ", run(part=2, test_run=False, debug=False))  # 1530
