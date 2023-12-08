# pylint: disable=too-many-return-statements,too-many-statements,too-many-branches,duplicate-code,unused-argument
# pylint: disable=unnecessary-list-index-lookup, E701

FILE_NAME = "2023/input/08.txt"

import itertools
import math

def run(part: int, test_run: bool = False, debug: bool = False):
    if test_run:
        file = FILE_NAME.replace(".txt", "-test.txt")
    else:
        file = FILE_NAME

    with open(file, encoding="utf-8") as f:
        data = f.readlines()

    data = [x.strip() for x in data]
    part_function = part1 if part == 1 else part2

    return part_function(data, debug)


def part1(data: list[str], debug: bool = False) -> int:
    results = 0

    directions = list(data.pop(0))
    data.pop(0)
    nodes = {}

    for line in data:
        node, options = line.split(" = ")
        options = options.replace("(", "").replace(")", "").split(", ")
        nodes[node] = (options[0], options[1])


    path = "AAA"

    get_direction = get_next_direction(directions)
    while path != "ZZZ":
        direction = next(get_direction)
        if debug: print(f"Direction: {direction}")
        if direction == "L":
            path = nodes[path][0]
        else:
            path = nodes[path][1]
        if debug: print (f"Path: {path}")
        results += 1


    return results

def get_next_direction(directions):
    for c in itertools.cycle(directions):
        yield c

def part2(data: list[str], debug: bool = False) -> int:
    directions = list(data.pop(0))
    data.pop(0)

    nodes = {}
    result_list = []

    for line in data:
        node, options = line.split(" = ")
        options = options.replace("(", "").replace(")", "").split(", ")
        nodes[node] = (options[0], options[1])

    if debug: print(nodes.keys())

    for start_path in [node for node in nodes.keys() if node.endswith("A")]:
        if debug: print (f"Start Path: {start_path}")
        results = 0

    
        get_direction = get_next_direction(directions)

        path = start_path

        while not path.endswith("Z"):
            direction = next(get_direction)
            if debug: print(f"Direction: {direction}")
            if direction == "L":
                path = nodes[path][0]
            else:
                path = nodes[path][1]
            if debug: print (f"Path: {path}")
            results += 1

        result_list.append(results)


    if debug: print(result_list)

    return math.lcm(*result_list)




if __name__ == "__main__":
    #final = run(part=1, test_run=True, debug=True)  # 6
    #final = run(part=1, test_run=False, debug=False)  # 12361
    #final = run(part=2, test_run=True, debug=True) # 6
    final = run(part=2, test_run=False, debug=False)  # 18215611419223
    print("ANSWER:", final)
