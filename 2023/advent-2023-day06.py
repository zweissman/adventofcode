# pylint: disable=too-many-return-statements,too-many-statements,too-many-branches,duplicate-code,unused-argument
# pylint: disable=unnecessary-list-index-lookup

from collections import defaultdict

FILE_NAME = "2023/input/06.txt"


def run(part: int, test_run: bool = False, debug: bool = False):
    if test_run:
        file = FILE_NAME.replace(".txt", "-test.txt")
    else:
        file = FILE_NAME

    with open(file, encoding="utf-8") as f:
        data = f.readlines()

    data = [x.strip() for x in data]
    part_function = part1 if part == 1 else part2

    return part_function(data, debug)


def part1(data: list[str], debug: bool = False) -> int:
    results = 0

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0

    return results


if __name__ == "__main__":
    final = run(part=1, test_run=True, debug=True)  #
    # final = run(part=1, test_run=False, debug=False)  #
    # final = run(part=2, test_run=True, debug=True) #
    # final = run(part=2, test_run=False, debug=False)  #
    print("ANSWER:", final)
