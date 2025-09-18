"""
--- Day 7: Some Assembly Required ---
This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

Your puzzle answer was 46065.

--- Part Two ---
Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?

Your puzzle answer was 14134.
"""

BIT_WIDTH = 16
BIT_MASK = (1 << BIT_WIDTH) - 1


def run(part: int, output_wire: str, test_suffix: str = "", debug: bool = False):
    y, d = __file__.split("advent-")[1].split("-day")
    file_name = f"{y}/input/{d.strip('.py')}{test_suffix}.txt"

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data if not x.startswith("#")]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, output_wire=output_wire, debug=debug)


def get_value(x: int | str, wires: dict[str, int]) -> int:
    if isinstance(x, int):
        return x

    if isinstance(x, str) and x.isdigit():
        return int(x)

    return wires[x]


def part1(data: list[str], output_wire: str, debug: bool = False) -> int:
    results = 0
    wires: dict[str, int] = {}

    results = get_results(data, wires, debug)[output_wire]

    return results


def get_results(data: list[str], wires: dict[str, int], debug: bool) -> dict[str, int]:
    while len(data):
        line = data.pop(0)
        op1, op2 = "", ""

        left, wire = line.split(" -> ")

        try:
            if "AND" in left:
                op1, op2 = left.split(" AND ")
                wires[wire] = get_value(op1, wires) & get_value(op2, wires)
            elif "OR" in left:
                op1, op2 = left.split(" OR ")
                wires[wire] = get_value(op1, wires) | get_value(op2, wires)
            elif "LSHIFT" in left:
                op1, op2 = left.split(" LSHIFT ")
                wires[wire] = get_value(op1, wires) << int(op2)
            elif "RSHIFT" in left:
                op1, op2 = left.split(" RSHIFT ")
                wires[wire] = get_value(op1, wires) >> int(op2)
            elif "NOT" in left:
                _, op1 = left.split("NOT ")
                wires[wire] = ~get_value(op1, wires) & BIT_MASK
            else:
                if wire not in wires:
                    wires[wire] = get_value(left, wires)
        except KeyError:
            # The value that we are looking for was not calculated yet. Push to the bottom of the list
            data.append(line)
            if debug:
                print(f"List length: {len(data)}")

    return wires


def part2(data: list[str], output_wire: str, debug: bool = False) -> int:
    results = 0
    wires: dict[str, int] = {}

    a_results = get_results(data.copy(), wires, debug)[output_wire]
    wires = {"b": a_results}

    results = get_results(data.copy(), wires, debug)[output_wire]

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, output_wire="d", test_suffix="-test", debug=True))  # 72
    # print("Real1: ", run(part=1, output_wire="a", debug=False))  # 46065
    # print("Test2: ", run(part=2, output_wire="d", test_suffix="-test", debug=True))  # 72
    print("Real2: ", run(part=2, output_wire="a", debug=False))  # 14134
