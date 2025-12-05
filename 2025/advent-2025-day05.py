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

    ranges: list[tuple[int, int]] = []
    ids: list[int] = []

    for row in data:
        if "-" in row:
            start, end = row.split("-")
            ranges.append((int(start), int(end)))
        elif row != "":
            ids.append(int(row))

    if debug:
        print("Ranges:", ranges)
        print("IDs:", ids)

    ranges = reduce_ranges(ranges, debug=debug)

    for id_ in ids:
        for range_ in ranges:
            if range_[0] <= id_ <= range_[1]:
                results += 1
                break

    return results


def reduce_ranges(ranges: list[tuple[int, int]], debug: bool = False) -> list[tuple[int, int]]:
    if debug:
        print("Reducing ranges:", ranges)
    # Sort ranges by start value
    ranges.sort(key=lambda x: x[0])
    reduced = []
    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= current_end + 1:  # Overlapping or contiguous ranges
            current_end = max(current_end, end)
        else:
            reduced.append((current_start, current_end))
            current_start, current_end = start, end

    reduced.append((current_start, current_end))  # Add the last range

    if debug:
        print("Reduced ranges:", reduced)

    return reduced


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    show(data, debug=debug)

    ranges: list[tuple[int, int]] = []
    ids: list[int] = []

    for row in data:
        if "-" in row:
            start, end = row.split("-")
            ranges.append((int(start), int(end)))
        elif row != "":
            ids.append(int(row))

    if debug:
        print("Ranges:", ranges)
        print("IDs:", ids)

    ranges = reduce_ranges(ranges, debug=debug)

    for range_ in ranges:
        results += range_[1] - range_[0] + 1

    return results


def show(grid: list[str], debug: bool = False) -> None:
    if debug:
        print()
        for y, row in enumerate(grid):
            print(f"{y:02}", "".join([str(x) for x in row]))


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 3
    # print("Real1: ", run(part=1, debug=False))  # 782
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # 14
    print("Real2: ", run(part=2, debug=False))  # 353863745078671
