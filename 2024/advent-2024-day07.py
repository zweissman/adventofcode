from ast import literal_eval
from itertools import product


def run(part: int, test_suffix: str = "", debug: bool = False):
    y, d = __file__.split("advent-")[1].split("-day")
    file_name = f"{y}/input/{d.strip('.py')}{test_suffix}.txt"

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def show(grid: list[str], debug: bool = False) -> None:
    if debug:
        print()
        for y, row in enumerate(grid):
            print(y, "".join([str(x) for x in row]))


def part1(data: list[str], debug: bool = False) -> int:
    results = 0
    show(data, debug=debug)

    for row_number, row in enumerate(data):
        test_value_str, number_strings = row.split(": ")
        test_value = int(test_value_str)
        numbers = [int(x) for x in number_strings.split(" ")]
        if (row_number + 1) % 100 == 0:
            print("row ", row_number + 1, test_value)

        combos = list(product(["*", "+"], repeat=len(numbers) - 1))
        if debug:
            print(combos)

        for combo in combos:
            equation_list: list[int | str] = [numbers[0]]

            for i, symbol in enumerate(combo):
                equation_list.append(symbol)
                equation_list.append(numbers[i + 1])

            total = equation_list[0]
            for i in range(1, len(equation_list) - 1, 2):
                operator = equation_list[i]
                second = equation_list[i + 1]
                equation = f"{total} {operator} {second}"
                total = literal_eval(equation)

            if debug:
                print(test_value, ": ", equation_list, total)
            if total == test_value:
                if debug:
                    print("MATCH")
                results += test_value
                break

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    show(data, debug=debug)

    for row_number, row in enumerate(data):
        test_value_str, number_strings = row.split(": ")
        test_value = int(test_value_str)
        numbers = [int(x) for x in number_strings.split(" ")]
        if (row_number + 1) % 100 == 0:
            print("row ", row_number + 1, test_value)

        combos = list(product(["*", "+", "||"], repeat=len(numbers) - 1))
        if debug:
            print(combos)

        for combo in combos:
            equation_list: list[int | str] = [numbers[0]]

            for i, symbol in enumerate(combo):
                equation_list.append(symbol)
                equation_list.append(numbers[i + 1])

            total = equation_list[0]
            for i in range(1, len(equation_list) - 1, 2):
                operator = equation_list[i]
                second = equation_list[i + 1]

                if operator == "||":
                    total = int(str(total) + str(second))
                else:
                    equation = f"{total} {operator} {second}"
                    total = literal_eval(equation)

            if debug:
                print(test_value, ": ", equation_list, total)
            if total == test_value:
                if debug:
                    print("MATCH")
                results += test_value
                break

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 3749
    # TODO: SLOW
    # print("Real1: ", run(part=1, debug=False))  # 663613490587
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # 11387
    # TODO: SLOW
    print("Real2: ", run(part=2, debug=False))  # 110365987435001
