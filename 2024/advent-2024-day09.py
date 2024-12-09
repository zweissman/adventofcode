FILE_NAME = "2024/input/09.txt"


def run(part: int, test_run: bool = False, debug: bool = False) -> int:
    if test_run:
        file = FILE_NAME.replace(".txt", "-test.txt")
    else:
        file = FILE_NAME

    with open(file, encoding="utf-8") as f:
        file_data = f.readlines()

    data = [int(x) for x in list(file_data[0].strip()) if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def part1(data: list[int], debug: bool = False) -> int:  # pylint: disable=unused-argument
    results = 0
    l_id = -1
    r_id = ((len(data) - 1) // 2) + 1
    l_size, l_space, r_size, r_space = 0, 0, 0, 0
    block_id = 0

    while True:
        if len(data) == 0:
            # Nothing left to process
            break

        l_size = data.pop(0)
        l_id += 1

        for _ in range(l_size):
            results += l_id * block_id
            block_id += 1

        if len(data) == 0:
            l_space += r_space
        else:
            l_space = data.pop(0)

        while l_space > 0:
            if r_size == 0:
                if len(data) == 0:
                    # Nothing left to process
                    break

                r_size = data.pop()
                r_space = data.pop()  # don't think that we need this
                r_id -= 1

            results += r_id * block_id
            block_id += 1
            r_size -= 1
            l_space -= 1

    while r_size > 0:
        results += r_id * block_id
        block_id += 1
        r_size -= 1

    return results


def part2(data: list[int], debug: bool = False) -> int:
    results = 0
    r_max_id = (len(data) - 1) // 2

    full_data = process_data(data, debug)

    while len(data) >= 2:
        r_size = data[-1]
        r_space = data[-2]

        if debug:
            print(full_data)
        # Remove these parts so we don't move data to places that were already processed

        splitted = full_data.split("." * r_size, 1)

        if len(splitted) == 2:
            # found a place for it, calc new location
            left, right = splitted[0], splitted[1]
            full_data = left + ("X" * r_size) + right

            start_id = len(left)
            for y in range(r_size):
                results += r_max_id * (start_id + y)

        else:
            # Calc where it is
            start_id = sum(data) - 1
            for y in range(r_size):
                results += r_max_id * (start_id - y)

        r_max_id -= 1
        data.pop()
        data.pop()
        full_data = full_data[: -r_size - r_space]

    return results


def process_data(data: list[int], debug: bool) -> str:
    results = ""

    for x in range(0, len(data), 2):
        l_size = data[x]
        try:
            l_space = data[x + 1]
        except IndexError:
            l_space = 0

        results += ("X" * l_size) + ("." * l_space)

    if debug:
        print(results)

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # 1928
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 6390180901651
    # print("Test2: ", run(part=2, test_run=True, debug=True))  # 2858
    print("Real2: ", run(part=2, test_run=False, debug=False))  # 6412390114238
