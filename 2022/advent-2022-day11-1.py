from collections import defaultdict

DATA_TEST = [
    "Monkey 0:",
    "  Starting items: 79, 98",
    "  Operation: new = old * 19",
    "  Test: divisible by 23",
    "    If true: throw to monkey 2",
    "    If false: throw to monkey 3",
    "",
    "Monkey 1:",
    "  Starting items: 54, 65, 75, 74",
    "  Operation: new = old + 6",
    "  Test: divisible by 19",
    "    If true: throw to monkey 2",
    "    If false: throw to monkey 0",
    "",
    "Monkey 2:",
    "  Starting items: 79, 60, 97",
    "  Operation: new = old * old",
    "  Test: divisible by 13",
    "    If true: throw to monkey 1",
    "    If false: throw to monkey 3",
    "",
    "Monkey 3:",
    "  Starting items: 74",
    "  Operation: new = old + 3",
    "  Test: divisible by 17",
    "    If true: throw to monkey 0",
    "    If false: throw to monkey 1",
]
DATA = [
    "Monkey 0:",
    "  Starting items: 74, 73, 57, 77, 74",
    "  Operation: new = old * 11",
    "  Test: divisible by 19",
    "    If true: throw to monkey 6",
    "    If false: throw to monkey 7",
    "",
    "Monkey 1:",
    "  Starting items: 99, 77, 79",
    "  Operation: new = old + 8",
    "  Test: divisible by 2",
    "    If true: throw to monkey 6",
    "    If false: throw to monkey 0",
    "",
    "Monkey 2:",
    "  Starting items: 64, 67, 50, 96, 89, 82, 82",
    "  Operation: new = old + 1",
    "  Test: divisible by 3",
    "    If true: throw to monkey 5",
    "    If false: throw to monkey 3",
    "",
    "Monkey 3:",
    "  Starting items: 88",
    "  Operation: new = old * 7",
    "  Test: divisible by 17",
    "    If true: throw to monkey 5",
    "    If false: throw to monkey 4",
    "",
    "Monkey 4:",
    "  Starting items: 80, 66, 98, 83, 70, 63, 57, 66",
    "  Operation: new = old + 4",
    "  Test: divisible by 13",
    "    If true: throw to monkey 0",
    "    If false: throw to monkey 1",
    "",
    "Monkey 5:",
    "  Starting items: 81, 93, 90, 61, 62, 64",
    "  Operation: new = old + 7",
    "  Test: divisible by 7",
    "    If true: throw to monkey 1",
    "    If false: throw to monkey 4",
    "",
    "Monkey 6:",
    "  Starting items: 69, 97, 88, 93",
    "  Operation: new = old * old",
    "  Test: divisible by 5",
    "    If true: throw to monkey 7",
    "    If false: throw to monkey 2",
    "",
    "Monkey 7:",
    "  Starting items: 59, 80",
    "  Operation: new = old + 6",
    "  Test: divisible by 11",
    "    If true: throw to monkey 2",
    "    If false: throw to monkey 3",
]


def run(data, debug=False):
    results = 0
    monkeys = {}

    while len(data) > 0:
        monkey_id = int(data.pop(0).replace("Monkey ", "").strip(":"))
        items = data.pop(0).replace("  Starting items: ", "")
        items = items.split(", ")
        operation = data.pop(0).replace("  Operation: new = old ", "")
        operation, value = operation.split(" ")
        if value != "old":
            value = int(value)
        else:
            value = None
        test = int(data.pop(0).replace("  Test: divisible by ", ""))
        t = int(data.pop(0).replace("    If true: throw to monkey ", ""))
        f = int(data.pop(0).replace("    If false: throw to monkey ", ""))
        if len(data) > 0:
            data.pop(0)
        monkey = {"items": items, "operation": operation, "test": test, "t": t, "f": f, "count": 0}
        if value:
            monkey["value"] = value
        monkeys[monkey_id] = monkey

    if debug:
        print(monkeys)

    for round in range(20):
        if debug:
            print(f"Round {round + 1}")
        for monkey_id, monkey in monkeys.items():
            items = monkey["items"]
            operation = monkey["operation"]
            test = monkey["test"]
            while len(items) > 0:
                item = int(items.pop(0))
                monkeys[monkey_id]["count"] = monkeys[monkey_id]["count"] + 1
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


if __name__ == "__main__":
    #    results = run(DATA_TEST, debug=True)
    results = run(DATA, debug=False)
    print("ANSWER:", results)
