from copy import deepcopy

FILE_NAME = "2022/input/05.txt"

DATA_TEST_STACKS = [[], ["N", "Z"], ["D", "C", "M"], ["P"]]
DATA = [
    [],
    ["S", "P", "W", "N", "J", "Z"],
    ["T", "S", "G"],
    ["H", "L", "R", "Q", "V"],
    ["D", "T", "S", "V"],
    ["J", "M", "B", "D", "T", "Z", "Q"],
    ["L", "Z", "C", "D", "J", "T", "W", "M"],
    ["J", "T", "G", "W", "M", "P", "L"],
    ["H", "Q", "F", "B", "T", "M", "G", "N"],
    ["W", "Q", "B", "P", "C", "G", "D", "R"],
]


def run(part: int, test_run: bool = False, debug: bool = False):
    if test_run:
        file = FILE_NAME.replace(".txt", "-test.txt")
        stacks = DATA_TEST_STACKS
    else:
        file = FILE_NAME
        stacks = DATA

    with open(file, encoding="utf-8") as f:
        file_data = f.readlines()

    data = [x.strip() for x in file_data]
    part_function = part1 if part == 1 else part2

    return part_function(stacks, data, debug=debug)


def part1(stacks_orig: list[list[str]], moves: list[str], debug: bool = False) -> str:
    results = ""
    stacks = deepcopy(stacks_orig)

    for move in moves:
        if debug:
            print(move)
        words = move.split()
        quantity, start, end = int(words[1]), int(words[3]), int(words[5])
        for _ in range(quantity):
            if debug:
                print(stacks)
            stacks[end].insert(0, stacks[start].pop(0))

    if debug:
        print(stacks)
    for stack in stacks:
        if len(stack) > 0:
            results += stack.pop(0)
    return results


def part2(stacks_orig: list[list[str]], moves: list[str], debug: bool = False) -> str:
    results = ""
    stacks = deepcopy(stacks_orig)

    for move in moves:
        if debug:
            print(move)
        words = move.split()
        quantity, start, end = int(words[1]), int(words[3]), int(words[5])
        move = stacks[start][:quantity]
        if debug:
            print("MOVE:", move)

        for _ in range(quantity):
            stacks[start].pop(0)

        stacks[end] = move + stacks[end]

        if debug:
            print(stacks)

    if debug:
        print(stacks)
    for stack in stacks:
        if len(stack) > 0:
            results += stack.pop(0)
    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # CMZ
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # MQTPGLLDN
    # print("Test2: ", run(part=2, test_run=True, debug=True))  # MCD
    print("Real2: ", run(part=2, test_run=False, debug=False))  # LVZPSTTCZ
