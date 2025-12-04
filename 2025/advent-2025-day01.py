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
    dial = 50
    show(data, debug=debug)

    for row in data:
        direction, value = row[0], int(row[1:])
        if direction == "L":
            dial -= value
        elif direction == "R":
            dial += value

        dial = dial % 100

        if dial == 0:
            results += 1

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    dial = 50

    for row in data:
        if debug:
            print(f"Dial: {dial} | Row: {row}")

        direction, value = row[0], int(row[1:])

        results += value // 100
        value = value % 100

        if direction == "L":
            if dial != 0 and dial - value <= 0:
                results += 1
                if debug:
                    print("  -> Overflow!")

            dial -= value

        elif direction == "R":
            if dial != 0 and dial + value >= 100:
                results += 1
                if debug:
                    print("  -> Overflow!")

            dial += value

        dial = dial % 100

    return results


def show(grid: list[str], debug: bool = False) -> None:
    if debug:
        print()
        for y, row in enumerate(grid):
            print(f"{y:02}", "".join([str(x) for x in row]))


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 3
    # print("Real1: ", run(part=1, debug=False))  # 1168
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # 16
    print("Real2: ", run(part=2, debug=False))  # 7199
