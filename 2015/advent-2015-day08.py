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

    literal_results, memory_results = 0, 0

    for row in data:
        literal, memory, _ = get_lengths(row)
        literal_results += literal
        memory_results += memory

    results = literal_results - memory_results

    return results


def get_lengths(row: str) -> tuple[int, int, int]:
    literal = len(row)
    decoded = 0
    encoded = 6  # for original escaped quotes and string quotes

    # confirm that it starts and ends with a quote and trim them
    assert row[0] == '"'
    assert row[-1] == '"'
    row = row[1:-1]
    i = 0

    while i < len(row):
        x = row[i]

        if x == "\\":
            if row[i + 1] == '"':
                i += 1
                encoded += 3
            elif row[i + 1] == "\\":
                i += 1
                encoded += 3
            elif row[i + 1] == "x":
                i += 3
                encoded += 4

        decoded += 1
        encoded += 1

        i += 1

    return literal, decoded, encoded


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    show(data, debug=debug)

    literal_results, encoded_results = 0, 0

    for row in data:
        literal, _, encoded = get_lengths(row)
        literal_results += literal
        encoded_results += encoded

    results = encoded_results - literal_results

    return results


def show(grid: list[str], debug: bool = False) -> None:
    if debug:
        print()
        for y, row in enumerate(grid):
            print(f"{y:02}", "".join([str(x) for x in row]))


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 12
    # print("Real1: ", run(part=1, debug=False))  # 1371
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # 19
    print("Real2: ", run(part=2, debug=False))  # 2117
