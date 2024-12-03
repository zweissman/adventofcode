FILE_NAME = "2022/input/04.txt"


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
    for row in data:
        left, right = row.split(",")
        start1, end1 = left.split("-")
        start2, end2 = right.split("-")
        start1, end1 = int(start1), int(end1)
        start2, end2 = int(start2), int(end2)

        if debug:
            print(start1, end1, start2, end2)

        if start1 <= start2 and end1 >= end2:
            if debug:
                print("BIG")
            results += 1
        elif start1 >= start2 and end1 <= end2:
            if debug:
                print("ALSO BIG")
            results += 1

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    for row in data:
        left, right = row.split(",")
        start1, end1 = left.split("-")
        start2, end2 = right.split("-")
        start1, end1 = int(start1), int(end1)
        start2, end2 = int(start2), int(end2)

        if debug:
            print(start1, end1, start2, end2)

        if set(range(start1, end1 + 1)).intersection(set(range(start2, end2 + 1))):
            if debug:
                print("OVERLAP")
            results += 1

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # 2
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 515
    # print("Test2: ", run(part=2, test_run=True, debug=True))  # 4
    print("Real2: ", run(part=2, test_run=False, debug=False))  # 883
