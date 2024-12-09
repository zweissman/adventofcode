FILE_NAME = "2022/input/11.txt"


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
    results = 0
    monkeys = {}

    while len(data) > 0:
        monkey_id = int(data.pop(0).replace("Monkey ", "").strip(":"))
        items = data.pop(0).replace("Starting items: ", "")
        items = items.split(", ")
        operation = data.pop(0).replace("Operation: new = old ", "")
        operation, value = operation.split(" ")
        if value != "old":
            value = int(value)
        else:
            value = None
        test = int(data.pop(0).replace("Test: divisible by ", ""))
        t = int(data.pop(0).replace("If true: throw to monkey ", ""))
        f = int(data.pop(0).replace("If false: throw to monkey ", ""))
        if len(data) > 0:
            data.pop(0)
        monkey = {
            "items": items,
            "operation": operation,
            "test": test,
            "t": t,
            "f": f,
            "count": 0,
        }
        if value:
            monkey["value"] = value
        monkeys[monkey_id] = monkey

    if debug:
        print(monkeys)

    for stage in range(20):
        if debug:
            print(f"Round {stage + 1}")
        for monkey_id, monkey in monkeys.items():
            items = monkey["items"]
            operation = monkey["operation"]
            test = monkey["test"]
            while len(items) > 0:
                item = int(items.pop(0))
                monkey["count"] = monkey["count"] + 1
                value = int(monkey.get("value", item))

                if operation == "*":
                    worry = item * value
                elif operation == "+":
                    worry = item + value
                else:
                    raise Exception(f"Unknown operation {operation}")

                worry = int(worry / 3)
                if worry % test == 0:
                    throw_to = monkey["t"]
                else:
                    throw_to = monkey["f"]
                monkeys[throw_to]["items"].append(worry)

    counts = []
    for _, monkey in monkeys.items():
        counts.append(monkey["count"])

    counts.sort(reverse=True)
    if debug:
        print(counts)
    results = counts[0] * counts[1]
    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    monkeys = {}
    lcm = 1

    while len(data) > 0:
        monkey_id = int(data.pop(0).replace("Monkey ", "").strip(":"))
        items = data.pop(0).replace("Starting items: ", "")
        items = items.split(", ")
        items = [int(x) for x in items]
        operation = data.pop(0).replace("Operation: new = old ", "")
        operation, value = operation.split(" ")
        if value != "old":
            value = int(value)
        else:
            value = None
        test = int(data.pop(0).replace("Test: divisible by ", ""))
        lcm *= test
        t = int(data.pop(0).replace("If true: throw to monkey ", ""))
        f = int(data.pop(0).replace("If false: throw to monkey ", ""))
        if len(data) > 0:
            data.pop(0)
        monkey = {
            "items": items,
            "operation": operation,
            "test": test,
            "t": t,
            "f": f,
            "count": 0,
        }
        if value:
            monkey["value"] = value
        monkeys[monkey_id] = monkey

    if debug:
        print(monkeys)

    for stage in range(10000):
        # if round % 20 == 0: print(f"Round {round + 1}")

        if stage % 1000 == 0:
            print(f"Round {stage + 1}")
            print([monkey["count"] for _, monkey in monkeys.items()])

        for monkey_id, monkey in monkeys.items():
            items = monkey["items"]
            operation = monkey["operation"]
            test = monkey["test"]
            while len(items) > 0:
                item = items.pop(0)
                monkey["count"] = monkey["count"] + 1
                value = int(monkey.get("value", item))

                if operation == "*":
                    worry = item * value
                elif operation == "+":
                    worry = item + value
                else:
                    raise Exception(f"Unknown operation {operation}")

                #                worry = int(worry / 3)
                if worry % test == 0:
                    throw_to = monkey["t"]
                else:
                    throw_to = monkey["f"]

                worry %= lcm
                monkeys[throw_to]["items"].append(worry)

    counts = []
    for _, monkey in monkeys.items():
        counts.append(monkey["count"])

    counts.sort(reverse=True)
    if debug:
        print(counts)
    results = counts[0] * counts[1]
    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # 10605
    print("Real1: ", run(part=1, test_run=False, debug=False))  # 69918
    # print("Test2: ", run(part=2, test_run=True, debug=True))  # 2713310158
    print("Real2: ", run(part=2, test_run=False, debug=False))  # 19573408701
