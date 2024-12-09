from collections import defaultdict
from itertools import combinations


def run(part: int, test_run: bool = False, debug: bool = False) -> int:
    file_name = "2024/input/08.txt"
    if test_run:
        file_name = file_name.replace(".txt", "-test.txt")

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(grid=data, debug=debug)


def part1(grid: list[str], debug: bool = False) -> int:
    frequencies = find_frequencies(grid)
    if debug:
        print(frequencies)

    nodes = find_nodes1(grid, frequencies, debug)
    if debug:
        print(nodes)

    return len(nodes)


def part2(grid: list[str], debug: bool = False) -> int:
    frequencies = find_frequencies(grid)
    if debug:
        print(frequencies)

    nodes = find_nodes2(grid, frequencies, debug)
    if debug:
        print(nodes)

    return len(nodes)


def find_frequencies(grid: list[str]) -> dict[str, list[tuple[int, int]]]:
    frequencies = defaultdict(list)

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == ".":
                continue

            frequencies[cell].append((x, y))

    return frequencies


def find_nodes1(
    data: list[str], frequencies: dict[str, list[tuple[int, int]]], debug: bool
) -> set[tuple[int, int]]:
    nodes = set()

    for frequency, antennas in frequencies.items():
        combos = list(combinations(antennas, 2))
        if debug:
            print(f"\nCombos for {frequency}")

        for combo in combos:
            first, second = combo[0], combo[1]
            dx = first[0] - second[0]
            dy = first[1] - second[1]
            if debug:
                print(first, second, ":", (dx, dy))

            first = first[0] + dx, first[1] + dy

            if is_inbounds(data, first):
                nodes.add(first)
                if debug:
                    print(f"Adding node1: {first}")
            else:
                if debug:
                    print(f"Skipping out of bounds node1: {first}")

            second = second[0] - dx, second[1] - dy

            if is_inbounds(data, second):
                nodes.add(second)
                if debug:
                    print(f"Adding node2: {second}")
            else:
                if debug:
                    print(f"Skipping out of bounds node2: {second}")

    return nodes


def find_nodes2(
    data: list[str], frequencies: dict[str, list[tuple[int, int]]], debug: bool
) -> set[tuple[int, int]]:
    nodes = set()

    for frequency, antennas in frequencies.items():
        combos = list(combinations(antennas, 2))
        if debug:
            print(f"\nCombos for {frequency}")

        for combo in combos:
            first, second = combo[0], combo[1]
            nodes.add(first)
            nodes.add(second)

            dx = first[0] - second[0]
            dy = first[1] - second[1]
            if debug:
                print(first, second, ":", (dx, dy))

            while True:
                first = first[0] + dx, first[1] + dy

                if is_inbounds(data, first):
                    nodes.add(first)
                    if debug:
                        print(f"Adding node1: {first}")
                else:
                    if debug:
                        print(f"Skipping out of bounds node1: {first}")
                    break

            while True:
                second = second[0] - dx, second[1] - dy
                if is_inbounds(data, second):
                    nodes.add(second)
                    if debug:
                        print(f"Adding node2: {second}")
                else:
                    if debug:
                        print(f"Skipping out of bounds node2: {second}")
                    break

    return nodes


def is_inbounds(data: list[str], node: tuple[int, int]) -> bool:
    return 0 <= node[0] < len(data[0]) and 0 <= node[1] < len(data)


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # 14
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 273
    # print("Test2: ", run(part=2, test_run=True, debug=True))  # 34
    print("Real2: ", run(part=2, test_run=False, debug=False))  # 1017
