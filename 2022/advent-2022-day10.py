FILE_NAME = "2022/input/10.txt"

X = 1
Y = 0
SCREEN = ""


def run(part: int, test_run: bool = False, debug: bool = False):
    if test_run:
        file = FILE_NAME.replace(".txt", "-test.txt")
    else:
        file = FILE_NAME

    with open(file, encoding="utf-8") as f:
        file_data = f.readlines()

    data = [x.strip() for x in file_data]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def part1(data: list[str], debug: bool = False) -> int:
    global X
    results = 0
    run_command = None
    run_command_arg = None
    clock = 1
    next_pop = 1
    X = 1

    while True:
        if debug:
            print(f"CLOCK: {clock} X {X} next {next_pop}")

        if next_pop == clock:
            if run_command is not None and run_command_arg is not None:
                run_command(run_command_arg, debug)
            if len(data) == 0:
                break
            command = data.pop(0)
            if debug:
                print("\t\t--> " + command)

            if command == "noop":
                run_command = None
                next_pop = clock + 1
            elif command.startswith("addx"):
                next_pop = clock + 2
                _, arg = command.split(" ")
                run_command = addx
                run_command_arg = int(arg)
            else:
                print(f"Unknown command {command}")
        elif next_pop < clock:
            print("We missed it")

        if (clock - 20) % 40 == 0:
            add_result = clock * X
            results += add_result
            if debug:
                print(f"== RESULTS: {results - add_result} + {add_result} = {results}")

        clock += 1

    return results


def part2(data: list[str], debug: bool = False) -> int:
    global X, Y, SCREEN
    results = 0
    run_command = None
    run_command_arg = None
    clock = 1
    next_pop = 1

    while True:
        if debug:
            print(f"CLOCK={clock} X={X} next={next_pop}")

        if next_pop == clock:
            if len(data) == 0:
                break
            command = data.pop(0)
            if debug:
                print("\t\t--> " + command)

            if command == "noop":
                run_command = None
                pop = clock + 1
            elif command.startswith("addx"):
                pop = clock + 2
                _, arg = command.split(" ")
                run_command = addx
                run_command_arg = int(arg)
            else:
                print(f"Unknown command {command}")
        elif next_pop < clock:
            print("We missed it")

        if X - 1 <= (clock - 1) % 40 <= X + 1:
            SCREEN += "#"
        else:
            SCREEN += "."
        show(debug)

        clock += 1

        if next_pop == clock and run_command and run_command_arg:
            run_command(run_command_arg, debug)

        next_pop = pop

    return results


def addx(arg, debug):
    global X

    if debug:
        print(f"\t$ addx({arg})  X {X} --> {X + arg}")
    X += arg


def show(debug):  # pylint: disable=unused-argument
    start = 0
    print()

    while True:
        print(SCREEN[start : start + 40])
        start += 40
        if len(SCREEN) < start:
            break


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # 13140
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 15140
    # print("Test2: ", run(part=2, test_run=True, debug=True))  #
    print("Real2: ", run(part=2, test_run=False, debug=False))  # BBPJAZGAP
