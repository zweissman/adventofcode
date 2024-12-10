FILE_NAME = "2023/input/06.txt"


def run(part: int, test_suffix: str = "", debug: bool = False):
    if part == 1:
        if test_suffix != "":
            data = [(7, 9), (15, 40), (30, 200)]
        else:
            data = [(45, 305), (97, 1062), (72, 1110), (95, 1695)]
    else:
        if test_suffix != "":
            data = [(71530, 940200)]
        else:
            data = [(45977295, 305106211101695)]

    part_function = part1 if part == 1 else part2

    return part_function(data, debug)


def part1(data: list[tuple[int, int]], debug: bool = False) -> int:
    results = 0

    for time, distance in data:
        win_count = 0
        if debug:
            print(time, distance)
        for i in range(1, time):
            if (time - i) * i > distance:
                win_count += 1
            elif win_count > 0:
                break
        print(win_count)
        if results == 0:
            results = win_count
        else:
            results *= win_count

    return results


def part2(data: list[tuple[int, int]], debug: bool = False) -> int:
    results = 0

    for time, distance in data:
        win_count = 0
        if debug:
            print(time, distance)

        for i in range(1, time):
            if (time - i) * i > distance:
                win_count += 1
            elif win_count > 0:
                break

        if debug:
            print(win_count)

        if results == 0:
            results = win_count
        else:
            results *= win_count

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 288
    # print("Real1: ", run(part=1, debug=False))  # 2612736
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # 71503
    print("Real2: ", run(part=2, debug=False))  # 29891250
