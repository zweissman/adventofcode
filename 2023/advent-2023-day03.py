# pylint: disable=too-many-return-statements,too-many-statements,too-many-branches,duplicate-code,unused-argument
# pylint: disable=unnecessary-list-index-lookup

FILE_NAME = "2023/input/03.txt"


def run(part: int, test_run: bool = False, debug: bool = False):
    if test_run:
        file = FILE_NAME.replace(".txt", "-test.txt")
    else:
        file = FILE_NAME

    with open(file, encoding="utf-8") as f:
        data = f.readlines()
    part_function = part1 if part == 1 else part2

    return part_function(data, debug)


def part1(data: list[str], debug: bool = False) -> int:
    results = 0
    grid = []

    for d in data:
        grid.append(list(d.strip()))

    for y, row in enumerate(grid):
        x = 0
        while x < len(row):
            cell = row[x]
            if not cell.isnumeric():
                x += 1
                continue

            part_number, length = get_part_number(row, x)
            is_part_flag = is_it_a_part(grid, x, y, length)

            if is_part_flag:
                if debug:
                    print("found part", part_number, "at", x, y, "length", length)
                results += int(part_number)

            x += length

    return results


def get_part_number(row: list[str], x_start: int) -> tuple[str, int]:
    part_number = ""

    if row[x_start].isnumeric():
        while x_start - 1 >= 0 and row[x_start - 1].isnumeric():
            x_start -= 1

    for x in range(x_start, len(row)):
        if row[x].isnumeric():
            part_number += row[x]
        else:
            #            print(f"{part_number=}")
            break
    else:
        x += 1

    return part_number, x - x_start


def is_it_a_part(
    grid: list[list[str]], x_start: int, y_start: int, length: int
) -> bool:
    if x_start != 0 and is_part(grid[y_start][x_start - 1]):
        # Check left
        return True
    if x_start + length < len(grid) and is_part(grid[y_start][x_start + length]):
        # Check right
        return True

    if y_start != 0:
        # Check above
        for x in range(max(0, x_start - 1), min(len(grid[0]), x_start + length + 1)):
            if is_part(grid[y_start - 1][x]):
                return True

    if y_start + 1 < len(grid):
        # Check below
        for x in range(max(0, x_start - 1), min(len(grid[0]), x_start + length + 1)):
            if is_part(grid[y_start + 1][x]):
                return True

    return False


def is_part(cell: str) -> bool:
    return not cell.isnumeric() and cell != "."


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    grid = []

    for d in data:
        grid.append(list(d.strip()))

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell != "*":
                continue

            part_list = set()
            try:
                part_number, _ = get_part_number(grid[y - 1], x - 1)
                part_list.add(part_number)
            except IndexError:
                pass

            try:
                part_number, _ = get_part_number(grid[y - 1], x)
                part_list.add(part_number)
            except IndexError:
                pass

            try:
                part_number, _ = get_part_number(grid[y - 1], x + 1)
                part_list.add(part_number)
            except IndexError:
                pass

            try:
                part_number, _ = get_part_number(grid[y], x - 1)
                part_list.add(part_number)
            except IndexError:
                pass

            try:
                part_number, _ = get_part_number(grid[y], x + 1)
                part_list.add(part_number)
            except IndexError:
                pass

            try:
                part_number, _ = get_part_number(grid[y + 1], x - 1)
                part_list.add(part_number)
            except IndexError:
                pass

            try:
                part_number, _ = get_part_number(grid[y + 1], x)
                part_list.add(part_number)
            except IndexError:
                pass

            try:
                part_number, _ = get_part_number(grid[y + 1], x + 1)
                part_list.add(part_number)
            except IndexError:
                pass

            part_list.discard("")
            if len(part_list) == 2:
                parts = list(part_list)
                results += int(parts[0]) * int(parts[1])

    return results


if __name__ == "__main__":
    # final = run(part=1, test_run=True, debug=True) # 4361
    # final = run(part=1, test_run=False, debug=False)  # 560670
    # final = run(part=2, test_run=True, debug=True) # 467835
    final = run(part=2, test_run=False, debug=False)  # 91622824
    print("ANSWER:", final)
