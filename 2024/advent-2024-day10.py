def run(part: int, test_suffix: str = "", debug: bool = False):  # pylint: disable=duplicate-code
    y, d = __file__.split("advent-")[1].split("-day")
    file_name = f"{y}/input/{d.strip('.py')}{test_suffix}.txt"

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def part1(data: list[str], debug: bool = False) -> int:
    results = 0
    show(data, debug=debug)

    for y, row in enumerate(data):
        for x, value in enumerate(row):
            if value == "0":
                result = len(get_trail_ends(data, int(x), int(y), 0, debug))
                if debug:
                    print(f"({x},{y}: {result})")
                results += result

    return results


def get_trail_ends(
    grid: list[str], x: int, y: int, step: int, debug: bool = False
) -> set[tuple[int, int]]:
    results = set()
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    for direction in directions:
        new_x, new_y = direction[0] + x, direction[1] + y
        if is_inbounds(grid, (new_x, new_y)):
            if grid[new_y][new_x] == str(step + 1):
                if grid[new_y][new_x] == "9":
                    # if debug: print("Adding", (x, y))
                    results.add((new_x, new_y))
                else:
                    results.update(get_trail_ends(grid, new_x, new_y, step + 1, debug))

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    show(data, debug=debug)

    for y, row in enumerate(data):
        for x, value in enumerate(row):
            if value == "0":
                result = get_trail_count(data, int(x), int(y), 0, debug)
                if debug:
                    print(f"({x},{y}: {result})")
                results += result

    return results


def get_trail_count(grid: list[str], x: int, y: int, step: int, debug: bool = False) -> int:
    results = 0
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    for direction in directions:
        new_x, new_y = direction[0] + x, direction[1] + y
        if is_inbounds(grid, (new_x, new_y)):
            if grid[new_y][new_x] == str(step + 1):
                if grid[new_y][new_x] == "9":
                    # if debug: print("Adding", (x, y))
                    results += 1
                else:
                    results += get_trail_count(grid, new_x, new_y, step + 1, debug)

    return results


def show(grid: list[str], debug: bool = False) -> None:
    if debug:
        print()
        for y, row in enumerate(grid):
            print(y, "".join([str(x) for x in row]))


def is_inbounds(data: list[str], node: tuple[int, int]) -> bool:
    return 0 <= node[0] < len(data[0]) and 0 <= node[1] < len(data)


if __name__ == "__main__":
    # print("Test1a: ", run(part=1, test_suffix="-test1a", debug=True))  # 2
    # print("Test1b: ", run(part=1, test_suffix="-test1b", debug=True))  # 4
    # print("Test1c: ", run(part=1, test_suffix="-test1c", debug=True))  # 3
    # print("Test1d: ", run(part=1, test_suffix="-test1d", debug=True))  # 5
    # print("Test1e: ", run(part=1, test_suffix="-test-e", debug=True))  # 36
    # print("Real1: ", run(part=1, debug=False))  # 674
    # print("Test2a: ", run(part=2, test_suffix="-test2a", debug=True))  # 3
    # print("Test2b: ", run(part=2, test_suffix="-test2b", debug=True))  # 13
    # print("Test2c: ", run(part=2, test_suffix="-test2c", debug=True))  # 227
    # print("Test2e: ", run(part=2, test_suffix="-test-e", debug=True))  # 81
    print("Real2: ", run(part=2, debug=False))  # 1372
