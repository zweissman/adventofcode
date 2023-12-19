# pylint: disable=too-many-return-statements,too-many-statements,too-many-branches,duplicate-code,unused-argument
# pylint: disable=unnecessary-list-index-lookup

from collections import deque
import pprint

pp = pprint.PrettyPrinter()

FILE_NAME = "2023/input/19.txt"


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


def show(grid: list[list[str]], debug: bool = False):
    if debug:
        print()
        for y in range(len(grid)):
            print("".join([str(x) for x in grid[y]]))


def part1(data: list[str], debug: bool = False) -> int:
    results = 0
    commands = {}
    parts = []

    run_objects = False
    for line in data:
        if line == "":
            run_objects = True
            continue

        if not run_objects:
            command_key, params = line.strip().split("{")
            command_params = params.strip("}").split(",")
            command: list[str | tuple[str, str, int, str]] = []
            for command_param in command_params:
                if ":" in command_param:
                    k, v = command_param.split(":")
                    key = k[:1]
                    compare = k[1:]

                    test = compare[:1]
                    test_value = compare[1:]

                    command.append((key, test, int(test_value), v))
                else:
                    command.append(command_param)

            commands[command_key] = command
        else:
            part_params = line.strip("{").strip("}").split(",")
            part: dict[str, int] = {}
            for object_param in part_params:
                k, v = object_param.split("=")
                part[k] = int(v)

            parts.append(part)

    for part in parts:
        workflow = "in"

        if debug:
            print(part)
        while workflow not in ["A", "R"]:
            workflow = calc_result(part, commands[workflow], workflow, debug)

        if workflow == "A":
            result = 0
            for _, value in part.items():
                result += value

            if debug:
                print(f"Accepted {result=} {part=}\n")
            results += result
        else:
            if debug:
                print(f"Rejected {part=}\n")

    return results


def calc_result(
    part: dict[str, int], commands: list, workflow: str, debug: bool
) -> str:
    if debug:
        print(f"{workflow}: {commands}")

    for command in commands:
        if isinstance(command, str):
            return command

        key, test, value, new_workflow = command
        if key not in part:
            continue

        if test == ">":
            if part[key] > value:
                return new_workflow
        elif test == "<":
            if part[key] < value:
                return new_workflow
        else:
            raise Exception(f"Unknown test operator {test} for {part=}")

    raise Exception("Result not found")


def get_range(test, value, param):
    low, high = param[0], param[1]

    if test == ">":
        low = max(low, value + 1)
    elif test == "<":
        high = min(high, value - 1)
    elif test == ">=":
        low = max(low, value)
    elif test == "<=":
        high = min(high, value)
    else:
        raise Exception(f"Unknown test in get_range {test}")

    return (low, high)


def get_ranges(param, test, value, xmas):
    x, m, a, s = xmas
    if param == "x":
        x = get_range(test, value, x)
    elif param == "m":
        m = get_range(test, value, m)
    elif param == "a":
        a = get_range(test, value, a)
    elif param == "s":
        s = get_range(test, value, s)
    else:
        raise Exception(f"Unknown parameter in get_ranges {param}")

    return (x, m, a, s)


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    commands = {}

    for line in data:
        if line == "":
            break

        command_key, params = line.strip().split("{")
        command_params = params.strip("}").split(",")
        command: list[str | tuple[str, str, int, str]] = []
        for command_param in command_params:
            if ":" in command_param:
                k, v = command_param.split(":")
                key = k[:1]
                compare = k[1:]

                test = compare[:1]
                test_value = compare[1:]

                command.append((key, test, int(test_value), v))
            else:
                command.append(command_param)

        commands[command_key] = command

    default_range = (1, 4000)
    q = deque([("in", ((default_range,) * 4))])
    while q:
        workflow, xmas = q.pop()
        if workflow == "R":
            continue
        if workflow == "A":
            result = get_score(xmas)
            results += result
            continue

        rule = commands[workflow]

        for parts in rule:
            if isinstance(parts, str):
                q.append((parts, xmas))
                break

            key, test, value, new_workflow = parts

            q.append((new_workflow, get_ranges(key, test, value, xmas)))
            xmas = get_ranges(key, "<=" if test == ">" else ">=", value, xmas)

    return results


def get_score(params: tuple) -> int:
    results = 1

    for param in params:
        results = results * (param[1] - param[0] + 1)

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # 19114
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 325952
    # print("Test2: ", run(part=2, test_run=True, debug=True))  # 167409079868000
    print("Real2: ", run(part=2, test_run=False, debug=False))  # 125744206494820
