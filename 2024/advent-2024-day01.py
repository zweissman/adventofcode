def run(part: int, test_suffix: str = "", debug: bool = False):  # pylint: disable=duplicate-code
    y, d = __file__.split("advent-")[1].split("-day")
    file_name = f"{y}/input/{d.strip('.py')}{test_suffix}.txt"

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def part1(data: list[str], debug: bool = False) -> int:
    results = 0

    list1 = []
    list2 = []

    for d in data:
        if debug:
            print(d)
        a, b = d.split("  ")
        list1.append(int(a.strip()))
        list2.append(int(b.strip()))

    list1 = sorted(list1)
    list2 = sorted(list2)

    for i, value in enumerate(list1):
        results += abs(value - list2[i])

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0

    list1 = []
    list2 = []

    for d in data:
        if debug:
            print(d)
        a, b = d.split("  ")
        list1.append(int(a.strip()))
        list2.append(int(b.strip()))

    for x in list1:
        results += x * list2.count(x)

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True)) # 11
    # print("Real1: ", run(part=1, debug=False)) # 1222801
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True)) # 31
    print("Real2: ", run(part=2, debug=False))  # 22545250
