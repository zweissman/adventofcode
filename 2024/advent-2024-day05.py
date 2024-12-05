from copy import deepcopy

FILE_NAME = "2024/input/05.txt"


def run(part: int, test_run: bool = False, debug: bool = False) -> int:
    if test_run:
        file = FILE_NAME.replace(".txt", "-test.txt")
    else:
        file = FILE_NAME

    with open(file, encoding="utf-8") as f:
        data = f.readlines()

    data = [x.strip() for x in data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def show(grid: list[str], debug: bool = False) -> None:
    if debug:
        print()
        for y, row in enumerate(grid):
            print(y, "".join([str(x) for x in row]))


def part1(data: list[str], debug: bool = False) -> int:
    results = 0

    show(data, debug=debug)
    page_map = get_map(data)

    for x, row in enumerate(data):
        row_values = [int(x) for x in row.split(",")]
        middle_value = row_values[(len(row_values) - 1) // 2]

        is_valid, _ = check_row(row_values, page_map)

        if is_valid:
            results += middle_value
            if debug:
                print(x, f"Adding middle value {middle_value}")

    return results


def get_map(data: list[str]) -> dict[int, list[int]]:
    page_map = {}

    while True:
        item = data.pop(0)
        if item == "":
            break

        k, v = (int(x) for x in item.split("|"))
        if k not in page_map:
            page_map[k] = [v]
        else:
            page_map[k].append(v)

    return page_map


def part2(data: list[str], debug: bool = False) -> int:
    results = 0

    show(data, debug=debug)
    page_map = get_map(data)

    for x, row in enumerate(data):
        row_values = [int(x) for x in row.split(",")]
        row_values_original = deepcopy(row_values)

        is_valid, bad_index = check_row(row_values, page_map)

        if not is_valid:
            while not is_valid:
                middle_value = 0

                row_values = fix_it(row_values_original, bad_index)
                row_values_original = deepcopy(row_values)

                is_valid, bad_index = check_row(row_values, page_map)

            middle_value = row_values_original[(len(row_values_original) - 1) // 2]
            results += middle_value
            if debug:
                print(x, f"Adding middle value {middle_value}")

    return results


def check_row(row_values: list[int], page_map: dict[int, list[int]]) -> tuple[bool, int]:
    valid = True

    while valid:
        page = row_values.pop(0)

        for item in row_values:
            if page not in page_map:
                valid = False
                break

            if item not in page_map[page]:
                valid = False
                break

        if len(row_values) == 0:
            break

    if valid:
        item = 0

    return valid, item


def fix_it(row: list[int], bad_page: int) -> list:
    new_row = deepcopy(row)
    index = new_row.index(bad_page)

    # swap the bad page index with the page before it
    new_row[index - 1], new_row[index] = new_row[index], new_row[index - 1]

    return new_row


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # 143
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 7074
    # print("Test2: ", run(part=2, test_run=True, debug=True))  # 123
    print("Real2: ", run(part=2, test_run=False, debug=False))  # 4828
