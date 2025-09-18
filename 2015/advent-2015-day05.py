"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?

Your puzzle answer was 236.

--- Part Two ---
Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
How many strings are nice under these new rules?

Your puzzle answer was 51.
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

    for line in data:
        stop = False

        if sum([1 for x in list(line) if x in "aeiou"]) < 3:  # pylint: disable=consider-using-generator
            if debug:
                print(line, "does not have enough vowels")
            continue

        for i in range(0, 26):
            letter = chr(ord("a") + i) * 2
            if letter in line:
                break
        else:
            if debug:
                print(line, "does not have a double letter")
            continue

        for bad in ["ab", "cd", "pq", "xy"]:
            if bad in line:
                if debug:
                    print(line, "has a bad word in it")
                stop = True
                break

        if stop is True:
            continue

        if debug:
            print(line, "is good")
        results += 1

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0

    for line in data:
        for i in range(len(line) - 2):
            if line[i : i + 2] in line[i + 2 :]:
                break
        else:
            if debug:
                print(line, "does not have double letters")
            continue

        for i in range(len(line) - 2):
            if line[i] == line[i + 2]:
                break
        else:
            if debug:
                print(line, "does not a repeat one away")
            continue

        if debug:
            print(line, "is good")
        results += 1

    return results


if __name__ == "__main__":
    # print("Test1a: ", run(part=1, test_suffix="-test1a", debug=True))  # 2
    # print("Real1: ", run(part=1, debug=False))  # 236
    # print("Test2a: ", run(part=2, test_suffix="-test2b", debug=True))  # 2
    print("Real2: ", run(part=2, debug=False))  # 51
