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

    for d in data:
        numbers_str = d.split()
        numbers = [int(x) for x in numbers_str]

        last_number = None
        direction = None

        if debug:
            print(d)

        for x in numbers:
            if direction is None:
                if last_number is None:
                    last_number = x
                    continue

                if last_number < x:
                    direction = "U"
                else:
                    direction = "D"

            if direction == "U":
                if last_number + 1 <= x <= last_number + 3:
                    last_number = x
                    continue

                break

            if direction == "D":
                if last_number - 1 >= x >= last_number - 3:
                    last_number = x
                    continue

                break

        else:
            results += 1
            if debug:
                print(direction)

    return results


def part2(data: list[str], debug: bool = False) -> int:
    # mypy doesn't like part1 and 2 having different signatures.
    return real_part2(data, debug)


def real_part2(data: list[str], bad_count: int = 0, debug: bool = False) -> int:
    results = 0

    for d in data:
        numbers_str = d.split()
        numbers = [int(x) for x in numbers_str]

        last_number = None
        direction = None

        if debug:
            print(d)

        for i, x in enumerate(numbers):
            if direction is None:
                if last_number is None:
                    last_number = x
                    continue

                if last_number < x:
                    direction = "U"
                else:
                    direction = "D"

            if direction == "U":
                if last_number + 1 <= x <= last_number + 3:
                    last_number = x
                    continue

            if direction == "D":
                if last_number - 1 >= x >= last_number - 3:
                    last_number = x
                    continue

            if bad_count == 0:
                if debug:
                    print("BAD1", x)

                new_numbers = d.split()
                del new_numbers[i]
                new_data = [" ".join(new_numbers)]

                bad_results = real_part2(new_data, bad_count=1, debug=debug)
                if bad_results == 1:
                    if debug:
                        print("CORRECTED INDEX")
                    results += 1
                    break

                if i == 2:
                    new_numbers = d.split()
                    del new_numbers[1]
                    new_data = [" ".join(new_numbers)]

                    bad_results = real_part2(new_data, bad_count=1, debug=debug)

                    if bad_results == 1:
                        if debug:
                            print("CORRECTED BEFORE")
                        results += 1
                        break

                # Try without the first number
                new_numbers = d.split()
                del new_numbers[0]
                new_data = [" ".join(new_numbers)]

                bad_results = real_part2(new_data, bad_count=1, debug=debug)

                if bad_results == 1:
                    if debug:
                        print("CORRECTED ZERO")
                    results += 1
                    break

            if debug:
                print("BAD_COUNT", bad_count)
            break

        else:
            results += 1
            if debug:
                print(direction)

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True)) # 2
    # print("Real1: ", run(part=1, debug=False)) # 321
    # TODO: Wrong
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True)) # 4
    print("Real2: ", run(part=2, debug=False))  # 386
