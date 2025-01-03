def run(part: int, test_suffix: str = "", debug: bool = False):
    y, d = __file__.split("advent-")[1].split("-day")
    file_name = f"{y}/input/{d.strip('.py')}{test_suffix}.txt"

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


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


def is_it_a_part(grid: list[list[str]], x_start: int, y_start: int, length: int) -> bool:
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


def part2(data: list[str], debug: bool = False) -> int:  # pylint: disable = unused-argument
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
                part_number, _ = get_part_number(grid[y], x - 1)  # pylint: disable=unnecessary-list-index-lookup
                part_list.add(part_number)
            except IndexError:
                pass

            try:
                part_number, _ = get_part_number(grid[y], x + 1)  # pylint: disable=unnecessary-list-index-lookup
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
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 4361
    # print("Real1: ", run(part=1, debug=False))  # 560670
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # 467835
    print("Real2: ", run(part=2, debug=False))  # 91622824
