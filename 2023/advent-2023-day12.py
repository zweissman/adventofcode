# pylint: disable=too-many-return-statements,too-many-statements,too-many-branches,duplicate-code,unused-argument
# pylint: disable=unnecessary-list-index-lookup

from itertools import product

FILE_NAME = "2023/input/12.txt"


def run(part: int, test_run: bool = False, debug: bool = False):
    if test_run:
        file = FILE_NAME.replace(".txt", "-test.txt")
    else:
        file = FILE_NAME

    with open(file, encoding="utf-8") as f:
        data = f.readlines()

    data = [x.strip() for x in data]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def part1(data: list[str], debug: bool = False) -> int:
    results = 0
    for line in data:
        if line.startswith("//"):
            continue

        springs, values = line.split(" ")
        springs = springs.replace(".", " ")

        result = get_variation_count(springs, values)
        if debug:
            print(springs, values, result)
        results += result

    return results


def get_variation_count(springs: str, values: str) -> int:
    variations = []
    for spring in product(" #", repeat=springs.count("?")):
        variations.append("".join(spring))

    results = []
    for variation in variations:
        result = get_valid_count(merge_run(springs, str(variation)), values)
        results.append(result)

    return sum(results)


def get_valid_count(springs: str, values: str) -> int:
    spring_groups = springs.split()
    run_lengths = []
    for springs in spring_groups:
        run_lengths.append(str(len(springs)))

    return ",".join(run_lengths) == values


def merge_run(springs: str, subs: str) -> str:
    assert springs.count("?") == len(subs)

    for c in subs:
        springs = springs.replace("?", c, 1)

    return springs


def part2(data: list[str], debug: bool = False) -> int:
    results = 0

    grid = []

    for d in data:
        d = d.strip()
        grid.append(list(d))

    return results


if __name__ == "__main__":
    import time  # qa: ignore:E402

    start_time = time.time()

    print("Test1: ", run(part=1, test_run=True, debug=True))  # 21
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 6949
    # print("Test2: ", run(part=2, test_run=True, debug=True)) #
    # print("Real2: ", run(part=2, test_run=False, debug=False))  #

    print(time.time() - start_time)
