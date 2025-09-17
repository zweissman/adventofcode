import itertools
from functools import cache


def run(part: int, test_suffix: str = "", debug: bool = False):
    y, d = __file__.split("advent-")[1].split("-day")
    file_name = f"{y}/input/{d.strip('.py')}{test_suffix}.txt"

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2
    steps = 2 if part == 1 else 25

    return part_function(data=data, steps=steps, debug=debug)


number_pad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [" ", "0", "A"],
]

direction_pad = [
    [" ", "^", "A"],
    ["<", "v", ">"],
]


def part1(data: list[str], steps: int, debug: bool = False) -> int:
    results = 0

    button_previous = "A"

    for code in data:
        min_length = 0
        for button in list(code):
            dir = get_dir([button], "num", button_previous)
            for _ in range(steps):
                dir = get_dir(dir, "dir")

            length = min([len(x) for x in dir])
            min_length += length
            if debug:
                print(button, length)

            button_previous = button

        result = min_length * int(code.replace("A", ""))
        results += result

        if debug:
            print(code, ":", min_length, int(code.replace("A", "")), "=", result)

    return results


def get_dir(codes: list[str], pad_type: str, button_previous: str = "A") -> list[str]:
    results: list = []
    result: list = []

    for code in codes:
        result = []
        for x in list(code):
            result.append(get_dir_from_to(button_previous, x, pad_type))
            button_previous = x

        possible_sequences = ["".join(s) for s in itertools.product(*result)]
        results.extend(possible_sequences)

    return results


def get_dir_from_to(start: str, end: str, pad_type: str) -> list[str]:
    results: list[str] = []

    a, b = (-1, -1), (-1, -1)
    assert len(start) == 1
    assert len(end) == 1

    if start == end:
        return ["A"]
    directions: list[str] = []

    if pad_type == "num":
        pad = number_pad
    else:
        pad = direction_pad

    for y, row in enumerate(pad):
        for x, value in enumerate(row):
            if value == start:
                a = (x, y)
            if value == end:
                b = (x, y)
    assert a != (-1, -1)
    assert b != (-1, -1)

    if b[0] > a[0]:
        directions.extend([">"] * abs(b[0] - a[0]))
    if b[1] < a[1]:
        directions.extend(["^"] * abs(b[1] - a[1]))
    if b[1] > a[1]:
        directions.extend(["v"] * abs(b[1] - a[1]))
    if b[0] < a[0]:
        directions.extend(["<"] * abs(b[0] - a[0]))

    results.append("".join(directions) + "A")
    if "".join(directions[::-1]) + "A" not in results:
        results.append("".join(directions[::-1]) + "A")

    if len(results) > 1:
        # Remove bad combos

        bad_start = ""
        if start in "0^":
            # no left first
            bad_start = "<"
        elif start == "1":
            # No down first
            bad_start = "v"
        elif start == "<":
            # No up first
            bad_start = "^"

        bad_end = ""
        if end in "0^":
            # no right last
            bad_end = ">"
        elif end == "1":
            # No up last
            bad_end = "^"
        elif end == "<":
            # No down last
            bad_end = "v"

        for result in list(results)[::]:
            if bad_start == result[0] or bad_end == result[-2]:
                pass

    return list(results)


def part2(data: list[str], steps: int, debug: bool = False) -> int:
    results = 0

    return part1(data, steps, debug)


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 126384
    # print("Real1: ", run(part=1, debug=True))  # 123096
    print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # 154115708116294
    # print("Real2: ", run(part=2, debug=False))  # 154517692795352
