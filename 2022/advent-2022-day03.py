FILE_NAME = "2022/input/03.txt"


def run(part: int, test_run: bool = False, debug: bool = False):
    if test_run:
        file = FILE_NAME.replace(".txt", "-test.txt")
    else:
        file = FILE_NAME

    with open(file, encoding="utf-8") as f:
        data = f.readlines()

    data = [x.strip() for x in data]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def part1(data: list[str], debug: bool = False) -> int:
    results = 0
    common = []

    for line in data:
        line = list(line)
        line_length = len(line)
        left, right = line[: int(line_length / 2)], line[int(line_length / 2) :]

        common.append(list(set(left) & set(right))[0])

    if debug:
        print(common)

    for let in common:
        if let.isupper():
            results += ord(let) - ord("A") + 26 + 1
        else:
            results += ord(let) - ord("a") + 1

        if debug:
            print(results)

    return results


def part2(data: list[str], debug: bool = False) -> int:
    common = []

    for index in range(0, len(data), 3):
        common.append(list(set(data[index]) & set(data[index + 1]) & set(data[index + 2]))[0])

    if debug:
        print(common)

    return calc_score(common, debug=debug)


def calc_score(common, debug=False):
    results = 0
    for let in common:
        if let.isupper():
            results += ord(let) - ord("A") + 26 + 1
        else:
            results += ord(let) - ord("a") + 1
        if debug:
            print(results)

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # 157
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 8515
    # print("Test2: ", run(part=2, test_run=True, debug=True))  # 70
    print("Real2: ", run(part=2, test_run=False, debug=False))  # 2434
