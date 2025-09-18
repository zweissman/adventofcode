"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
Your puzzle answer was 2572.

--- Part Two ---
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

Your puzzle answer was 2631.
"""

from collections import defaultdict


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

    for line in data:
        x, y = 0, 0
        houses: dict[tuple[int, int], int] = defaultdict(int)
        houses[(x, y)] += 1

        for c in list(line):
            if c == ">":
                x += 1
            elif c == "<":
                x -= 1
            elif c == "^":
                y -= 1
            elif c == "v":
                y += 1
            else:
                raise Exception(f"This should not happen {c}")
            houses[(x, y)] += 1

        if debug:
            print(line, len(houses.keys()))

        results += len(houses.keys())

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0

    for line in data:
        x1, y1 = 0, 0
        x2, y2 = 0, 0
        houses: dict[tuple[int, int], int] = defaultdict(int)
        houses[(x1, y1)] += 2

        for i, c in enumerate(list(line)):
            if i % 2 == 0:
                x, y = x1, y1
            else:
                x, y = x2, y2

            if c == ">":
                x += 1
            elif c == "<":
                x -= 1
            elif c == "^":
                y -= 1
            elif c == "v":
                y += 1
            else:
                raise Exception(f"This should not happen {c}")

            if i % 2 == 0:
                x1 = x
                y1 = y
            else:
                x2 = x
                y2 = y

            houses[(x, y)] += 1

        if debug:
            print(line, len(houses.keys()))

        results += len(houses.keys())

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test1a", debug=True))  # 8
    # print("Real1: ", run(part=1, debug=False))  # 2572
    # print("Test2: ", run(part=2, test_suffix="-test2b", debug=True))  # 17
    print("Real2: ", run(part=2, debug=False))  # 2631
