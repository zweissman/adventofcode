def run(part: int, test_run: bool = False, debug: bool = False):
    file_name = "2023/input/13.txt"
    if test_run:
        file_name = file_name.replace(".txt", "-test.txt")

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def part1(data: list[str], debug: bool = False) -> int:  # pylint: disable = unused-argument
    results = 0

    grid = []

    for d in data:
        d = d.strip()
        grid.append(list(d))

    return results


def part2(data: list[str], debug: bool = False) -> int:  # pylint: disable = unused-argument
    results = 0

    grid = []

    for d in data:
        d = d.strip()
        grid.append(list(d))

    return results


if __name__ == "__main__":
    import time  # qa: ignore:E402

    start_time = time.time()

    # TODO: MISSING
    print("Test1: ", run(part=1, test_run=True, debug=True))  #
    # TODO: MISSING
    # print("Real1: ", run(part=1, test_run=False, debug=False))  #
    # TODO: MISSING
    # print("Test2: ", run(part=2, test_run=True, debug=True)) #
    # TODO: MISSING
    # print("Real2: ", run(part=2, test_run=False, debug=False))  #

#    print("time", time.time() - start_time)
