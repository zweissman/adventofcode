"""
--- Day 7: Some Assembly Required ---
This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately,
little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535).
A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a
signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until
all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect
wires x and y to an AND gate, and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to
emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide
operators for these gates.

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

"""


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
    wires = {}

    for line in data:
        op1, op2 = ""

        left, wire = line.split(" -> ")

        if "AND" in left:
            op1, op2 = left.split(" AND ")
        elif "OR" in left:
            op1, op2 = left.split(" OR ")
        elif "LSHIFT" in left:
            op1, op2 = left.split(" LSHIFT ")
        elif "RSHIFT" in left:
            op1, op2 = left.split(" RSHIFT ")
        elif "NOT" in left:
            op1, _ = left.split("NOT ")
            if op1 in wires:
                op1 = wires[op1]
            wires[wire] = int(not int(op1))
        else:
            wires[wire] = left
            continue

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0

    return results


if __name__ == "__main__":
    op1 = "8"
    #    print(int(not int(op1, 2)))
    print(bin(op1))

    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  #
    # print("Real1: ", run(part=1, debug=False))  #
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  #
    # print("Real2: ", run(part=2, debug=False))  #
