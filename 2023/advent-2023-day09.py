def run(part: int, test_run: bool = False, debug: bool = False):
    file_name = "2023/input/09.txt"
    if test_run:
        file_name = file_name.replace(".txt", "-test.txt")

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data]
    part_function = part1 if part == 1 else part2

    return part_function(data, debug)


def part1(data: list[str], debug: bool = False) -> int:
    results = 0

    for line in data:
        numbers = [int(x) for x in line.split(" ")]
        sequence = [numbers]

        if debug:
            print()
            print(sequence)

        while sum(sequence[-1]) != 0:
            new_sequence = []
            for i in range(len(sequence[-1]) - 1):
                new_sequence.append(sequence[-1][i + 1] - sequence[-1][i])
            if debug:
                print(new_sequence)
            sequence.append(new_sequence)

        if debug:
            print("last numbers")
        for i in range(len(sequence) - 1, 0, -1):
            last_number = sequence[i][-1]

            if debug:
                print(last_number)

            sequence[i - 1].append(last_number + sequence[i - 1][-1])
            if debug:
                print(sequence[i - 1])

        results += sequence[0][-1]

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0

    for line in data:
        numbers = [int(x) for x in line.split(" ")]
        sequence = [numbers]

        if debug:
            print()
            print(sequence)

        while sum(sequence[-1]) != 0:
            new_sequence = []
            for i in range(len(sequence[-1]) - 1):
                new_sequence.append(sequence[-1][i + 1] - sequence[-1][i])
            if debug:
                print(new_sequence)
            sequence.append(new_sequence)

        if debug:
            print("first numbers")
        for i in range(len(sequence) - 1, 0, -1):
            first_number = sequence[i][0]

            if debug:
                print(first_number)

            sequence[i - 1].insert(0, sequence[i - 1][0] - first_number)
            if debug:
                print(sequence[i - 1])

        results += sequence[0][0]

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # 114
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 1798691765
    # print("Test2: ", run(part=2, test_run=True, debug=True))  # 2
    print("Real2: ", run(part=2, test_run=False, debug=False))  # 1104
