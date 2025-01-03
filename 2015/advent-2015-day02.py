"""
--- Day 2: I Was Told There Would Be No Math ---
The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the
dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required
wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l.
The elves also need a little extra paper for each present: the area of the smallest side.

For example:

A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet
of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot
of slack, for a total of 43 square feet.
All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

---- part 2
The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length
they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one
face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow
is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

For example:

A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of
ribbon for the bow, for a total of 34 feet.
A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of
ribbon for the bow, for a total of 14 feet.
How many total feet of ribbon should they order?
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

    for line in data:
        ws, hs, ls = line.split("x")
        w, h, l = int(ws), int(hs), int(ls)
        slack = min(w * h, h * l, w * l)
        area = (2 * w * h) + (2 * h * l) + (2 * w * l) + slack

        if debug:
            print(line, area)
        results += area

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0

    for line in data:
        ws, hs, ls = line.split("x")
        w, h, l = int(ws), int(hs), int(ls)
        slack = min(2 * w + 2 * h, 2 * h + 2 * l, 2 * w + 2 * l)
        area = (w * h * l) + slack

        if debug:
            print(line, area)
        results += area

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 101
    # print("Real1: ", run(part=1, debug=False))  # 1606483
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # 48
    print("Real2: ", run(part=2, debug=False))  # 3842356
