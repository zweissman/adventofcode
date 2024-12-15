def run(part: int, test_suffix: str = "", debug: bool = False):
    y, d = __file__.split("advent-")[1].split("-day")
    file_name = f"{y}/input/{d.strip('.py')}{test_suffix}.txt"

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


MAX_TOKEN = 100


def part1(data: list[str], debug: bool = False) -> int:
    results = 0

    while len(data) > 0:
        button_a, button_b, prize_str = data.pop(0), data.pop(0), data.pop(0)
        button_a = button_a.strip("Button A: X+").replace(" Y+", "")
        button_b = button_b.strip("Button B: X+").replace(" Y+", "")
        prize_str = prize_str.strip("Prize: X=").replace(" Y=", "")
        a = eval(button_a)  # pylint: disable=eval-used
        b = eval(button_b)  # pylint: disable=eval-used
        prize = eval(prize_str)  # pylint: disable=eval-used

        for b_press in range(0, MAX_TOKEN):
            if (prize[0] - (b[0] * b_press)) % a[0] == 0:
                a_press = (prize[0] - (b[0] * b_press)) / a[0]
                if a_press > MAX_TOKEN:
                    continue
                x = a_press * a[0] + b_press * b[0]
                y = a_press * a[1] + b_press * b[1]
                if prize == (x, y):
                    if debug:
                        print(
                            f"Found winner after {int(a_press)}*3 = {int(a_press*3)} + {int(b_press)} tokens"
                        )
                    results += int(b_press + a_press * 3)
                    break

        if debug:
            print(a, b, prize)
        if len(data) > 0:
            data.pop(0)

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    z = 0

    while len(data) > 0:
        z += 1
        button_a, button_b, prize_str = data.pop(0), data.pop(0), data.pop(0)
        button_a = button_a.strip("Button A: X+").replace(" Y+", "")
        button_b = button_b.strip("Button B: X+").replace(" Y+", "")
        prize_str = prize_str.strip("Prize: X=").replace(" Y=", "")
        a = eval(button_a)  # pylint: disable=eval-used
        b = eval(button_b)  # pylint: disable=eval-used
        prize = eval(prize_str)  # pylint: disable=eval-used
        prize = prize[0] + 10000000000000, prize[1] + 10000000000000

        numerator = prize[0] * a[1] - prize[1] * a[0]
        b_press = numerator / (b[0] * a[1] - b[1] * a[0])
        remainder = prize[0] - b_press * b[0]

        if a[0] == 0:
            l = prize[1]
            r = a[1]
        else:
            l = remainder
            r = a[0]

        a_press = l / r

        if int(a_press) * a[1] + int(b_press) * b[1] == prize[1] and l % r == 0:
            results += int(b_press + a_press * 3)
            if debug:
                print(
                    prize,
                    f"Found winner after {int(a_press)}*3 = {int(a_press*3)} + {int(b_press)} tokens",
                )

        if len(data) > 0:
            data.pop(0)

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 480
    # print("Real1: ", run(part=1, debug=False))  # 34787
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # 875318608908
    print("Real2: ", run(part=2, debug=False))  # 85644161121698
