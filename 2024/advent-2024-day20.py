from collections import deque


def run(part: int, test_suffix: str = "", debug: bool = False):
    y, d = __file__.split("advent-")[1].split("-day")
    file_name = f"{y}/input/{d.strip('.py')}{test_suffix}.txt"

    if test_suffix == "":
        min_save = 100
    else:
        if part == 1:
            min_save = 1
        else:
            min_save = 50
    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, min_save=min_save, debug=debug)


def part1(data: list[str], min_save, debug: bool = False) -> int:
    grid = grid_to_str(data)
    start = find_in_grid(grid, "S")
    end = find_in_grid(grid, "E")
    grid[start[1]][start[0]] = "."
    grid[end[1]][end[0]] = "."

    distances, path = get_pathfinder_distances(grid, start)
    clean_time = distances[end[1]][end[0]]

    if debug:
        print(start, end, clean_time)

    combos = set()

    walls = 2

    for x, y in path:
        cell_grid = grid[y][x]
        cell_distances = distances[y][x]
        if cell_grid != "." or cell_distances == -1:
            continue

        for x2, y2 in path:
            distance = abs(y2 - y) + abs(x2 - x)
            if distance > walls:
                # too far
                continue
            cell_distances2 = distances[y2][x2]
            cost_savings = abs(cell_distances2 - cell_distances) - distance
            if cost_savings >= min_save:
                combos.add(((x, y), (x2, y2)))
                if debug:
                    print((x, y), (x2, y2), cost_savings)

    return len(combos) // 2


def part2(data: list[str], min_save, debug: bool = False) -> int:
    grid = grid_to_str(data)
    start = find_in_grid(grid, "S")
    end = find_in_grid(grid, "E")
    grid[start[1]][start[0]] = "."
    grid[end[1]][end[0]] = "."

    distances, path = get_pathfinder_distances(grid, start)
    clean_time = distances[end[1]][end[0]]

    if debug:
        print(start, end, clean_time)

    combos = set()

    walls = 20

    for x, y in path:
        cell_grid = grid[y][x]
        cell_distances = distances[y][x]
        if cell_grid != "." or cell_distances == -1:
            continue

        for x2, y2 in path:
            distance = abs(y2 - y) + abs(x2 - x)
            if distance > walls:
                # too far
                continue
            cell_distances2 = distances[y2][x2]
            cost_savings = abs(cell_distances2 - cell_distances) - distance
            if cost_savings >= min_save:
                combos.add(((x, y), (x2, y2)))
                if debug:
                    print((x, y), (x2, y2), cost_savings)

    return len(combos) // 2


def show(grid: list[list[str]], debug: bool = False) -> None:
    if debug:
        print()
        for y, row in enumerate(grid):
            print(f"{y:02}", "".join([str(x) for x in row]))


def is_inbounds(data: list[list[str]], node: tuple[int, int]) -> bool:
    return 0 <= node[0] < len(data[0]) and 0 <= node[1] < len(data)


def grid_to_str(data: list[str]) -> list[list[str]]:
    grid = []
    for row in data:
        grid.append(list(row))

    return grid


def find_in_grid(grid: list[list[str]], character: str) -> tuple[int, int]:
    for y, row in enumerate(grid):
        try:
            x = row.index(character)
        except ValueError:
            x = -1

        if x != -1:
            return (x, y)

    return (-1, -1)


def get_pathfinder_distances(
    grid: list[list[str]], start: tuple[int, int]
) -> tuple[list[list[int]], list[tuple[int, int]]]:
    start_x, start_y = start

    q: deque[tuple[int, int]] = deque()
    q.append((start_x, start_y))

    path = [(start_x, start_y)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    distances = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    distances[start_y][start_x] = 0

    while q:
        p = q.popleft()

        for i in range(4):
            x = p[0] + dx[i]
            y = p[1] + dy[i]
            if is_inbounds(grid, (x, y)) and distances[y][x] == -1:
                if grid[y][x] == ".":
                    distances[y][x] = distances[p[1]][p[0]] + 1
                    q.append((x, y))
                    path.append((x, y))

    return distances, path


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 44
    # TODO: Slow
    # print("Real1: ", run(part=1, debug=False))  # 1332
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # 285
    # TODO: Slow
    print("Real2: ", run(part=2, debug=False))  # 987695
