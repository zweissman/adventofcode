"""
--- Day 8: Matchsticks ---
Space on the sleigh is limited this year, and so Santa will be bringing his list as a digital copy. He needs to know how much space it will take up when stored.

It is common in many programming languages to provide a way to escape special characters in strings. For example, C, JavaScript, Perl, Python, and even PHP handle special characters in very similar ways.

However, it is important to realize the difference between the number of characters in the code representation of the string literal and the number of characters in the in-memory string itself.

For example:

"" is 2 characters of code (the two double quotes), but the string contains zero characters.
"abc" is 5 characters of code, but 3 characters in the string data.
"aaa\"aaa" is 10 characters of code, but the string itself contains six "a" characters and a single, escaped quote character, for a total of 7 characters in the string data.
"\x27" is 6 characters of code, but the string itself contains just one - an apostrophe ('), escaped using hexadecimal notation.
Santa's list is a file that contains many double-quoted string literals, one on each line. The only escape sequences used are \\ (which represents a single backslash), \" (which represents a lone double-quote character), and \\x plus two hexadecimal characters (which represents a single character with that ASCII code).

Disregarding the whitespace in the file, what is the number of characters of code for string literals minus the number of characters in memory for the values of the strings in total for the entire file?

For example, given the four strings above, the total number of characters of string code (2 + 5 + 10 + 6 = 23) minus the total number of characters in memory for string values (0 + 3 + 7 + 1 = 11) is 23 - 11 = 12.

Your puzzle answer was 1371.

--- Part Two ---
Now, let's go the other way. In addition to finding the number of characters of code, you should now encode each code representation as a new string and find the number of characters of the new encoded representation, including the surrounding double quotes.

For example:

"" encodes to "\"\"", an increase from 2 characters to 6.
"abc" encodes to "\"abc\"", an increase from 5 characters to 9.
"aaa\"aaa" encodes to "\"aaa\\\"aaa\"", an increase from 10 characters to 16.
"\x27" encodes to "\"\\x27\"", an increase from 6 characters to 11.
Your task is to find the total number of characters to represent the newly encoded strings minus the number of characters of code in each original string literal. For example, for the strings above, the total encoded length (6 + 9 + 16 + 11 = 42) minus the characters in the original code representation (23, just like in the first part of this puzzle) is 42 - 23 = 19.

Your puzzle answer was 2117.
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
    show(data, debug=debug)

    literal_results, memory_results = 0, 0

    for row in data:
        literal, memory, _ = get_lengths(row)
        literal_results += literal
        memory_results += memory

    results = literal_results - memory_results

    return results


def get_lengths(row: str) -> tuple[int, int, int]:
    literal = len(row)
    decoded = 0
    encoded = 6  # for original escaped quotes and string quotes

    # confirm that it starts and ends with a quote and trim them
    assert row[0] == '"'
    assert row[-1] == '"'
    row = row[1:-1]
    i = 0

    while i < len(row):
        x = row[i]

        if x == "\\":
            if row[i + 1] == '"':
                i += 1
                encoded += 3
            elif row[i + 1] == "\\":
                i += 1
                encoded += 3
            elif row[i + 1] == "x":
                i += 3
                encoded += 4

        decoded += 1
        encoded += 1

        i += 1

    return literal, decoded, encoded


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    show(data, debug=debug)

    literal_results, encoded_results = 0, 0

    for row in data:
        literal, _, encoded = get_lengths(row)
        literal_results += literal
        encoded_results += encoded

    results = encoded_results - literal_results

    return results


def show(grid: list[str], debug: bool = False) -> None:
    if debug:
        print()
        for y, row in enumerate(grid):
            print(f"{y:02}", "".join([str(x) for x in row]))


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 12
    # print("Real1: ", run(part=1, debug=False))  # 1371
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # 19
    print("Real2: ", run(part=2, debug=False))  # 2117
