# pylint: disable=too-many-return-statements,too-many-statements,too-many-branches,duplicate-code,unused-argument
# pylint: disable=unnecessary-list-index-lookup

import itertools

FILE_NAME = "2023/input/11.txt"


def run(
    part: int, empty_row_count: int = 1, test_run: bool = False, debug: bool = False
):
    if test_run:
        file = FILE_NAME.replace(".txt", "-test.txt")
    else:
        file = FILE_NAME

    with open(file, encoding="utf-8") as f:
        data = f.readlines()

    data = [x.strip() for x in data]
    part_function = part1 if part == 1 else part2

    return part_function(data, empty_row_count, debug)


def show(grid: list[list[str]], debug: bool = False):
    if debug:
        print()
        for y in range(len(grid)):
            print("".join([str(x) for x in grid[y]]))


def part1(data: list[str], empty_row_count: int = 1, debug: bool = False) -> int:
    results = 0

    grid, empty_rows, empty_cols = [], [], []

    for i, d in enumerate(data):
        d = d.strip()
        grid.append(list(d))
        if d == len(d) * ".":
            empty_rows.append(i)

    for x in range(len(grid[0])):
        for y in range(len(grid)):  # pylint: disable=consider-using-enumerate
            c = grid[y][x]
            if c == "#":
                break
        else:
            empty_cols.append(x)

    show(grid, debug)

    if debug:
        print(f"{empty_rows=}")
    if debug:
        print(f"{empty_cols=}")

    stars = {}
    star_count = 1
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == "#":
                stars[star_count] = (x, y)
                star_count += 1

    if debug:
        print(stars)

    combos = list(itertools.combinations(range(len(stars)), 2))

    for star1, star2 in combos:
        distance = calc_distance(
            stars[star1 + 1],
            stars[star2 + 1],
            empty_rows,
            empty_cols,
            empty_row_count,
        )
        results += distance

        # if debug: print(f"{star1+1}: {stars[star1+1]}")
        # if debug: print(f"{star2+1}: {stars[star2+1]}")
        # if debug: print(distance)

    return results


def calc_distance(
    star1: tuple[int, int],
    star2: tuple[int, int],
    empty_rows: list[int],
    empty_cols: list[int],
    empty_row_count: int,
) -> int:
    distance = abs(star1[0] - star2[0]) + abs(star1[1] - star2[1])

    for empty_row in empty_rows:
        if (star1[1] < empty_row < star2[1]) or (star2[1] < empty_row < star1[1]):
            distance += empty_row_count

    for empty_col in empty_cols:
        if (star1[0] < empty_col < star2[0]) or (star2[0] < empty_col < star1[0]):
            distance += empty_row_count

    return distance


def part2(data: list[str], empty_row_count: int = 1, debug: bool = False) -> int:
    return part1(data, empty_row_count, debug)


if __name__ == "__main__":
    # final = run(part=1, empty_row_count=1, test_run=True, debug=True)  # 374
    # final = run(part=1, empty_row_count=1, test_run=False, debug=False)  # 9543156
    # final = run(part=2, empty_row_count=999999, test_run=True, debug=True) # 82000210
    final = run(
        part=2, empty_row_count=999999, test_run=False, debug=False
    )  # 625243292686
    print("ANSWER:", final)
