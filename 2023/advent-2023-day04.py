# pylint: disable=too-many-return-statements,too-many-statements,too-many-branches,duplicate-code,unused-argument
# pylint: disable=unnecessary-list-index-lookup

from collections import defaultdict

FILE_NAME = "2023/input/04.txt"


def run(part: int, test_run: bool = False, debug: bool = False):
    if test_run:
        file = FILE_NAME.replace(".txt", "-test.txt")
    else:
        file = FILE_NAME

    with open(file, encoding="utf-8") as f:
        data = f.readlines()
    part_function = part1 if part == 1 else part2

    return part_function(data, debug)


def part1(data: list[str], debug: bool = False) -> int:
    results = 0

    for line in data:
        _, rest = line.split(":")
        win, mine = rest.strip().split("|")
        win_numbers = win.strip().split(" ")
        my_numbers = mine.strip().split(" ")

        win_count = 0
        for w in win_numbers:
            if w == "":
                continue
            if w in my_numbers:
                if not win_count:
                    win_count = 1
                else:
                    win_count = win_count * 2

        results += win_count

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0

    extras: dict[int, int] = defaultdict(int)

    for line in data:
        card, rest = line.split(":")
        card_id_str = card.split(" ")[-1]
        card_id = int(card_id_str.strip())
        extras[card_id] += 1  # count the original
        win, mine = rest.strip().split("|")
        win_numbers = win.strip().split(" ")
        my_numbers = mine.strip().split(" ")

        win_count = 0
        for w in win_numbers:
            if w == "":
                continue
            if w in my_numbers:
                win_count += 1

        for z in range(win_count):
            extras[card_id + z + 1] += extras[card_id]

        if debug:
            print(extras)
            print()

    if debug:
        print([v for k, v in extras.items()])
    results = sum(v for (k, v) in extras.items())

    return results


if __name__ == "__main__":
    # final = run(part=1, test_run=False, debug=True) # 13
    # final = run(part=1, test_run=False, debug=False)  # 23441
    # final = run(part=2, test_run=True, debug=True) # 30
    final = run(part=2, test_run=False, debug=False)  # 5923918
    print("ANSWER:", final)
