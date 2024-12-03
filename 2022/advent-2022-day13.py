from ast import literal_eval

FILE_NAME = "2022/input/13.txt"


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


class Thing:
    def __init__(self, item):
        self.item = literal_eval(item)

    def __lt__(self, right):
        result = compare(self.item, right.item)
        return result == 1

    def __gt__(self, right):
        result = compare(self.item, right.item)
        return result == -1

    def __eq__(self, right):
        result = compare(self.item, right.item)
        return result == 0

    def __str__(self):
        return str(self.item)

    def __repr__(self):
        return str(self.item)


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        # int compare
        if left < right:
            return 1
        if left > right:
            return -1
        return 0

    if isinstance(left, list) and isinstance(right, list):
        for i, start in enumerate(left):
            if i >= len(right):
                return -1

            result = compare(start, right[i])
            if result != 0:
                return result

        # same so far:
        if len(left) < len(right):
            return 1
        if len(left) > len(right):
            return -1
        return 0

    if type(left) is not type(right):
        if isinstance(left, list) and isinstance(right, int):
            right = [right]
        elif isinstance(left, int) and isinstance(right, list):
            left = [left]
        else:
            raise Exception("Unknown type combo", type(left), type(right))
    return compare(left, right)


def part1(data: list[str], debug: bool = False) -> int:
    right_orders = []
    row = 0

    while len(data) > 0:
        row += 1
        left = literal_eval(data.pop(0))
        right = literal_eval(data.pop(0))
        if len(data) > 0:
            data.pop(0)

        if debug:
            print(row, left, right)

        result = 0
        for i, _ in enumerate(left):
            if i >= len(right):
                break
            result = compare(left[i], right[i])
            if result == 1:
                right_orders.append(row)
                break
            if result == -1:
                break

        if result == 0 and len(left) < len(right):
            right_orders.append(row)

    if debug:
        print("right order", right_orders)

    return sum(right_orders)


def part2(data: list[str], debug: bool = False) -> int:
    items = []
    data.append("[[2]]")
    data.append("[[6]]")

    while len(data) > 0:
        item = data.pop(0)
        if item == "":
            continue
        items.append(Thing(item))

    items = sorted(items)

    i2 = items.index(Thing("[[2]]")) + 1
    i6 = items.index(Thing("[[6]]")) + 1

    if debug:
        print(f"{i2=}, {i6=}")
    return i2 * i6


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # 13
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 5198
    # print("Test2: ", run(part=2, test_run=True, debug=True))  # 140
    print("Real2: ", run(part=2, test_run=False, debug=False))  # 22344
