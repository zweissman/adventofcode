from typing import Any


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

    map_: dict[int, Any] = {new_list: [] for new_list in range(256)}

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
                for i, val in enumerate(map_[key]):
                    if val.split(" ")[0] == left:
                        map_[key][i] = f"{left} {right}"
                        break
                else:
                    map_[key].append(f"{left} {right}")

            else:
                assert "-" in section
                left, _ = section.split("-")
                for c in left:
                    key = (key + ord(c)) * 17 % 256
                for i, val in enumerate(map_[key]):
                    if val.split(" ")[0] == left:
                        map_[key][i] = ""
                        break

            if debug:
                print(key, map_[key])

        for k, v in map_.items():
            if len(v) > 0:
                if debug:
                    print(k, map_[k])
                map_[k] = [val for val in map_[k] if val != ""]
                if debug:
                    print(k, map_[k])
                lens_value = 0
                for slot, lens in enumerate(map_[k]):
                    lens_value += (k + 1) * (slot + 1) * int(lens.split(" ")[1])

                results += lens_value

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 1320
    # print("Real1: ", run(part=1, debug=False))  # 507291
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True)) # 145
    print("Real2: ", run(part=2, debug=True))  # 296921
