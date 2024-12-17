def run(part: int, test_suffix: str = "", debug: bool = False):
    y, d = __file__.split("advent-")[1].split("-day")
    file_name = f"{y}/input/{d.strip('.py')}{test_suffix}.txt"

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def part1(data: list[str], debug: bool = False) -> str:
    results = ""

    while True:
        a = int(data.pop(0).replace("Register A: ", ""))
        b = int(data.pop(0).replace("Register B: ", ""))
        c = int(data.pop(0).replace("Register C: ", ""))
        data.pop(0)
        program_str = data.pop(0).replace("Program: ", "")
        programs = [int(x) for x in program_str.split(",")]

        if debug:
            print(a, b, c, programs)

        results = run_program(a, b, c, programs)
        if debug:
            print(results)

        if len(data) == 0:
            break

        data.pop(0)

    return results


def run_program(a: int, b: int, c: int, programs: list[int]) -> str:
    results = []
    i = 0
    while i < len(programs):
        op = programs[i]
        combo = programs[i + 1]

        if combo == 4:
            combo_val = a
        elif combo == 5:
            combo_val = b
        elif combo == 6:
            combo_val = c
        else:
            combo_val = combo

        if op == 0:  # adv
            a = int(a / 2**combo_val)
        elif op == 1:  # bxl
            b = b ^ combo
        elif op == 2:  # bst
            b = combo_val % 8
        elif op == 3:  # jnz
            if a == 0:
                pass
            else:
                i = combo - 2

        elif op == 4:  # bxc
            b = b ^ c
        elif op == 5:  # out
            results.append(str(combo_val % 8))
        elif op == 6:  # bdv
            b = int(a / 2**combo_val)
        elif op == 7:  # cdv
            c = int(a / 2**combo_val)
        else:
            raise Exception(f"Should not get an op {op}")

        i += 2

    return ",".join(results)


def part2(data: list[str], debug: bool = False) -> int:
    results = ""

    a = int(data.pop(0).replace("Register A: ", ""))
    b = int(data.pop(0).replace("Register B: ", ""))
    c = int(data.pop(0).replace("Register C: ", ""))
    data.pop(0)
    program_str = data.pop(0).replace("Program: ", "")
    programs = [int(x) for x in program_str.split(",")]

    if debug:
        print(a, b, c, programs)

    matches = []
    previous = 0
    for i in range(37221266013684, 2**45, -68719476736 // (2**19)):
        results = run_program(i, b, c, programs)
        if results.startswith("2,4,1,2,7,5,4,1,1,3,5,5"):
            matches.append(i)
            print(i, results, previous - i)
            previous = i

        if results == program_str:
            print("REAL", i)

    return i


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test1a", debug=True))  # 4,6,3,5,6,3,5,2,1,0
    # print("Real1: ", run(part=1, debug=False))  # 1,7,2,1,4,1,5,4,0
    # print("Test2: ", run(part=2, test_suffix="-test2b", debug=True))  # 117440
    print("Real2: ", run(part=2, debug=False))  # 37221261688308
