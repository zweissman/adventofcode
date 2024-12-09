import itertools
import math
from collections.abc import Iterator


def run(part: int, test_suffix: str = "", debug: bool = False):
    file = "2023/input/08.txt"

    if test_suffix:
        file = file.replace(".txt", test_suffix + ".txt")

    with open(file, encoding="utf-8") as f:
        file_data = f.readlines()

    data = [x.strip() for x in file_data]
    part_function = part1 if part == 1 else part2

    return part_function(data, debug)


def part1(data: list[str], debug: bool = False) -> int:
    results = 0

    directions = list(data.pop(0))
    data.pop(0)
    nodes = {}

    for line in data:
        node, options = line.split(" = ")
        left, right = options.replace("(", "").replace(")", "").split(", ")
        nodes[node] = (left, right)

    path = "AAA"

    get_direction = get_next_direction(directions)
    while path != "ZZZ":
        direction = next(get_direction)
        if debug:
            print(f"Direction: {direction}")
        if direction == "L":
            path = nodes[path][0]
        else:
            path = nodes[path][1]
        if debug:
            print(f"Path: {path}")
        results += 1

    return results


def get_next_direction(directions: list[str]) -> Iterator[str]:
    yield from itertools.cycle(directions)


def part2(data: list[str], debug: bool = False) -> int:
    directions = list(data.pop(0))
    data.pop(0)

    nodes = {}
    result_list = []

    for line in data:
        node, options = line.split(" = ")
        left, right = options.replace("(", "").replace(")", "").split(", ")
        nodes[node] = (left, right)

    if debug:
        print(nodes.keys())

    for start_path in [node for node, _ in nodes.items() if node.endswith("A")]:
        if debug:
            print(f"Start Path: {start_path}")
        results = 0

        get_direction = get_next_direction(directions)

        path = start_path

        while not path.endswith("Z"):
            direction = next(get_direction)
            if debug:
                print(f"Direction: {direction}")
            if direction == "L":
                path = nodes[path][0]
            else:
                path = nodes[path][1]
            if debug:
                print(f"Path: {path}")
            results += 1

        result_list.append(results)

    if debug:
        print(result_list)

    return math.lcm(*result_list)


if __name__ == "__main__":
    # print("Test1a: ", run(part=1, test_suffix="-test1a", debug=True))  # 2
    # print("Test1b: ", run(part=1, test_suffix="-test1b", debug=True))  # 6
    # print("Real1: ", run(part=1, debug=False))  # 12361
    # print("Test2: ", run(part=2, test_suffix="-test2", debug=True))  # 6
    print("Real2: ", run(part=2, debug=False))  # 18215611419223
