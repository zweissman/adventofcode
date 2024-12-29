def run(part: int, test_suffix: str = "", debug: bool = False):
    y, d = __file__.split("advent-")[1].split("-day")
    file_name = f"{y}/input/{d.strip('.py')}{test_suffix}.txt"

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def part1(data: list[str], debug: bool = False) -> int:
    results = 0
    locks = []
    keys = []

    while len(data) > 0:
        grid2 = []
        while len(data) > 0:
            line = data.pop(0)
            if line == "":
                break
            grid2.append(line)

        grid = grid_to_str(grid2)

        # Rotate 90 degrees
        grid_90 = list(zip(*grid))

        result = []
        for row in grid_90:
            result.append(row.count("#") - 1)

        if grid_90[0][0] == "#":
            if debug:
                print("lock", result)
            locks.append(result)
        else:
            if debug:
                print("key", result)
            keys.append(result)

    for lock in locks:
        for key in keys:
            max_size = 5
            combo = [x + y for x, y in zip(lock, key)]
            if max(combo) <= max_size:
                results += 1

    return results


def part2(data: list[str], debug: bool = False) -> int:  # pylint: disable=unused-argument
    results = 0

    return results


def grid_to_str(data: list[str]) -> list[list[str]]:
    grid = []
    for row in data:
        grid.append(list(row))

    return grid


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 3
    print("Real1: ", run(part=1, debug=False))  # 3249
