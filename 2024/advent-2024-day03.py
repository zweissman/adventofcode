import re


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
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 161
    # print("Real1: ", run(part=1, debug=False))  # 168539636
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # 48
    print("Real2: ", run(part=2, debug=False))  # 97529391
