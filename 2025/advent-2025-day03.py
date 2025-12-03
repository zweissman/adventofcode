def run(part: int, test_suffix: str = "", debug: bool = False):
    y, d = __file__.split("advent-")[1].split("-day")
    file_name = f"{y}/input/{d.strip('.py')}{test_suffix}.txt"

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def part1(data: list[str], debug: bool = False) -> int:
    results = 0
    show(data, debug=debug)

    for row in data:
        results += get_power(row, 2, debug=debug)

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    show(data, debug=debug)

    for row in data:
        results += get_power(row, 12, debug=debug)

    return results


def get_power(row: str, count: int = 2, debug: bool = False) -> int:
    if debug:
        print(row)
    digits = []

    numbers = [int(x) for x in row]
    max_index = 0

    for x in range((count - 1) * -1, 0):
        max_number = max(numbers[max_index:x])
        max_index = numbers.index(max_number, max_index) + 1
        digits.append(max_number)

    max_number = max(numbers[max_index:])
    digits.append(max_number)

    # Join the string representations of the integers
    results = int("".join([str(num) for num in digits]))

    if debug:
        print("\t", results)
    assert len(digits) == count

    return results


def show(grid: list[str], debug: bool = False) -> None:
    if debug:
        print()
        for y, row in enumerate(grid):
            print(f"{y:02}", "".join([str(x) for x in row]))


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 357
    # print("Real1: ", run(part=1, debug=False))  # 17092
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # 3121910778619
    print("Real2: ", run(part=2, debug=False))  # 170147128753455
