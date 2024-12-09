def run(part: int, test_run: bool = False, debug: bool = False) -> int:
    file_name = "2024/input/00.txt"
    if test_run:
        file_name = file_name.replace(".txt", "-test.txt")

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def show(grid: list[str], debug: bool = False) -> None:
    if debug:
        print()
        for y, row in enumerate(grid):
            print(y, "".join([str(x) for x in row]))


def is_inbounds(data: list[str], node: tuple[int, int]) -> bool:
    return 0 <= node[0] < len(data[0]) and 0 <= node[1] < len(data)


def part1(data: list[str], debug: bool = False) -> int:
    results = 0
    show(data, debug=debug)

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    show(data, debug=debug)

    return results


if __name__ == "__main__":
    print("Test1: ", run(part=1, test_run=True, debug=True))  #
    # print("Real1: ", run(part=1, test_run=False, debug=False))  #
    # print("Test2: ", run(part=2, test_run=True, debug=True))  #
    # print("Real2: ", run(part=2, test_run=False, debug=False))  #
