def run(part: int, test_suffix: str = "", debug: bool = False):
    y, d = __file__.split("advent-")[1].split("-day")
    file_name = f"{y}/input/{d.strip('.py')}{test_suffix}.txt"

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data if not x.startswith("#")]
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
    print("Test1: ", run(part=1, test_suffix="-test", debug=True))  #
    # TODO: MISSING
    # print("Real1: ", run(part=1, debug=False))  #
    # TODO: MISSING
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True)) #
    # TODO: MISSING
    # print("Real2: ", run(part=2, debug=False))  #

#    print("time", time.time() - start_time)
