def run(part: int, test_suffix: str = "", debug: bool = False):  # pylint: disable=duplicate-code
    file = "2023/input/01.txt"

    if test_suffix:
        file = file.replace(".txt", test_suffix + ".txt")

    with open(file, encoding="utf-8") as f:
        file_data = f.readlines()

    data = [x.strip() for x in file_data]
    part_function = part1 if part == 1 else part2

    return part_function(data, debug)


def part1(data: list[str], debug: bool = False) -> int:  # pylint: disable=unused-argument
    results = 0

    for line in data:
        start, end = None, None
        for letter in line:
            if letter.isnumeric():
                start = letter
                break

        for letter in reversed(line):
            if letter.isnumeric():
                end = letter
                break

        results += int(f"{start}{end}")

    return results


def part2(data: list[str], debug: bool = False) -> int:  # pylint: disable=unused-argument
    results = 0

    for line in data:
        start, end = None, None
        start_line, end_line = line, line

        while not start:
            start_line = replace_words(start_line, reverse=False)
            letter = start_line[:1]
            if letter.isnumeric():
                start = letter
                break

            start_line = start_line[1:]

        while not end:
            end_line = replace_words(end_line, reverse=True)
            letter = end_line[-1:]
            if letter.isnumeric():
                end = letter
                break

            end_line = end_line[:-1]

        results += int(f"{start}{end}")

    return results


def replace_words(line: str, reverse: bool = False) -> str:
    func = line.endswith if reverse else line.startswith
    rep = -1 if reverse else 1

    digits = [
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
    ]

    for key, value in digits:
        if func(key):
            return line.replace(key, value, rep)

    return line


if __name__ == "__main__":
    print("Test1: ", run(part=1, test_suffix="-test1", debug=True))  # 142
    print("Real1: ", run(part=1, debug=False))  # 54597
    print("Test2: ", run(part=2, test_suffix="-test2", debug=True))  # 281
    print("Real2: ", run(part=2, debug=False))  # 54504
