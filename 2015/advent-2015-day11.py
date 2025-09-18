"""
--- Day 11: Corporate Policy ---
Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
For example:

hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
abbcegjk fails the third requirement, because it only has one double letter (bb).
The next password after abcdefgh is abcdffaa.
The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
Given Santa's current password (your puzzle input), what should his next password be?

Your puzzle answer was hxbxxyzz.

--- Part Two ---
Santa's password expired again. What's the next one?

Your puzzle answer was hxcaabcc.

"""

BAD_LETTERS = ["i", "l", "o"]


def run(part: int, test_suffix: str = "", debug: bool = False):
    y, d = __file__.split("advent-")[1].split("-day")
    file_name = f"{y}/input/{d.strip('.py')}{test_suffix}.txt"

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def get_next_letter(letter: str) -> str:
    if letter == "h":
        return "j"
    if letter == "k":
        return "m"
    if letter == "n":
        return "p"
    return chr(ord(letter) + 1)


def base26_to_int(word: str) -> int:
    """Converts a base-26 string (a-z) to its integer equivalent."""
    result = 0
    word = "z" + word
    for i, char in enumerate(reversed(word)):
        # 'a' is 0, 'b' is 1, ..., 'z' is 25
        value = ord(char) - ord("a")
        result += value * (26**i)
    return result


def int_to_base26(value: int) -> str:
    """Converts an integer to its base-26 string equivalent (A-Z)."""
    if value == 0:
        return "a"  # Special case for 0

    result = ""
    while value > 0:
        remainder = value % 26
        # Convert remainder to character ('a' + remainder)
        char = chr(ord("a") + remainder)
        result = char + result  # Prepend character to build the string
        value //= 26

    assert result[0:1] == "z"
    result = result[1:]

    return result


def check_for_bad_letters(word: str):
    for bad_letter in BAD_LETTERS:
        index = word.find(bad_letter)
        if index >= 0:
            word = word.replace(bad_letter, get_next_letter(bad_letter))
            word = word[: index + 1] + (len(word) - index - 1) * "a"
            return word

    return ""


def has_run(word: str, run_length: int) -> bool:
    for i in range(0, len(word) - run_length):
        if ord(word[i]) + 2 == ord(word[i + 1]) + 1 == ord(word[i + 2]):
            return True

    return False


def has_match(word: str) -> bool:
    found = ""
    for i in range(0, len(word) - 1):
        if word[i] == word[i + 1]:
            if found != "" and found != word[i]:  # pylint: disable=[consider-using-in]
                return True
            if found == "":
                found = word[i]

    return False


def is_valid(word: str) -> bool:
    if not has_run(word, 3):
        return False

    if not has_match(word):
        return False

    return True


def part1(data: list[str], debug: bool = False) -> str:
    show(data, debug=debug)

    for word in data:
        offset = 1
        int_version = base26_to_int(word)
        next_password = int_to_base26(int_version + offset)
        next_password = check_for_bad_letters(next_password)

        while not is_valid(next_password):
            offset += 1
            next_password = int_to_base26(int_version + offset)
            new_password = check_for_bad_letters(next_password)
            if new_password:
                int_version = base26_to_int(new_password)
                offset = -1
                next_password = new_password

            if debug:
                print(word, next_password)

        if debug:
            print(word, next_password)

    return next_password


def part2(data: list[str], debug: bool = False) -> str:
    return part1(data, debug)


def show(grid: list[str], debug: bool = False) -> None:
    if debug:
        print()
        for y, row in enumerate(grid):
            print(f"{y:02}", "".join([str(x) for x in row]))


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # ghjaabcc
    # print("Real1: ", run(part=1, debug=False))  # hxbxxyzz
    print("Real2: ", run(part=1, debug=False))  # hxcaabcc
