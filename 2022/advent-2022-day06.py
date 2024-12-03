FILE_NAME = "2022/input/06.txt"


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
    x = 4
    for row in data:
        if debug:
            print(row)
        for index in range(len(row) + x - 1):
            if len(set(row[index : index + x])) == x:
                results = index + x
                break

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    x = 14

    for row in data:
        if debug:
            print(row)
        for index in range(len(row) + x - 1):
            if len(set(row[index : index + x])) == x:
                results = index + x
                break

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # 7
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 1723
    # print("Test2: ", run(part=2, test_run=True, debug=True))  # 19
    print("Real2: ", run(part=2, test_run=False, debug=False))  # 3708
