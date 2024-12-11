CACHE: dict[tuple[int, int], int] = {}


def run(part: int, test_suffix: str = "", debug: bool = False):
    y, d = __file__.split("advent-")[1].split("-day")
    file_name = f"{y}/input/{d.strip('.py')}{test_suffix}.txt"

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def part1(data: list[str], debug: bool = False) -> int:  # pylint: disable=unused-argument
    results = 0
    stones = [int(x) for x in data[0].split()]

    for stone in stones:
        results += stone_count(stone, 25)

    return results


def part2(data: list[str], debug: bool = False) -> int:  # pylint: disable=unused-argument
    results = 0
    stones = [int(x) for x in data[0].split()]

    for stone in stones:
        results += stone_count(stone, 75)

    return results


def stone_count(stone: int, step: int) -> int:
    if step == 0:
        return 1

    if (stone, step) in CACHE:
        return CACHE[(stone, step)]

    if stone == 0:
        results = stone_count(1, step - 1)
        CACHE[(stone, step)] = results
        return results

    stone_str = str(stone)
    stone_length = len(str(stone))

    if stone_length % 2 == 0:
        stone1, stone2 = int(stone_str[: stone_length // 2]), int(stone_str[stone_length // 2 :])
        stone1_count = stone_count(stone1, step - 1)
        stone2_count = stone_count(stone2, step - 1)
        CACHE[(stone, step)] = stone1_count + stone2_count
        return stone1_count + stone2_count

    results = stone_count(stone * 2024, step - 1)
    CACHE[(stone, step)] = results

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 55312
    # print("Real1: ", run(part=1, debug=False))  # 193269
    print("Real2: ", run(part=2, debug=False))  # 228449040027793
