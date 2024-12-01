# pylint: disable=too-many-return-statements,too-many-statements,too-many-branches,duplicate-code,unused-argument
# pylint: disable=unnecessary-list-index-lookup

FILE_NAME = "2024/input/01.txt"


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

    list1 = []
    list2 = []

    for d in data:
        a, b = d.split("  ")
        list1.append(int(a.strip()))
        list2.append(int(b.strip()))

    list1 = sorted(list1)
    list2 = sorted(list2)

    for i, _ in enumerate(list1):
        results += abs(list1[i] - list2[i])

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0

    list1 = []
    list2 = []

    for d in data:
        a, b = d.split("  ")
        list1.append(int(a.strip()))
        list2.append(int(b.strip()))

    for i, x in enumerate(list1):
        x = list1[i]
        results += x * list2.count(x)

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))
    # print("Real1: ", run(part=1, test_run=False, debug=False))
    # print("Test2: ", run(part=2, test_run=True, debug=True))
    print("Real2: ", run(part=2, test_run=False, debug=False))
