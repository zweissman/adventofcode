def run(part: int, test_run: bool = False, debug: bool = False):
    file_name = "2023/input/21.txt"
    if test_run:
        file_name = file_name.replace(".txt", "-test.txt")
        steps = 6
    else:
        steps = 64

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip().replace("S", "O") for x in file_data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, steps=steps, debug=debug)


def show(grid: list[str], step: int, debug: bool = False) -> None:
    if debug:
        print()
        print("Step", step + 1)
        for _, row in enumerate(grid):
            print("".join([str(x) for x in row]))
        print("Score: ", get_score(grid))


def get_score(grid: list[str]) -> int:
    results = 0

    for _, row in enumerate(grid):
        results += row.count("O")

    return results


def part1(data: list[str], steps: int, debug: bool = False) -> int:
    step = 0

    for step in range(steps):
        show(data, step, debug)
        run_step(data, step, debug)

    return get_score(data)


def run_step(data: list[str], steps: int, debug: bool = False) -> None:  # pylint: disable=unused-argument
    pass


def part2(data: list[str], steps: int, debug: bool = False) -> int:  # pylint: disable=unused-argument
    results = 0

    return results


# def find_start(grid: list[list[str]]) -> tuple[int, int]:
#     for y, row in enumerate(grid):
#         x = row.find("S")
#         if x != -1:
#             return (x, y)

#     return (-1, -1)

if __name__ == "__main__":
    # TODO
    print("Test1: ", run(part=1, test_run=True, debug=True))  #
    # print("Real1: ", run(part=1, test_run=False, debug=False))  #
    # print("Test2: ", run(part=2, test_run=True, debug=True))  #
    # print("Real2: ", run(part=2, test_run=False, debug=False))  #
