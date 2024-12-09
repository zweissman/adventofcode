def run(part: int, test_run: bool = False, debug: bool = False) -> int:
    file_name = "2024/input/04.txt"
    if test_run:
        file_name = file_name.replace(".txt", "-test.txt")

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def show(grid: list[str], debug: bool = False) -> None:
    if debug:
        print()
        for y, row in enumerate(grid):
            print(y, "".join([str(x) for x in row]))


def part1(data: list[str], debug: bool = False) -> int:
    WORD = "XMAS"
    results = 0

    show(data, debug=debug)
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell == WORD[0]:
                results += word_count(data, WORD, x, y, debug)

    return results


def word_count(grid: list[str], word: str, x: int, y: int, debug: bool) -> int:
    results = 0
    directions = [
        (-1, -1, "up left"),
        (0, -1, "up"),
        (1, -1, "up right"),
        (-1, 0, "left"),
        (1, 0, "right"),
        (-1, 1, "down left"),
        (0, 1, "down"),
        (1, 1, "down right"),
    ]
    try:
        for dx, dy, direction in directions:
            for i in range(1, len(word)):
                test_x = x + i * dx
                test_y = y + i * dy
                if test_x < 0 or test_y < 0 or test_x >= len(grid[0]) or test_y >= len(grid):
                    break
                if grid[test_y][test_x] != word[i]:
                    break
            else:
                results += 1
                if debug:
                    print(f"Found {word} at ({x}, {y}) with direction {direction}")

    except IndexError:
        pass

    return results


def part2(data: list[str], debug: bool = False) -> int:
    WORD = "MAS"
    target_letter_index = len(WORD) // 2

    results = 0

    show(data, debug=debug)

    results += word_count_x(data, WORD, 1, 8, debug)

    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell == WORD[target_letter_index]:
                results += word_count_x(data, WORD, x, y, debug)

    return results


def word_count_x(grid: list[str], word: str, x: int, y: int, debug: bool) -> int:
    patterns = [
        (((-1, 1, "down left"), (1, -1, "up right")), ((-1, -1, "up left"), (1, 1, "down right"))),
        (((-1, 1, "down left"), (1, -1, "up right")), ((1, 1, "down right"), (-1, -1, "up left"))),
        (((1, -1, "up right"), (-1, 1, "down left")), ((-1, -1, "up left"), (1, 1, "down right"))),
        (((1, -1, "up right"), (-1, 1, "down left")), ((1, 1, "down right"), (-1, -1, "up left"))),
    ]
    try:
        for pattern in patterns:
            orientation = ""
            for line in pattern:
                # slash start
                dx, dy, direction = line[0]

                test_x = x + dx
                test_y = y + dy
                orientation += direction + "-"

                if test_x < 0 or test_y < 0 or test_x >= len(grid[0]) or test_y >= len(grid):
                    break
                if grid[test_y][test_x] != word[0]:
                    break

                # slash end
                dx, dy, direction = line[1]

                test_x = x + dx
                test_y = y + dy
                orientation += direction + " / "

                if test_x < 0 or test_y < 0 or test_x >= len(grid[0]) or test_y >= len(grid):
                    break
                if grid[test_y][test_x] != word[2]:
                    break

            else:
                if debug:
                    print(f"Found {word} at ({x}, {y}) with orientation {orientation}")
                return 1

    except IndexError:
        pass

    return 0


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # 18
    # print("Real1: ", run(part=1, test_run=False, debug=False))  #2493
    # print("Test2: ", run(part=2, test_run=True, debug=True))  # 9
    print("Real2: ", run(part=2, test_run=False, debug=False))  # 1890
