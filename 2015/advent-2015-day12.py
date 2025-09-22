"""
--- Day 12: JSAbacusFramework.io ---
Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.

They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.

For example:

[1,2,3] and {"a":2,"b":4} both have a sum of 6.
[[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
{"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
[] and {} both have a sum of 0.
You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?

Your puzzle answer was 191164.

--- Part Two ---
Uh oh - the Accounting-Elves have realized that they double-counted everything red.

Ignore any object (and all of its children) which has any property with the value "red". Do this only for objects ({...}), not arrays ([...]).

[1,2,3] still has a sum of 6.
[1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
{"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
[1,"red",5] has a sum of 6, because "red" in an array has no effect.

Your puzzle answer was 87842.
"""

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
