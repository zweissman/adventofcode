FILE_NAME = "2022/input/01.txt"


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


def part1(data: list[str], debug: bool = False) -> int: #type: ignore[unused-argument]
    max_total = 0
    total = 0

    for row in data:
        if debug: print(row)
        if row in (0, ""):
            max_total = max(total, max_total)
            total = 0
        else:
            total += int(row)

    results = max(total, max_total)

    return results


def part2(data: list[str], debug: bool = False) -> int:
    max_total = []
    total = 0

    for row in data:
        if row in (0, ""):
            if debug:
                print(total)
            max_total.append(total)
            max_total.sort(reverse=True)
            max_total = max_total[:3]
            total = 0
        else:
            total += int(row)

    if debug:
        print(total)
    max_total.append(total)
    max_total.sort(reverse=True)
    max_total = max_total[:3]

    return sum(max_total)


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True)) # 24000
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 69626
    # print("Test2: ", run(part=2, test_run=True, debug=True))  # 45000
    print("Real2: ", run(part=2, test_run=False, debug=False))  # 206780
