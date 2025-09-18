"""
--- Day 10: Elves Look, Elves Say ---
Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence. For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step, take the previous value, and replace each run of digits (like 111) with the number of digits (3) followed by the digit itself (1).

For example:

1 becomes 11 (1 copy of digit 1).
11 becomes 21 (2 copies of digit 1).
21 becomes 1211 (one 2 followed by one 1).
1211 becomes 111221 (one 1, one 2, and two 1s).
111221 becomes 312211 (three 1s, two 2s, and one 1).
Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

Your puzzle input is 1321131112.

Your puzzle answer was 492982.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Neat, right? You might also enjoy hearing John Conway talking about this sequence (that's Conway of Conway's Game of Life fame).

Now, starting again with the digits in your puzzle input, apply this process 50 times. What is the length of the new result?

Your puzzle answer was 6989950.

"""

from itertools import groupby


def run(part: int, iterations: int, test_suffix: str = "", debug: bool = False):
    y, d = __file__.split("advent-")[1].split("-day")
    file_name = f"{y}/input/{d.strip('.py')}{test_suffix}.txt"

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, iterations=iterations, debug=debug)


def part1(data: list[str], iterations: int, debug: bool = False) -> int:
    show(data, debug=debug)

    sequence = list(data[0])

    for _ in range(iterations):
        results = ""

        for number, group in groupby(sequence):
            occurrence = len(list(group))

            results += str(occurrence) + number

        if debug:
            print(f"{_} -> {len(results)}")

        sequence = list(results)

    return len(results)


def part2(data: list[str], iterations: int, debug: bool = False) -> int:
    sequence = data[0]
    for _ in range(iterations):
        sequence = "".join([str(len(list(g))) + str(k) for k, g in groupby(sequence)])
        if debug:
            print(sequence)

    return len(sequence)


def show(grid: list[str], debug: bool = False) -> None:
    if debug:
        print()
        for y, row in enumerate(grid):
            print(f"{y:02}", "".join([str(x) for x in row]))


if __name__ == "__main__":
    # print("Test1: ", run(part=1, iterations=5, test_suffix="-test", debug=True))  # 312211
    # print("Real1: ", run(part=1, iterations=40, debug=False))  # 492982
    print("Real2: ", run(part=2, iterations=50, debug=True))  # 6989950
