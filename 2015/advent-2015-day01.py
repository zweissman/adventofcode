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

    for line in data:
        result = line.count("(") - line.count(")")
        results += result
        if debug:
            print(result, line)

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    for line in data:
        floor = 0
        for i, c in enumerate(line):
            if c == "(":
                floor += 1
            else:
                floor += -1

            if floor < 0:
                results = i + 1
                if debug:
                    print(line, results)
                break

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 0
    # print("Real1: ", run(part=1, debug=False))  # 74
    print("Real2: ", run(part=2, debug=False))  # 1795
