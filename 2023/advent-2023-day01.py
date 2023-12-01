FILE_NAME = "2023/input/01.txt"


def run(part: int, test_run: bool = False, debug: bool = False):  # pylint: disable=duplicate-code
    if test_run:
        file = FILE_NAME.replace(".txt", "-test.txt")
    else:
        file = FILE_NAME

    with open(file, encoding="utf-8") as f:
        data = f.read()
    part_function = part1 if part == 1 else part2

    return part_function(data, debug)


def part1(data: str, debug: bool = False) -> int:  # pylint: disable=duplicate-code, unused-argument
    results = 0

    for line in data.split():
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


def part2(data: str, debug: bool = False) -> int:  # pylint: disable=duplicate-code, unused-argument
    results = 0

    for line in data.split():
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
    final = run(part=2, test_run=False, debug=True)
    print("ANSWER:", final)
