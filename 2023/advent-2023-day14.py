# pylint: disable=too-many-return-statements,too-many-statements,too-many-branches,duplicate-code,unused-argument
# pylint: disable=unnecessary-list-index-lookup


FILE_NAME = "2023/input/14.txt"


def run(part: int, test_run: bool = False, debug: bool = False):
    if test_run:
        file = FILE_NAME.replace(".txt", "-test.txt")
    else:
        file = FILE_NAME

    with open(file, encoding="utf-8") as f:
        data = f.readlines()

    data = [x.strip() for x in data]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def part1(data: list[str], debug: bool = False) -> int:
    results = 0

    grid = []
    for d in data:
        if d.startswith("//"):
            continue

        grid.append(list(d))

    print("Start")
    show(grid, debug)

    direction = "N"

    if direction == "E":
        degrees = 0
    elif direction == "N":
        degrees = 90
    elif direction == "W":
        degrees = 180
    elif direction == "S":
        degrees = 270
    else:
        raise Exception("Invalid direction", direction)

    grid_rotated = rotate(grid, degrees)

    #    print("Rotated", direction, degrees)
    #    show(grid_rotated, debug)

    for y, row in enumerate(grid_rotated):
        line = "".join(row).split("#")
        new_line = []
        for section in line:
            if section == "":
                new_line.append("")
                continue
            stones = section.count("O")
            new_line.append("." * (len(section) - stones) + "O" * stones)
        grid_rotated[y] = list("#".join(new_line))

    #    print("After move")
    #    show(grid_rotated, debug)
    grid = rotate(grid_rotated, -degrees)
    #    print("After rotated back")
    show(grid, debug)

    for y, row in enumerate(grid):
        results += row.count("O") * (len(grid) - y)

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0

    grid = []
    for d in data:
        if d.startswith("//"):
            continue

        grid.append(list(d))

    print("Start")
    show(grid, debug)

    directions = "NWSE"
    cycle = 0

    for cycle in range(1, 1000000000):
        if cycle % 10000 == 0:
            print(1000000000 - cycle)
        for direction in directions:
            # if direction == "E":
            #     degrees = 0
            # elif direction == "N":
            #     degrees = 90
            # elif direction == "W":
            #     degrees = 180
            # elif direction == "S":
            #     degrees = 270
            # else:
            #     raise Exception("Invalid direction", direction)

            grid = rotate(grid, 90)

            #    print("Rotated", direction, degrees)
            #    show(grid_rotated, debug)

            for y, row in enumerate(grid):
                line = "".join(row).split("#")
                new_line = []
                for section in line:
                    if section == "":
                        new_line.append("")
                        continue
                    stones = section.count("O")
                    new_line.append("." * (len(section) - stones) + "O" * stones)
                grid[y] = list("#".join(new_line))

            # grid = rotate(grid_rotated, -degrees)

            if debug:
                print(f"Cycle {cycle}: {direction}")
            show(grid, debug)
            if debug:
                print()

        if debug:
            print(f"Cycle {cycle}")
        show(grid, debug)
        if debug:
            print()

    for y, row in enumerate(grid):
        results += row.count("O") * (len(grid) - y)

    return results


def part2x(data: list[str], debug: bool = False) -> int:
    results = 0

    grid = []
    for d in data:
        if d.startswith("//"):
            continue

        grid.append(list(d))

    show(grid, debug)

    directions = "NWSE"
    cycle = 0

    for cycle in range(1, 1000000000):
        if cycle % 10000 == 0:
            print(cycle)
        for direction in directions:
            if direction in "NW":
                for y, row in enumerate(grid):
                    for x, c in enumerate(row):
                        if c == "O":
                            if direction == "N":
                                if y == 0:
                                    continue
                                y_new = y

                                while y_new - 1 >= 0 and grid[y_new - 1][x] == ".":
                                    y_new -= 1

                                if y_new < y:
                                    grid[y][x] = "."
                                    grid[y_new][x] = "O"

                            elif direction == "W":
                                if x == 0:
                                    continue
                                x_new = x

                                while x_new - 1 >= 0 and grid[y][x_new - 1] == ".":
                                    x_new -= 1

                                if x_new < x:
                                    grid[y][x] = "."
                                    grid[y][x_new] = "O"
            else:
                for y in range(len(grid) - 1, -1, -1):
                    for x in range(len(grid[y]) - 1, -1, -1):
                        c = grid[y][x]
                        if c == "O":
                            if direction == "S":
                                if y == len(grid) - 1:
                                    continue
                                y_new = y

                                while y_new + 1 < len(grid) and grid[y_new + 1][x] == ".":
                                    y_new += 1

                                if y_new > y:
                                    grid[y][x] = "."
                                    grid[y_new][x] = "O"

                            elif direction == "E":
                                if x == len(grid[0]) - 1:
                                    continue
                                x_new = x

                                while x_new + 1 < len(grid[0]) and grid[y][x_new + 1] == ".":
                                    x_new += 1

                                if x_new > x:
                                    grid[y][x] = "."
                                    grid[y][x_new] = "O"

            if debug:
                print(f"Cycle {cycle}: {direction}")
            show(grid, debug)
            if debug:
                print()

        if debug:
            print(f"Cycle {cycle}")
        show(grid, debug)
        if debug:
            print()

    for y, row in enumerate(grid):
        results += row.count("O") * (len(grid) - y)

    return results


def rotate(matrix, degree):
    if degree == 0:
        return matrix
    elif degree > 0:
        return rotate(list(zip(*matrix[::-1])), degree - 90)
    else:
        return rotate(matrix, 360 + degree)


def show(grid, debug):
    if debug:
        for row in grid:
            print("".join([str(x) for x in row]))
        print()


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # 136
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 106990
    print("Test2: ", run(part=2, test_run=True, debug=False))  #
    # print("Real2: ", run(part=2, test_run=False, debug=False))  #
