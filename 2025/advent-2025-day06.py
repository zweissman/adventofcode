import re


def run(part: int, test_suffix: str = "", debug: bool = False):
    y, d = __file__.split("advent-")[1].split("-day")
    file_name = f"{y}/input/{d.strip('.py')}{test_suffix}.txt"

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.replace("\n", " ") for x in file_data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def part1(data: list[str], debug: bool = False) -> int:
    results = 0
    show(data, debug=debug)

    numbers: list[list[int]] = []
    operators = data[-1].split()

    for i in range(len(data) - 1):
        numbers.append([int(x) for x in data[i].split()])

    for i, operator in enumerate(operators):
        if operator == "+":
            col_results = 0
            for row in numbers:
                col_results += row[i]
        elif operator == "*":
            col_results = 1
            for row in numbers:
                col_results *= row[i]

        results += col_results

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    show(data, debug=debug)

    numbers: list[list[str]] = []
    operators = re.findall(r"[+*]\s*", data[-1] + " ")

    for row in data[:-1]:
        index = 0
        new_row: list[str] = []
        for i, value in enumerate(operators):
            col_width = len(value)  # Including space

            new_row.append(row[index : index + col_width][:-1])  # Exclude trailing space
            index += col_width

        numbers.append(new_row)

    rotated_numbers = rotate(numbers)
    if debug:
        print(rotated_numbers)

    for i, operator in enumerate(operators):
        if debug:
            print("a", rotated_numbers[i])
        max_length = len(max(rotated_numbers[i], key=len))
        #        if debug: print("b", max_length)

        converted_numbers = [""] * max_length
        for x in range(max_length - 1, -1, -1):
            for number in reversed(rotated_numbers[i]):
                converted_numbers[x] = converted_numbers[x] + number.ljust(max_length, " ")[x]

        if debug:
            print("c", converted_numbers)

        if operator.strip() == "+":
            col_results = 0
            for number in converted_numbers:
                if number.strip() != "":
                    col_results += int(number)
        elif operator.strip() == "*":
            col_results = 1
            for number in converted_numbers:
                if number.strip() != "":
                    col_results *= int(number)

        if debug:
            print("d", col_results)
        results += col_results

    return results


def rotate(matrix: list[list[str]]) -> list[list[str]]:
    # Reverse the order of rows
    reversed_matrix = matrix[::-1]

    # Use zip to transpose the reversed matrix
    # map(list, ...) converts the tuples from zip back into lists
    rotated_matrix = list(map(list, zip(*reversed_matrix)))

    return rotated_matrix


def show(grid: list[str], debug: bool = False) -> None:
    if debug:
        print()
        for y, row in enumerate(grid):
            print(f"{y:02}", "".join([str(x) for x in row]))


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 4277556
    # print("Real1: ", run(part=1, debug=False))  # 4693419406682
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # 3263827
    print("Real2: ", run(part=2, debug=False))  # 9029931401920
