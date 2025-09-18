"""
--- Day 4: The Ideal Stocking Stuffer ---
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
Your puzzle answer was 282749.

--- Part Two ---
Now find one that starts with six zeroes.

Your puzzle answer was 9962624.
"""

import hashlib


def run(part: int, test_suffix: str = "", debug: bool = False):
    y, d = __file__.split("advent-")[1].split("-day")
    file_name = f"{y}/input/{d.strip('.py')}{test_suffix}.txt"

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def part1(data: list[str], debug: bool = False) -> int:
    key = data[0]

    for counter in range(9999999):
        pre_hash = key + str(counter)
        md5 = hashlib.md5(usedforsecurity=False)
        md5.update(pre_hash.encode("utf-8"))
        md5_hash = md5.hexdigest()

        if str(md5_hash)[:5] == "00000":
            return counter

        if debug:
            if counter % 100000 == 0:
                print(key, counter)

    return 0


def part2(data: list[str], debug: bool = False) -> int:
    key = data[0]

    for counter in range(9999999999):
        pre_hash = key + str(counter)
        md5 = hashlib.md5(usedforsecurity=False)
        md5.update(pre_hash.encode("utf-8"))
        md5_hash = md5.hexdigest()

        if str(md5_hash)[:6] == "000000":
            return counter

        if debug:
            if counter % 100000 == 0:
                print(key, counter)

    return 0


if __name__ == "__main__":
    # print("Test1a: ", run(part=1, test_suffix="-test1a", debug=True))  # 609043
    # print("Test1b: ", run(part=1, test_suffix="-test1b", debug=True))  # 1048970
    # print("Real1: ", run(part=1, debug=False))  # 282749
    print("Real2: ", run(part=2, debug=False))  # 9962624
