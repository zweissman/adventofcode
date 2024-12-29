"""
--- Day 6: Probably a Fire Hazard ---
Because your neighbors keep defeating you in the holiday house decorating contest year after year,
you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to
display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at
0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle
various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners
of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in
a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions
Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on,
and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
After following the instructions, how many lights are lit?
"""


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
    grid = [[0] * 1000 for _ in range(1000)]

    for line in data:
        if line.startswith("turn"):
            line = line.lstrip("turn ")
            if line.startswith("on"):
                line = line.lstrip("on ")
                change = 1
            elif line.startswith("off"):
                line = line.lstrip("off ")
                change = 0
            else:
                raise Exception("Not sure what to do with: ", line)
        elif line.startswith("toggle"):
            line = line.lstrip("toggle ")
            change = -1
        else:
            raise Exception("Not sure what to do with: ", line)

        start_str, end_str = line.split(" through ")
        start = tuple(int(x) for x in start_str.split(","))
        end = tuple(int(x) for x in end_str.split(","))

        if debug:
            print(start, end, change)

        for y in range(start[1], end[1] + 1):
            for x in range(start[0], end[0] + 1):
                value = grid[y][x]
                if change == -1:
                    grid[y][x] = int(not value)
                else:
                    grid[y][x] = change

    # score it
    for row in grid:
        results += sum(row)

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    grid = [[0] * 1000 for _ in range(1000)]

    for line in data:
        if line.startswith("turn"):
            line = line.lstrip("turn ")
            if line.startswith("on"):
                line = line.lstrip("on ")
                change = 1
            elif line.startswith("off"):
                line = line.lstrip("off ")
                change = -1
            else:
                raise Exception("Not sure what to do with: ", line)
        elif line.startswith("toggle"):
            line = line.lstrip("toggle ")
            change = 2
        else:
            raise Exception("Not sure what to do with: ", line)

        start_str, end_str = line.split(" through ")
        start = tuple(int(x) for x in start_str.split(","))
        end = tuple(int(x) for x in end_str.split(","))

        if debug:
            print(start, end, change)

        for y in range(start[1], end[1] + 1):
            for x in range(start[0], end[0] + 1):
                grid[y][x] = max(grid[y][x] + change, 0)

    # score it
    for row in grid:
        results += sum(row)

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 998996
    # print("Real1: ", run(part=1, debug=False))  # 569999
    print("Real2: ", run(part=2, debug=False))  # 17836115
