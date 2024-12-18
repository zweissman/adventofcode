from collections import deque


def run(part: int, test_suffix: str = "", debug: bool = False):
    y, d = __file__.split("advent-")[1].split("-day")
    file_name = f"{y}/input/{d.strip('.py')}{test_suffix}.txt"
    if test_suffix != "":
        width, height = 7, 7
        end = (7, 7)
        steps = 12
    else:
        width, height = 71, 71
        end = (71, 71)
        steps = 1024

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    grid = [["." for _ in range(width)] for _ in range(height)]

    return part_function(data=data, grid=grid, end=end, steps=steps, debug=debug)


def part1(data: list[str], grid, end, steps, debug: bool = False) -> int:
    results = 0
    #    show(data, debug=debug)

    load_grid(grid, data[:steps])

    show(grid, debug)
    results = pathfinder(grid, (0, 0), end)

    return results


def load_grid(grid: list[list[str]], data: list[str]) -> None:
    for line in data:
        x, y = (int(a) for a in line.split(","))
        grid[y][x] = "#"


def pathfinder(grid: list[list[str]], start: tuple[int, int], end: tuple[int, int]) -> int:
    start_x, start_y = start
    end_x, end_y = end

    if grid[start_y][start_x] == "#" or grid[end_y - 1][end_x - 1] == "#":
        return -1

    q: deque[tuple[int, int]] = deque()
    q.append((start_x, start_y))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    distances = [[-1 for _ in range(end_x)] for _ in range(end_y)]

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

    return distances[end_y - 1][end_x - 1]


def part2(data: list[str], grid, end, steps, debug: bool = False) -> str:
    results = ""

    load_grid(grid, data[:steps])

    show(grid, debug)

    count = pathfinder(grid, (0, 0), end)
    if count == -1:
        print("The steps are set too far")

    for i in range(steps, len(data)):
        x, y = (int(a) for a in data[i].split(","))
        grid[y][x] = "#"
        show(grid, debug)
        count = pathfinder(grid, (0, 0), end)
        if count == -1:
            return f"{x},{y}"

    return results


def show(grid: list[str], debug: bool = False) -> None:
    if debug:
        print()
        for y, row in enumerate(grid):
            print(f"{y:02}", "".join([str(x) for x in row]))


def is_inbounds(data: list[list[str]], node: tuple[int, int]) -> bool:
    return 0 <= node[0] < len(data[0]) and 0 <= node[1] < len(data)


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 22
    # print("Real1: ", run(part=1, debug=False))  # 336
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # 6,1
    print("Real2: ", run(part=2, debug=False))  # 24,30
