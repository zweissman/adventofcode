FILE_NAME = "2022/input/08.txt"


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
    grid = []

    for row in data:
        grid.append(list(row))

    for row in grid:
        if debug:
            print(row)

    results = 2 * len(grid) + 2 * len(grid[0]) - 4

    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[x]) - 1):
            if debug:
                print("GRID:", x, y, grid[x][y])
            results += is_visible(grid, x, y)

    return results


def is_visible(grid, x, y):
    height = grid[x][y]

    # Left
    for xx in range(x - 1, -1, -1):
        if grid[xx][y] >= height:
            break
    else:
        return 1

    # Right
    for xx in range(x + 1, len(grid)):
        if grid[xx][y] >= height:
            break
    else:
        return 1

    # Up
    for yy in range(y - 1, -1, -1):
        if grid[x][yy] >= height:
            break
    else:
        return 1

    # Down
    for yy in range(y + 1, len(grid[0])):
        if grid[x][yy] >= height:
            break
    else:
        return 1

    return 0


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    grid = []

    for row in data:
        grid.append(list(row))

    if debug:
        for row in grid:
            print(row)

    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[x]) - 1):
            if debug:
                print("GRID:", x, y, grid[x][y])
            score = calc_score(grid, x, y)
            if debug:
                print("SCORE:", score)
            results = max(results, score)

    return results


def calc_score(grid, x, y):
    height = grid[x][y]

    # Up
    score_up = 0
    for xx in range(x - 1, -1, -1):
        if grid[xx][y] < height:
            score_up += 1
        else:
            score_up += 1
            break

    # Down
    score_down = 0
    for xx in range(x + 1, len(grid)):
        if grid[xx][y] < height:
            score_down += 1
        else:
            score_down += 1
            break

    # Left
    score_left = 0
    for yy in range(y - 1, -1, -1):
        if grid[x][yy] < height:
            score_left += 1
        else:
            score_left += 1
            break

    # Right
    score_right = 0
    for yy in range(y + 1, len(grid[0])):
        if grid[x][yy] < height:
            score_right += 1
        else:
            score_right += 1
            break

    total_score = score_up * score_down * score_left * score_right
    return total_score


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # 21
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 1715
    # print("Test2: ", run(part=2, test_run=True, debug=True))  # 8
    print("Real2: ", run(part=2, test_run=False, debug=False))  # 374400
