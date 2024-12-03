import sys

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

sys.setrecursionlimit(10000)

FILE_NAME = "2022/input/12.txt"


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


class ZGrid(Grid):
    def __init__(self, width=0, height=0, matrix=None, inverse=False):
        super().__init__(width=width, height=height, matrix=matrix, inverse=inverse)

    def walkable(self, to_x, to_y, from_x, from_y):
        return (
            self.inside(to_x, to_y)
            and self.nodes[to_y][to_x].walkable
            and self.nodes[to_y][to_x].weight - self.nodes[from_y][from_x].weight <= 1
        )

    def neighbors(self, node, diagonal_movement=DiagonalMovement.never):  # pylint: disable=unused-argument
        """
        get all neighbors of one node
        :param node: node
        """
        x = node.x
        y = node.y
        neighbors = []

        # ↑
        if self.walkable(x, y - 1, x, y):
            neighbors.append(self.nodes[y - 1][x])
        # →
        if self.walkable(x + 1, y, x, y):
            neighbors.append(self.nodes[y][x + 1])
        # ↓
        if self.walkable(x, y + 1, x, y):
            neighbors.append(self.nodes[y + 1][x])
        # ←
        if self.walkable(x - 1, y, x, y):
            neighbors.append(self.nodes[y][x - 1])

        return neighbors


def part1(data: list[str], debug: bool = False) -> int:
    current = ()
    destination = ()
    grid = []

    for row in data:
        grid.append(list(row))

    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if value == "S":
                row[x] = "a"
                current = (x, y)
            elif value == "E":
                row[x] = "z"
                destination = (x, y)
            row[x] = ord(row[x]) - ord("a") + 1

    print("Checking Start", current, "End", destination)

    grid = ZGrid(matrix=grid)

    start = grid.node(current[0], current[1])
    end = grid.node(destination[0], destination[1])

    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)

    if debug:
        print("operations:", runs, "path length:", len(path))
    if debug:
        print(grid.grid_str(path=path, start=start, end=end))

    return len(path) - 1


def part2(data: list[str], debug: bool = False) -> int:
    current = ()
    destination = ()
    starts = []
    grid = []

    for row in data:
        grid.append(list(row))

    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if value == "S":
                row[x] = "a"
            elif value == "E":
                row[x] = "z"
                destination = (x, y)
            row[x] = ord(row[x]) - ord("a") + 1
            if row[x] == 1:
                starts.append((x, y))

    shortest = 999999
    for current in starts:
        if debug:
            print("Checking Start", current, "End", destination)

        this_grid = ZGrid(matrix=grid)

        start = this_grid.node(current[0], current[1])
        end = this_grid.node(destination[0], destination[1])

        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, this_grid)

        if len(path) > 0:
            if debug:
                print("operations:", runs, "path length:", len(path) - 1)
            #           print(grid.grid_str(path=path, start=start, end=end))
            shortest = min(len(path) - 1, shortest)

    return shortest


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # 31
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 504
    # print("Test2: ", run(part=2, test_run=True, debug=True))  # 29
    print("Real2: ", run(part=2, test_run=False, debug=False))  # 500
