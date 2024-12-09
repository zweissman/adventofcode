from typing import Optional


def run(part: int, test_suffix: str = "", debug: bool = False):  # pylint: disable=duplicate-code
    file_name = "2023/input/10.txt"
    if test_suffix:
        file_name = file_name.replace(".txt", test_suffix + ".txt")

    with open(file_name, encoding="utf-8") as file:
        data = file.readlines()

    data = [x.strip() for x in data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def part1(data: list[str], debug: bool = False) -> int:
    results = 0

    grid = []

    for d in data:
        grid.append(list(d.strip()))

    if debug:
        print(grid)

    connections = []
    start = None
    visited = set()

    for y, row in enumerate(grid):
        if start:
            break
        for x, c in enumerate(row):
            if c == "S":
                connection = get_connections(grid, x, y, debug)
                connections.append(connection)
                assert connection
                start = connection[0]
                visited.add((x, y))

                # figure out what char S should be
                for possible in "|-F7JL":
                    grid[y][x] = possible
                    possible_connection = get_connections(grid, x, y, debug)
                    if possible_connection == connection:
                        break

                break
    else:
        raise Exception("Unable to find start")

    while start not in (connections[-1][1], connections[-1][2]) or len(connections) <= 2:
        if debug:
            print(f"{connection=}")

        if connections[-1][1] not in visited:
            next_grid = connections[-1][1]
        else:
            next_grid = connections[-1][2]

        if debug:
            print(f"{next_grid=}")
        connection = get_connections(grid, next_grid[0], next_grid[1], debug)
        connections.append(connection)
        visited.add(next_grid)

    results = len(visited) // 2

    return results


def get_connections(
    grid: list[list[str]], x: int, y: int, debug: bool = False
) -> Optional[list[tuple[int, int]]]:
    c = grid[y][x]
    if debug:
        print(f"({x}, {y})= {c}")
    results = []
    results.append((x, y))

    up, down, left, right = ".", ".", ".", "."
    if c == "S":
        if y - 1 >= 0:
            up = grid[y - 1][x]
        if y + 1 < len(grid):
            down = grid[y + 1][x]
        if x - 1 >= 0:
            left = grid[y][x - 1]
        if x + 1 < len(grid[y]):
            right = grid[y][x + 1]

    elif c == "F":
        down = grid[y + 1][x]
        right = grid[y][x + 1]
    elif c == "-":
        left = grid[y][x - 1]
        right = grid[y][x + 1]
    elif c == "7":
        left = grid[y][x - 1]
        down = grid[y + 1][x]
    elif c == "|":
        down = grid[y + 1][x]
        up = grid[y - 1][x]
    elif c == "J":
        up = grid[y - 1][x]
        left = grid[y][x - 1]
    elif c == "L":
        right = grid[y][x + 1]
        up = grid[y - 1][x]

    if debug:
        print(up, down, left, right)

    if up in "|-F7":
        results.append((x, y - 1))
    if down in "|-JL":
        results.append((x, y + 1))
    if left in "|-FL":
        results.append((x - 1, y))
    if right in "|-7J":
        results.append((x + 1, y))

    if len(results) != 3:
        return None

    return results


def get_surrounding(
    grid: list[list[str]], x: int, y: int, debug: bool = False
) -> tuple[str, str, str, str]:
    up, down, left, right = ".", ".", ".", "."
    if y - 1 >= 0:
        up = grid[y - 1][x]
    if y + 1 < len(grid):
        down = grid[y + 1][x]
    if x - 1 >= 0:
        left = grid[y][x - 1]
    if x + 1 < len(grid[y]):
        right = grid[y][x + 1]

    return up, down, left, right


def part2(data: list[str], debug: bool = False) -> int:
    results = 0

    grid = []

    for d in data:
        grid.append(list(d.strip()))

    show(grid, debug)

    connections = []
    start = None
    visited = set()

    for y, row in enumerate(grid):
        if start:
            break
        for x, c in enumerate(row):
            if c == "S":
                connection = get_connections(grid, x, y, debug)
                connections.append(connection)
                assert connection
                start = connection[0]
                visited.add((x, y))

                # figure out what char S should be
                for possible in "|-F7JL":
                    grid[y][x] = possible
                    possible_connection = get_connections(grid, x, y, debug)
                    if possible_connection == connection:
                        break
                break
    else:
        raise Exception("Unable to find start")

    while start not in (connections[-1][1], connections[-1][2]) or len(connections) <= 2:
        if debug:
            print(f"{connection=}")

        if connections[-1][1] not in visited:
            next_grid = connections[-1][1]
        else:
            next_grid = connections[-1][2]

        if debug:
            print(f"{next_grid=}")
        connection = get_connections(grid, next_grid[0], next_grid[1], debug)
        connections.append(connection)
        visited.add(next_grid)

    # Remove all pipes that are not in the path
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if (x, y) not in visited:
                grid[y][x] = "."

    show(grid, debug)

    for y, row in enumerate(grid):
        is_inside = False
        for x, c in enumerate(row):
            c = grid[y][x]
            if c in "|F7":
                is_inside = not is_inside
            if c == "." and is_inside:
                if debug:
                    print(f"{x=}, {y=}")
                grid[y][x] = "*"
                results += 1

    show(grid, debug)

    return results


def show(grid, debug: bool = False):
    if debug:
        print()
        for y in range(len(grid)):
            print("".join([str(x) for x in grid[y]]))


if __name__ == "__main__":
    # print("Test1a: ", run(part=1, test_suffix="-test1a", debug=True))  # 4
    # print("Test1b: ", run(part=1, test_suffix="-test1b", debug=True))  # 8
    # print("Real1: ", run(part=1, debug=False))  # 6828
    # print("Test2a: ", run(part=2, test_suffix="-test2a", debug=True))  # 4
    # print("Test2b: ", run(part=2, test_suffix="-test2b", debug=True))  # 4
    # print("Test2c: ", run(part=2, test_suffix="-test2c", debug=True))  # 8
    # print("Test2d: ", run(part=2, test_suffix="-test2d", debug=True))  # 10
    print("Real2: ", run(part=2, debug=False))  # 459
