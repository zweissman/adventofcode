import json
from typing import Any


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
    json_data = "".join(data)
    parsed = json.loads(json_data)

    for item in parsed:
        values = get_value(item)
        results += values
        if debug:
            print(values, results)

    return results


def get_value(item: Any) -> int:
    results = 0

    if isinstance(item, int):
        results = item

    elif isinstance(item, list):
        for value in item:
            results += get_value(value)

    elif isinstance(item, dict):
        for _, value in item.items():
            results += get_value(value)

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    json_data = "".join(data)
    parsed = json.loads(json_data)

    for item in parsed:
        values, _ = get_value_no_red(item)
        results += values
        if debug:
            print(values, results)

    return results


def get_value_no_red(item: Any) -> tuple[int, bool]:
    results = 0
    red_flag = False

    if isinstance(item, str):
        if item == "red":
            return 0, True

    elif isinstance(item, int):
        return item, False

    elif isinstance(item, list):
        for value in item:
            result, _ = get_value_no_red(value)
            results += result

    elif isinstance(item, dict):
        for _, value in item.items():
            result, red_flag = get_value_no_red(value)
            if red_flag:
                return 0, False
            results += result

    return results, False


def show(grid: list[str], debug: bool = False) -> None:
    if debug:
        print()
        for y, row in enumerate(grid):
            print(f"{y:02}", "".join([str(x) for x in row]))


if __name__ == "__main__":
    print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 82
    # print("Real1: ", run(part=1, debug=False))  # 191164
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # 65
    # print("Real2: ", run(part=2, debug=False))  # 87842
