def run(part: int, test_suffix: str = "", debug: bool = False):  # pylint: disable=duplicate-code
    file_name = "2023/input/00.txt"
    if test_suffix:
        file_name = file_name.replace(".txt", test_suffix + ".txt")

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def part1(data: list[str], debug: bool = False) -> int:
    results = 0

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0

    return results


if __name__ == "__main__":
    print("Test1: ", run(part=1, test_suffix="-test1", debug=True))  #
    print("Real1: ", run(part=1, debug=False))  #
    print("Test2: ", run(part=2, test_suffix="-test2", debug=True))  #
    print("Real2: ", run(part=2, debug=False))  #
