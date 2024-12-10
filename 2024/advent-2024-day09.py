def run(part: int, test_suffix: str = "", debug: bool = False):
    y, d = __file__.split("advent-")[1].split("-day")
    file_name = f"{y}/input/{d.strip('.py')}{test_suffix}.txt"

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def part1(data: list[str], debug: bool = False) -> int:  # pylint: disable=unused-argument
    values = [int(x) for x in list(data[0])]

    results = 0
    l_id = -1
    r_id = ((len(values) - 1) // 2) + 1
    l_size, l_space, r_size, r_space = 0, 0, 0, 0
    block_id = 0

    while True:
        if len(values) == 0:
            # Nothing left to process
            break

        l_size = values.pop(0)
        l_id += 1

        for _ in range(l_size):
            results += l_id * block_id
            block_id += 1

        if len(values) == 0:
            l_space += r_space
        else:
            l_space = values.pop(0)

        while l_space > 0:
            if r_size == 0:
                if len(values) == 0:
                    # Nothing left to process
                    break

                r_size = values.pop()
                r_space = values.pop()  # don't think that we need this
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


def part2(data: list[str], debug: bool = False) -> int:
    values = [int(x) for x in list(data[0])]

    results = 0
    r_max_id = (len(values) - 1) // 2

    full_data = process_data(values, debug)

    while len(values) >= 2:
        r_size = values[-1]
        r_space = values[-2]

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
            start_id = sum(values) - 1
            for y in range(r_size):
                results += r_max_id * (start_id - y)

        r_max_id -= 1
        values.pop()
        values.pop()
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
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 1928
    # print("Real1: ", run(part=1, debug=False))  # 6390180901651
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # 2858
    print("Real2: ", run(part=2, debug=False))  # 6412390114238
