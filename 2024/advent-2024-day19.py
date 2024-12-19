from functools import cache


def run(part: int, test_suffix: str = "", debug: bool = False):
    y, d = __file__.split("advent-")[1].split("-day")
    file_name = f"{y}/input/{d.strip('.py')}{test_suffix}.txt"

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def part1(data: list[str], debug: bool = False) -> int:
    global TOWELS
    TOWELS = data.pop(0).split(", ")

    results = 0
    data.pop(0)
    patterns = data

    for towel in TOWELS:
        if towel[0] not in TOWEL_DICT:
            TOWEL_DICT[towel[0]] = []
        TOWEL_DICT[towel[0]].append(towel)

    for pattern in patterns:
        result = get_pattern_count(pattern)
        if result > 0:
            results += 1
        if debug:
            print(result, pattern)

    return results

    # import re2 as re

    # regex_pattern = towels.replace(", ", "|")
    # regex_pattern = "^(?:" + regex_pattern + ")*$"

    # regex = re.compile(regex_pattern)
    # for pattern in patterns:
    #     result = len(regex.findall(pattern))
    #     results += result
    #     if debug:
    #         print(result, pattern)

    # return results


TOWEL_DICT: dict[str, list[str]] = {}
TOWELS: list[str] = []


def part2(data: list[str], debug: bool = False) -> int:
    global TOWELS
    TOWELS = data.pop(0).split(", ")

    results = 0
    data.pop(0)
    patterns = data

    for towel in TOWELS:
        if towel[0] not in TOWEL_DICT:
            TOWEL_DICT[towel[0]] = []
        TOWEL_DICT[towel[0]].append(towel)

    for pattern in patterns:
        result = get_pattern_count(pattern)
        results += result
        if debug:
            print(result, pattern)

    return results


@cache
def get_pattern_count(pattern: str) -> int:
    results = 0
    if pattern in TOWELS:
        results += 1

    if pattern != "" and pattern[0] in TOWEL_DICT:
        for prefix in TOWEL_DICT[pattern[0]]:
            if pattern.startswith(prefix):
                results += get_pattern_count(pattern[len(prefix) :])

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 6
    # print("Real1: ", run(part=1, debug=False))  # 300
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # 16
    print("Real2: ", run(part=2, debug=False))  # 624802218898092
