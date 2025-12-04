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
    score: set[int] = set()
    show(data, debug=debug)

    for pair in data[0].split(","):
        low, high = map(int, pair.split("-"))

        if debug:
            print(low, high)

        score = score | get_funny_score(low, high, debug=debug)

    results = sum(score)
    return results


def get_funny_score(low: int, high: int, silly_times: int = 2, debug: bool = False) -> set[int]:
    score: set[int] = set()

    # If len(low) is not evenly divisible by silly_times, increment to the the next size. ex: 555 -> 1000
    while len(str(low)) % silly_times != 0:
        low = int("1" + "0" * len(str(low)))

    # If len(high) is not evenly divisible by silly_times, decrement to the the previous size. ex: 555 -> 99
    while len(str(high)) % silly_times != 0:
        high = int("9" * (len(str(high)) - 1))

    if low > high:
        # if debug:
        #     print("There is no valid range:", low, high)
        return score

    assert len(str(low)) % silly_times == 0
    assert len(str(high)) % silly_times == 0

    while len(str(low)) != len(str(high)):
        # break down the sets so that we can call this function for equal length ranges
        temp_high = int("9" * len(str(low)))
        score = score.union(get_funny_score(low, temp_high, silly_times=silly_times, debug=debug))
        low = int("1" + "0" * (len(str(temp_high)) + silly_times - 1))

    if debug:
        print("working on", low, high)

    assert len(str(low)) == len(str(high))

    silly_length = len(str(low)) // silly_times
    silly_start = int(str(low)[:silly_length])
    silly_end = int(str(high)[:silly_length])

    for x in range(silly_start, silly_end + 1):
        silly = int(str(x) * silly_times)
        if low <= silly <= high:
            score.add(silly)
            if debug:
                print("\tFound silly:", silly)

    return score


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    score: set[int] = set()
    show(data, debug=debug)

    for pair in data[0].split(","):
        low, high = map(int, pair.split("-"))

        for silly_times in range(2, len(str(high)) + 1):
            if debug:
                print(low, high, "-->", silly_times)
            score = score | get_funny_score(low, high, silly_times=silly_times, debug=debug)

    results = sum(score)
    return results


def show(grid: list[str], debug: bool = False) -> None:
    if debug:
        print()
        for y, row in enumerate(grid):
            print(f"{y:02}", "".join([str(x) for x in row]))


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 1227775554
    # print("Real1: ", run(part=1, debug=False))  # 30323879646
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # 4174379265
    print("Real2: ", run(part=2, debug=False))  # 43872163557
