# pylint: disable=eval-used,redefined-outer-name,redefined-builtin,unspecified-encoding
# pylint: disable=consider-using-enumerate, pointless-string-statement

FILE_NAME = "2015/input/03.txt"


"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
"""


def part1_run1() -> int:
    with open(FILE_NAME) as f:
        input = f.read()

        x = 0
        y = 0
        houses = {(x, y)}
        for direction in input:
            if direction == "^":
                y += 1
            elif direction == "v":
                y -= 1
            elif direction == ">":
                x += 1
            elif direction == "<":
                x -= 1
            houses.add((x, y))
        return len(houses)


"""
--- Part Two ---
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
"""


def part2_run1() -> int:
    with open(FILE_NAME) as f:
        input = f.read()

        x = 0
        y = 0
        rx = 0
        ry = 0
        houses = {(x, y)}
        for i, direction in enumerate(input):
            if i % 2 == 0:
                if direction == "^":
                    y += 1
                elif direction == "v":
                    y -= 1
                elif direction == ">":
                    x += 1
                elif direction == "<":
                    x -= 1
                houses.add((x, y))
            else:
                if direction == "^":
                    ry += 1
                elif direction == "v":
                    ry -= 1
                elif direction == ">":
                    rx += 1
                elif direction == "<":
                    rx -= 1
                houses.add((rx, ry))
        return len(houses)


if __name__ == "__main__":
    #        print(f"Part 1 answer {part1_run1()}")
    print(f"Part 2 answer {part2_run1()}")
