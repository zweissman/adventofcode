# pylint: disable=eval-used,redefined-outer-name,redefined-builtin,unspecified-encoding
# pylint: disable=consider-using-enumerate, pointless-string-statement
from ast import literal_eval as eval

"""
Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and he's fresh out! To save Christmas, he needs you to collect fifty stars by December 25th.

Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Here's an easy puzzle to warm you up.

Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:

(()) and ()() both result in floor 0.
((( and (()(()( both result in floor 3.
))((((( also results in floor 3.
()) and ))( both result in floor -1 (the first basement level).
))) and )())()) both result in floor -3.
To what floor do the instructions take Santa?
"""

FILE_NAME = "2015/input/01.txt"

"""
Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

For example:

) causes him to enter the basement at character position 1.
()()) causes him to enter the basement at character position 5.
What is the position of the character that causes Santa to first enter the basement?
"""


def part1_run1() -> int:
    with open(FILE_NAME, "r") as f:
        input = f.read()

        return input.count("(") - input.count(")")


def part1_run2() -> int:
    with open(FILE_NAME, "r") as f:
        instructions = f.read()
    floor = 0
    for instruction in instructions:
        if instruction == "(":
            floor += 1
        elif instruction == ")":
            floor -= 1
    return floor


def part1_run3() -> int:
    with open(FILE_NAME) as file:
        data = file.read()
    floor = 0
    for c in data:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
    return floor


def part1_run4() -> int:
    with open(FILE_NAME) as data:
        instructions = data.read()

    floor = 0
    for i, c in enumerate(instructions):
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        else:
            raise ValueError(f'Unknown instruction "{c}" at position {i}')

    return floor


def part1_run5() -> int:
    floor = 0

    with open(FILE_NAME) as f:
        for line in f:
            for char in line:
                if char == "(":
                    floor += 1
                elif char == ")":
                    floor -= 1
                else:
                    continue

    return floor


def part1_run6() -> int:
    with open(FILE_NAME) as input_file:
        input_data = input_file.read()

    floor = 0
    for char in input_data:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
    return floor


def part1_run7() -> int:
    with open(FILE_NAME) as input_file:
        instructions = input_file.read()

    floor = 0
    for i in instructions:
        if i == "(":
            floor += 1
        elif i == ")":
            floor -= 1
        else:
            raise Exception("Unknown instruction: " + i)

    return floor


def part1_run8() -> int:
    with open(FILE_NAME) as f:
        data = f.read()
    return data.count("(") - data.count(")")


def part1_run9() -> int:
    with open(FILE_NAME, "r") as f:
        input = f.read()
    floor = 0
    for c in input:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
    return floor


def part1_run10() -> int:
    with open(FILE_NAME) as file:
        data = file.read()
    floor = 0
    for i in range(len(data)):
        if data[i] == "(":
            floor += 1
        elif data[i] == ")":
            floor -= 1
    return floor


def part2_run1() -> int:
    with open(FILE_NAME, "r") as f:
        instructions = f.read()
    floor = 0
    for i in range(len(instructions)):
        if instructions[i] == "(":
            floor += 1
        elif instructions[i] == ")":
            floor -= 1
        if floor == -1:
            return i + 1
    return floor


def part2_run2() -> int:
    with open(FILE_NAME) as file:
        data = file.read()

    floor = 0
    for i in range(len(data)):
        if data[i] == "(":
            floor += 1
        elif data[i] == ")":
            floor -= 1
        if floor == -1:
            return i + 1
    return -1


def part2_run3() -> int:
    with open(FILE_NAME) as file:
        data = file.read()
    floor = 0
    for i in range(len(data)):
        if data[i] == "(":
            floor += 1
        elif data[i] == ")":
            floor -= 1
        if floor == -1:
            return i + 1
    return floor


def part2_run4() -> int:
    with open(FILE_NAME, "r") as f:
        instructions = f.read()

    floor = 0
    for i, instruction in enumerate(instructions):
        if instruction == "(":
            floor += 1
        elif instruction == ")":
            floor -= 1

        if floor == -1:
            return i + 1

    raise ValueError("Never entered basement.")


def part2_run5() -> int:
    with open(FILE_NAME, "r") as f:
        input = f.read()
    floor = 0
    for i, c in enumerate(input):
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        if floor == -1:
            return i + 1
    raise ValueError("Never entered the basement")


def part2_run6() -> int:
    with open(FILE_NAME, "r") as f:
        input = f.read()
    floor = 0
    for i in range(len(input)):
        if input[i] == "(":
            floor += 1
        elif input[i] == ")":
            floor -= 1
        if floor == -1:
            return i + 1

    return i


def part2_run7() -> int:
    with open(FILE_NAME, "r") as f:
        data = f.read()
    floor = 0
    for i in range(len(data)):
        if data[i] == "(":
            floor += 1
        elif data[i] == ")":
            floor -= 1
        if floor == -1:
            return i + 1

    return -1


def part2_run8() -> int:
    with open(FILE_NAME, "r") as f:
        input = f.read()
    floor = 0
    for i, c in enumerate(input):
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        if floor == -1:
            return i + 1
    return -1


if __name__ == "__main__":
    import timeit

    for i in range(1, 10):
        print(
            f"Part 1 answer {i}: {eval(f'part1_run{i}')()}\tTime: {timeit.timeit(eval(f'part1_run{i}'), number=1000)}"
        )
    for i in range(1, 8):
        print(
            f"Part 2 answer {i}: {eval(f'part2_run{i}')()}\tTime: {timeit.timeit(eval(f'part2_run{i}'), number=1000)}"
        )
