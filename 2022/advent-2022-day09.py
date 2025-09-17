FILE_NAME = "2022/input/09.txt"

GRID = []
KNOTS = []
H = ()
T = ()


def run(part: int, test_run: bool = False, debug: bool = False):
    if test_run:
        file = FILE_NAME.replace(".txt", "-test.txt")
        dim = 10
        x = 0
        y = 4
    else:
        file = FILE_NAME
        dim = 1000
        x = 500
        y = 500

    with open(file, encoding="utf-8") as f:
        file_data = f.readlines()

    data = [x.strip() for x in file_data]
    if part == 1:
        part_function = part1
        knot_count = 2
    else:
        part_function = part2
        knot_count = 10

    return part_function(data=data, x=x, y=y, dim=dim, knot_count=knot_count, debug=debug)


def part1(data: list[str], x: int, y: int, dim: int, knot_count: int, debug=False) -> int:
    results = 0
    global GRID, H, T
    GRID = [[0] * dim for i in range(dim)]
    H = (x, y)
    T = (x, y)

    if debug:
        print(knot_count)
        show1(dim)

    for row in data:
        # if debug: print(row)
        move1(row, dim, debug)

    results = score()
    return results


def move1(command, dim, debug):
    global H, T

    direction, count = command.split(" ")
    count = int(count)

    try:
        for i in range(count):
            if debug:
                print(f"\nMove {direction} {i + 1} of {count}")
            if direction == "R":
                H = (H[0] + 1, H[1])
            elif direction == "L":
                H = (H[0] - 1, H[1])
            elif direction == "U":
                H = (H[0], H[1] - 1)
            elif direction == "D":
                H = (H[0], H[1] + 1)

            hor = H[0] - T[0]
            ver = H[1] - T[1]
            if hor != 0 and ver != 0 and (abs(hor) + abs(ver)) > 2:
                # move diagonal
                # print("T move DIAGONAL")
                if direction == "R":
                    T = (H[0] - 1, H[1])
                elif direction == "L":
                    T = (H[0] + 1, H[1])
                elif direction == "U":
                    T = (H[0], H[1] + 1)
                elif direction == "D":
                    T = (H[0], H[1] - 1)

            elif hor != 0 and abs(hor) > 1:
                # move horizontally
                # print("T move HORIZON")
                if hor > 0:
                    T = (T[0] + 1, T[1])
                else:
                    T = (T[0] - 1, T[1])
            elif ver != 0 and abs(ver) > 1:
                # move vertically
                #                print("T move VERTICAL")
                if ver > 0:
                    T = (T[0], T[1] + 1)
                else:
                    T = (T[0], T[1] - 1)

            GRID[T[0]][T[1]] = 1

            if debug:
                show1(dim)
            if debug:
                print(score())

    except IndexError as e:
        raise Exception(f"Ran off the board, increase DIM: {H=} {T=}") from e


def show1(dim):
    for x in range(dim):
        line = ""
        for y in range(dim):
            if H == (y, x):
                if GRID[y][x] == 1:
                    line += "h"
                else:
                    line += "H"
            elif T == (y, x):
                line += "T"
            else:
                line += str(GRID[y][x])
        print(line)


def score():
    results = 0
    for x in GRID:
        results += sum(x)
    return results


def part2(data: list[str], x: int, y: int, dim: int, knot_count: int, debug: bool = False) -> int:
    results = 0
    global GRID, KNOTS
    GRID = [[0] * dim for i in range(dim)]
    for _ in range(knot_count):
        KNOTS.append((x, y))

    if debug:
        show1(dim)

    for row in data:
        #        if debug: print(row)
        move2(row, dim, knot_count, debug)

    results = score()
    return results


def move2(command, dim, knot_count, debug):
    global KNOTS, H, T
    H = None
    T = None
    direction, count = command.split(" ")
    count = int(count)
    try:
        for i in range(count):
            if debug:
                print(f"\nMove {direction} {i} of {count}")
            stop = False

            for k in range(knot_count - 1):
                H = KNOTS[k]
                T = KNOTS[k + 1]

                if k == 0:
                    # Only for the first head
                    if direction == "R":
                        H = (H[0] + 1, H[1])
                    elif direction == "L":
                        H = (H[0] - 1, H[1])
                    elif direction == "U":
                        H = (H[0], H[1] - 1)
                    elif direction == "D":
                        H = (H[0], H[1] + 1)

                hor = H[0] - T[0]
                ver = H[1] - T[1]

                if hor != 0 and ver != 0 and (abs(hor) + abs(ver)) > 2:
                    # print("T move DIAGONAL")
                    if ver < 0:
                        T = (T[0], T[1] - 1)
                    else:
                        T = (T[0], T[1] + 1)

                    if hor > 0:
                        T = (T[0] + 1, T[1])
                    else:
                        T = (T[0] - 1, T[1])

                elif hor != 0 and abs(hor) > 1:
                    # print("T move HORIZON")
                    if hor > 0:
                        T = (T[0] + 1, T[1])
                    else:
                        T = (T[0] - 1, T[1])
                elif ver != 0 and abs(ver) > 1:
                    # print("T move VERTICAL")
                    if ver > 0:
                        T = (T[0], T[1] + 1)
                    else:
                        T = (T[0], T[1] - 1)
                else:
                    stop = True

                #                LAST_HEAD = H
                KNOTS[k] = H
                KNOTS[k + 1] = T
                # if debug: print()
                # if debug: show2(dim, knot_count)
                if stop:
                    break

            TAIL = KNOTS[knot_count - 1]
            if debug:
                print(f"SCORE {TAIL}")
            GRID[TAIL[0]][TAIL[1]] = 1
            if debug:
                show2(dim, knot_count)
            if debug:
                print(score())

    except IndexError as e:
        raise Exception(f"Ran off the board, increase DIM. {KNOTS=}") from e


def show2(dim, knot_count):
    for x in range(dim):
        line = ""
        for y in range(dim):
            for k in range(knot_count):
                if KNOTS[k] == (y, x):
                    if k == 0:
                        line += "H"
                    else:
                        line += str(k)
                    break
            else:
                if GRID[y][x] == 1:
                    line += "x"
                else:
                    line += "."

        print(line)


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # 13
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 6464
    # print("Test2: ", run(part=2, test_run=True, debug=True))  # 1
    print("Real2: ", run(part=2, test_run=False, debug=False))  # 2604
