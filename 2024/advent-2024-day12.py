DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))


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
    grid = grid_to_str(data)
    show(grid, debug=debug)

    cell_count = len(grid) * len(grid[0])
    while True:
        all_cells = "".join(["".join(x) for x in grid])
        if all_cells.count(".") >= cell_count:
            break
        next_plot = all_cells.replace(".", "")[0]
        plot_x, plot_y = find_plot(grid, next_plot)
        if debug:
            print(f"Processing plot {next_plot} at ({plot_x},{plot_y})")
        results += get_plot_cost1(grid, plot_x, plot_y, debug)

    return results


def get_plot_cost1(grid: list[list[str]], start_x: int, start_y: int, debug: bool) -> int:
    area = 0
    perimeter = 0
    visited = set()
    to_check = set()

    to_check.add((start_x, start_y))

    while len(to_check) > 0:
        x, y = to_check.pop()
        plot = grid[y][x]
        grid[y][x] = "."
        visited.add((x, y))
        area += 1

        for direction in DIRECTIONS:
            new_x = x + direction[0]
            new_y = y + direction[1]

            if (new_x, new_y) in visited:
                continue

            if is_inbounds(grid, (new_x, new_y)):
                if grid[new_y][new_x] == plot:
                    to_check.add((new_x, new_y))
                else:
                    perimeter += 1

            else:
                perimeter += 1

    if debug:
        print(f"{area=} {perimeter=}  ={area*perimeter}")

    return area * perimeter


def find_plot(grid: list[list[str]], plot: str) -> tuple[int, int]:
    for y, row in enumerate(grid):
        if plot in row:
            x = row.index(plot)
            return (x, y)

    return (-1, -1)


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    grid = grid_to_str(data)
    show(grid, debug=debug)

    cell_count = len(grid) * len(grid[0])
    while True:
        all_cells = "".join(["".join(x) for x in grid])
        if all_cells.count(".") >= cell_count:
            break
        next_plot = all_cells.replace(".", "")[0]
        plot_x, plot_y = find_plot(grid, next_plot)
        if debug:
            print(f"Processing plot {next_plot} at ({plot_x},{plot_y})")
        results += get_plot_cost2(grid, plot_x, plot_y, debug)

    return results


def get_plot_cost2(grid: list[list[str]], start_x: int, start_y: int, debug: bool) -> int:
    area = 0
    visited = set()
    to_check = set()

    to_check.add((start_x, start_y))

    while len(to_check) > 0:
        x, y = to_check.pop()
        plot = grid[y][x]
        grid[y][x] = "."
        visited.add((x, y))
        area += 1

        for direction in DIRECTIONS:
            new_x = x + direction[0]
            new_y = y + direction[1]

            if (new_x, new_y) in visited:
                continue
            if is_inbounds(grid, (new_x, new_y)):
                if grid[new_y][new_x] == plot:
                    to_check.add((new_x, new_y))
                    continue

    sides = 0
    sorted_visited: list[tuple[int, int]] = sorted(visited)
    x_set = {x for x, _ in sorted_visited}
    y_set = {y for _, y in sorted_visited}

    for a in x_set:
        same_side = []
        for x, y in sorted_visited:
            if x == a and (x - 1, y) not in sorted_visited:
                same_side.append(y)

        if len(same_side) > 0:
            sides += 1
            for i in range(1, len(same_side)):
                if same_side[i - 1] != same_side[i] - 1:
                    sides += 1

    for a in x_set:
        same_side = []
        for x, y in sorted_visited:
            if x == a and (x + 1, y) not in sorted_visited:
                same_side.append(y)

        if len(same_side) > 0:
            sides += 1
            for i in range(1, len(same_side)):
                if same_side[i - 1] != same_side[i] - 1:
                    sides += 1

    for b in y_set:
        same_side = []
        for x, y in sorted_visited:
            if y == b and (x, y + 1) not in sorted_visited:
                same_side.append(x)

        if len(same_side) > 0:
            sides += 1
            for i in range(1, len(same_side)):
                if same_side[i - 1] != same_side[i] - 1:
                    sides += 1

    for b in y_set:
        same_side = []
        for x, y in sorted_visited:
            if y == b and (x, y - 1) not in sorted_visited:
                same_side.append(x)

        if len(same_side) > 0:
            sides += 1
            for i in range(1, len(same_side)):
                if same_side[i - 1] != same_side[i] - 1:
                    sides += 1

    if debug:
        print(f"{area=} {sides=}  ={area*sides} {sorted_visited}")

    return area * sides


def show(grid: list[list[str]], debug: bool = False) -> None:
    if debug:
        print()
        for y, row in enumerate(grid):
            print(y, "".join([str(x) for x in row]))


def is_inbounds(data: list[list[str]], node: tuple[int, int]) -> bool:
    return 0 <= node[0] < len(data[0]) and 0 <= node[1] < len(data)


def grid_to_str(data: list[str]) -> list[list[str]]:
    grid = []
    for row in data:
        grid.append(list(row))

    return grid


if __name__ == "__main__":
    # print("Test1a: ", run(part=1, test_suffix="-test-a", debug=True))  # 140
    # print("Test1b: ", run(part=1, test_suffix="-test-b", debug=True))  # 772
    # print("Test1c: ", run(part=1, test_suffix="-test-c", debug=True))  # 1930
    # print("Real1: ", run(part=1, debug=False))  # 1467094

    # print("Test2a: ", run(part=2, test_suffix="-test-a", debug=True))  # 80
    # print("Test2b: ", run(part=2, test_suffix="-test-b", debug=True))  # 436
    # print("Test2d: ", run(part=2, test_suffix="-test2d", debug=True))  # 236
    # print("Test2e: ", run(part=2, test_suffix="-test2e", debug=True))  # 368
    # print("Test2c: ", run(part=2, test_suffix="-test-c", debug=True))  # 1206
    print("Real2: ", run(part=2, debug=False))  # 881182
