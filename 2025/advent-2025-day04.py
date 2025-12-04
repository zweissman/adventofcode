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

    grid = []

    for d in data:
        d = d.strip()
        grid.append(list(d))

    show(grid, debug)

    results = find_movable_rolls(grid, debug)

    return results


def find_movable_rolls(grid: list[list[str]], remove_after: bool = False, debug: bool = False) -> int:
    results = 0
    directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    movable_positions = []

    for y, row in enumerate(grid):
        for x, current in enumerate(row):
            if current == ".":
                continue

            empty_count = 0

            for dx, dy in directions:
                if not is_inbounds(grid, (x + dx, y + dy)) or grid[y + dy][x + dx] == ".":
                    empty_count += 1

                    if empty_count >= 5:
                        results += 1
                        movable_positions.append((x, y))

                        if debug:
                            print(f"Movable roll found at ({x}, {y})")
                        break

    if remove_after:
        for x, y in movable_positions:
            grid[y][x] = "."

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    grid = []

    for d in data:
        d = d.strip()
        grid.append(list(d))

    run_count = -1

    while run_count != 0:
        show(grid, debug)
        run_count = find_movable_rolls(grid, remove_after=True, debug=debug)
        if debug:
            print(f"Run removed {run_count} movable rolls")

        results += run_count

    return results


def show(grid: list[list[str]], debug: bool = False) -> None:
    if debug:
        print()
        for y, row in enumerate(grid):
            print(f"{y:02}", "".join([str(x) for x in row]))


def is_inbounds(data: list[list[str]], node: tuple[int, int]) -> bool:
    return 0 <= node[0] < len(data[0]) and 0 <= node[1] < len(data)


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 13
    # print("Real1: ", run(part=1, debug=False))  # 1523
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # 43
    print("Real2: ", run(part=2, debug=False))  # 9290
