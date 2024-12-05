import re

FILE_NAME = "2024/input/03.txt"


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


def part1(data: list[str], debug: bool = False) -> int:
    results = 0
    text = "".join(data)

    if debug:
        print(text)

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    regex = re.compile(pattern)
    matches = regex.findall(text)

    if debug:
        print(matches)

    for a, b in matches:
        results += int(a) * int(b)

    return results


def part2(data: list[str], debug: bool = False) -> int:
    # Start with a do() operand
    text = "do()" + "".join(data)

    if debug:
        print(text)

    # Remove all the don't() ... do(), then rerun part 1
    pattern = r"don't\(\).*?(?:do\(\)|$)"
    text = re.sub(pattern, "", text)

    return part1([text], debug)


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # 161
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 168539636
    # print("Test2: ", run(part=2, test_run=True, debug=True))  # 48
    print("Real2: ", run(part=2, test_run=False, debug=False))  # 97529391
