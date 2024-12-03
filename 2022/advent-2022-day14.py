FILE_NAME = "2022/input/14.txt"


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
    left = 999999
    right = 0
    depth = 0
    grid = []
    sand_start = (500, 0)

    for row in data:
        points = row.split(" -> ")
        for point in points:
            x, y = point.split(",")
            x = int(x)
            y = int(y)

            left = min(left, x)
            right = max(right, x)
            depth = max(depth, y)

    if debug:
        print(left, right, depth)
    grid = [["."] * (right - left + 1) for i in range(depth + 1)]
    sand_start = (sand_start[0] - left, sand_start[1])
    grid[sand_start[1]][sand_start[0]] = "+"

    if debug:
        show(grid)

    for row in data:
        points = row.split(" -> ")
        for i in range(len(points) - 1):
            x1, y1 = points[i].split(",")
            x2, y2 = points[i + 1].split(",")
            x1 = int(x1) - left
            y1 = int(y1)
            x2 = int(x2) - left
            y2 = int(y2)

            if abs(x1 - x2) == 0:
                # vertical
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    grid[y][x1] = "#"
            else:
                # horizontal
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    grid[y1][x] = "#"

    #            if debug: show(grid)

    sand_count = 1
    while drop_sand(sand_start[0], sand_start[1], grid, debug):
        sand_count += 1
    return sand_count - 1


def part2(data: list[str], debug: bool = False) -> int:
    left = 999999
    right = 0
    depth = 0
    grid = []
    sand_start = (500, 0)

    for row in data:
        points = row.split(" -> ")
        for point in points:
            x, y = point.split(",")
            x = int(x)
            y = int(y)

            left = min(left, x)
            right = max(right, x)
            depth = max(depth, y)

    if debug:
        print(left, right, depth)
    # Adjust for "infinite floor"
    left = left - depth
    right = right + depth

    grid = [["."] * (right - left + 1) for i in range(depth + 1 + 2)]
    sand_start = (sand_start[0] - left, sand_start[1])
    grid[sand_start[1]][sand_start[0]] = "+"

    # init floor
    for x in range(len(grid[0])):
        grid[len(grid) - 1][x] = "@"

    if debug:
        show(grid)

    for row in data:
        points = row.split(" -> ")
        for i in range(len(points) - 1):
            x1, y1 = points[i].split(",")
            x2, y2 = points[i + 1].split(",")
            x1 = int(x1) - left
            y1 = int(y1)
            x2 = int(x2) - left
            y2 = int(y2)

            if abs(x1 - x2) == 0:
                # vertical
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    grid[y][x1] = "#"
            else:
                # horizontal
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    grid[y1][x] = "#"

    #            if debug: show(grid)

    sand_count = 1
    while drop_sand(sand_start[0], sand_start[1], grid, debug):
        sand_count += 1

    return sand_count


def drop_sand(x, y, grid, debug):
    try:
        while grid[y + 1][x] == ".":
            y += 1

        # check diagonal left
        if grid[y + 1][x - 1] == ".":
            return drop_sand(x - 1, y, grid, debug)

        # check diagonal right
        if grid[y + 1][x + 1] == ".":
            return drop_sand(x + 1, y, grid, debug)

        grid[y][x] = "*"
        if debug:
            show(grid)
        grid[y][x] = "o"
        if y == 0:
            return False

        return True
    except IndexError:
        return False


def show(grid):
    print()
    for y in range(len(grid)):
        print("".join([str(x) for x in grid[y]]))


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # 24
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 1199
    # print("Test2: ", run(part=2, test_run=True, debug=True))  # 93
    print("Real2: ", run(part=2, test_run=False, debug=False))  # 23925
