# pylint: disable=too-many-return-statements,too-many-statements,too-many-branches,duplicate-code,unused-argument
# pylint: disable=unnecessary-list-index-lookup

# import sys
# sys.setrecursionlimit(15000)


FILE_NAME = "2023/input/17.txt"


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


def show(grid: list[list[str]], debug: bool = False):
    if debug:
        print()
        for y in range(len(grid)):
            print("".join([str(x) for x in grid[y]]))


def part1(data: list[str], debug: bool = False) -> int:
    grid = []

    for line in data:
        line = line.strip()
        if not line.startswith("#"):
            grid.append(list(line))

    show(grid, debug)

    import heapq

    g = [[int(j) for j in row] for row in grid]

    q = [(0, 0, 0, -1, 0)]
    seen = set()
    while q:
        cost, x, y, dir, mult = heapq.heappop(q)

        key = (x, y, dir, mult)
        if key in seen:
            continue
        seen.add(key)

        if x == len(g[0]) - 1 and y == len(g) - 1:
            return cost

        for d in range(4):
            if d == dir and mult == 3:
                continue

            if d != dir and d // 2 == dir // 2:
                continue

            nx = x - (d == 0) + (d == 1)
            ny = y - (d == 2) + (d == 3)

            if nx < 0 or nx >= len(g[0]) or ny < 0 or ny >= len(g):
                continue

            heapq.heappush(q, (cost + g[ny][nx], nx, ny, d, mult * (d == dir) + 1))
    return cost


def part2(data: list[str], debug: bool = False) -> int:
    grid = []

    for line in data:
        line = line.strip()
        if not line.startswith("#"):
            grid.append(list(line))

    show(grid, debug)

    import heapq

    g = [[int(j) for j in row] for row in grid]

    q = [(0, 0, 0, 1, 0)]
    seen = set()
    while q:
        cost, x, y, dir, mult = heapq.heappop(q)

        key = (x, y, dir, mult)
        if key in seen:
            continue
        seen.add(key)

        if x == len(g[0]) - 1 and y == len(g) - 1:
            return cost

        for d in range(4):
            if d != dir and mult < 4:
                continue
            if d == dir and mult == 10:
                continue

            if d != dir and d // 2 == dir // 2:
                continue

            nx = x - (d == 0) + (d == 1)
            ny = y - (d == 2) + (d == 3)

            if nx < 0 or nx >= len(g[0]) or ny < 0 or ny >= len(g):
                continue

            heapq.heappush(q, (cost + g[ny][nx], nx, ny, d, mult * (d == dir) + 1))

    return cost


if __name__ == "__main__":
    print("Test1: ", run(part=1, test_run=True, debug=True))  # 102
    # print("Real1: ", run(part=1, test_run=False, debug=False))  #  916
    # print("Test2: ", run(part=2, test_run=True, debug=True)) # 94
    # print("Real2: ", run(part=2, test_run=False, debug=False))  # 1064 too low
