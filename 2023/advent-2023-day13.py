# pylint: disable=too-many-return-statements,too-many-statements,too-many-branches,duplicate-code,unused-argument
# pylint: disable=unnecessary-list-index-lookup

FILE_NAME = "2023/input/13.txt"


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

    grid = []

    for d in data:
        d = d.strip()
        grid.append(list(d))

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0

    grid = []

    for d in data:
        d = d.strip()
        grid.append(list(d))

    return results



if __name__ == "__main__":
    import time # qa: ignore:E402
    start_time = time.time()

    print("Test1: ", run(part=1, test_run=True, debug=True))  #
    # print("Real1: ", run(part=1, test_run=False, debug=False))  #
    # print("Test2: ", run(part=2, test_run=True, debug=True)) #
    # print("Real2: ", run(part=2, test_run=False, debug=False))  #

#    print(time.time() - start_time)
