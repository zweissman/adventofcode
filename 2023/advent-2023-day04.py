from collections import defaultdict


def run(part: int, test_suffix: str = "", debug: bool = False):
    y, d = __file__.split("advent-")[1].split("-day")
    file_name = f"{y}/input/{d.strip('.py')}{test_suffix}.txt"

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def part1(data: list[str], debug: bool = False) -> int:  # pylint: disable = unused-argument
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
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 13
    # print("Real1: ", run(part=1, debug=False))  # 23441
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # 30
    print("Real2: ", run(part=2, debug=False))  # 5923918
