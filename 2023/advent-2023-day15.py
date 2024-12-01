# pylint: disable=too-many-return-statements,too-many-statements,too-many-branches,duplicate-code,unused-argument
# pylint: disable=unnecessary-list-index-lookup

from typing import Any

FILE_NAME = "2023/input/15.txt"


def run(part: int, test_run: bool = False, debug: bool = False):
    if test_run:
        file = FILE_NAME.replace(".txt", "-test.txt")
    else:
        file = FILE_NAME

    with open(file, encoding="utf-8") as f:
        data = f.readlines()

    data = [x.strip() for x in data]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def part1(data: list[str], debug: bool = False) -> int:
    results = 0

    for line in data:
        if line.startswith("//"):
            continue
        sections = line.split(",")
        for section in sections:
            word = 0
            for c in section:
                word = (word + ord(c)) * 17 % 256
                if debug:
                    print(c, word)
            results += word

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0

    map: dict[int, Any] = {new_list: [] for new_list in range(256)}

    for line in data:
        if line.startswith("//"):
            continue
        sections = line.split(",")
        for section in sections:
            key = 0
            if "=" in section:
                left, right = section.split("=")
                for c in left:
                    key = (key + ord(c)) * 17 % 256
                for i, val in enumerate(map[key]):
                    if val.split(" ")[0] == left:
                        map[key][i] = f"{left} {right}"
                        break
                else:
                    map[key].append(f"{left} {right}")

            else:
                assert "-" in section
                left, _ = section.split("-")
                for c in left:
                    key = (key + ord(c)) * 17 % 256
                for i, val in enumerate(map[key]):
                    if val.split(" ")[0] == left:
                        map[key][i] = ""
                        break

            if debug:
                print(key, map[key])

        for k, v in map.items():
            if len(v) > 0:
                if debug:
                    print(k, map[k])
                map[k] = [val for val in map[k] if val != ""]
                if debug:
                    print(k, map[k])
                lens_value = 0
                for slot, lens in enumerate(map[k]):
                    lens_value += (k + 1) * (slot + 1) * int(lens.split(" ")[1])

                results += lens_value

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # 1320
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 507291
    # print("Test2: ", run(part=2, test_run=True, debug=True)) # 145
    print("Real2: ", run(part=2, test_run=False, debug=True))  # 296921
