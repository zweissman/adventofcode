def run(part: int, test_run: bool = False, debug: bool = False):
    file_name = "2023/input/17.txt"
    if test_run:
        file_name = file_name.replace(".txt", "-test.txt")

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def show(grid: list[list[str]], debug: bool = False):
    if debug:
        print()
        for y in range(len(grid)):
            print("".join([str(x) for x in grid[y]]))


class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def a_star_algorithm(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = {start_node}
        closed_list = set()

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n is None or g[v] < g[n]:
                    n = v

            if n is None:
                return None

            # if the current node is the stop_node
            # then we begin reconstruction the path from it to the start_node
            if n == stop_node:
                reconstruction_path = []

                while parents[n] != n:
                    reconstruction_path.append(n)
                    n = parents[n]

                reconstruction_path.append(start_node)

                reconstruction_path.reverse()

                return reconstruction_path

            # for all neighbors of the current node do
            for m, weight in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as its parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        return None


def part1(data: list[str], debug: bool = False) -> int:
    grid = []

    for d in data:
        d = d.strip()
        if not d.startswith("#"):
            grid.append(list(d))

    show(grid, debug)

    adjacency_list = {}

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            adjacency_list[(x, y)] = get_neighbors(grid, x, y)

    graph1 = Graph(adjacency_list)
    path = graph1.a_star_algorithm((0, 0), (len(grid[0]) - 1, len(grid) - 1))

    results = show_path(grid, path, debug)
    return results


def part2(data: list[str], debug: bool = False) -> int:  # pylint: disable = unused-argument
    results = 0
    grid = []

    if debug:
        show(grid, debug)

    return results


def show_path(original_grid, path, debug):
    results = 0
    grid = [row[:] for row in original_grid]
    for x, y in path:
        results += int(grid[y][x])
        grid[y][x] = "#"

    show(grid, debug)

    return results


def get_neighbors(grid, x, y):
    neighbors = []
    if x > 0:
        neighbors.append(((x - 1, y), int(grid[y][x - 1])))
    if y > 0:
        neighbors.append(((x, y - 1), int(grid[y - 1][x])))
    if x < len(grid[0]) - 1:
        neighbors.append(((x + 1, y), int(grid[y][x + 1])))
    if y < len(grid) - 1:
        neighbors.append(((x, y + 1), int(grid[y + 1][x])))

    return neighbors


if __name__ == "__main__":
    print("Test1: ", run(part=1, test_run=True, debug=True))  #
    # print("Real1: ", run(part=1, test_run=False, debug=False))  #
    # print("Test2: ", run(part=2, test_run=True, debug=True)) #
    # print("Real2: ", run(part=2, test_run=False, debug=False))  #
