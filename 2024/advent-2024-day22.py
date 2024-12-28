from collections import defaultdict


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

    steps = 2000
    for secret_str in data:
        secret = int(secret_str)
        for _ in range(steps):
            secret = ((secret * 64) ^ secret) % 16777216
            secret = ((secret // 32) ^ secret) % 16777216
            secret = ((secret * 2048) ^ secret) % 16777216

        results += secret
        if debug:
            print(secret_str, secret)

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    # show(data, debug=debug)
    last_prices = [0, 0, 0, 0]
    price_history_all = defaultdict(list)
    steps = 2000

    for secret_str in data:
        price_history = {}
        secret = int(secret_str)
        last_price = int(str(secret)[-1])
        last_prices.pop(0)
        last_prices.append(last_price)

        for step in range(steps):
            secret = ((secret * 64) ^ secret) % 16777216
            secret = ((secret // 32) ^ secret) % 16777216
            secret = ((secret * 2048) ^ secret) % 16777216

            price = int(str(secret)[-1])
            delta = price - last_price
            last_price = price
            last_prices.pop(0)
            last_prices.append(delta)
            last_price_key = ",".join([str(x) for x in last_prices])

            if step > 4 - 3:
                if last_price_key not in price_history:
                    price_history[last_price_key] = price
                    price_history_all[last_price_key].append(price)

                if debug:
                    print(delta, "\t", secret, price, ",".join([str(x) for x in last_prices]))
                    print(price, last_price_key)

    largest = 0
    largest_key = ""
    for k, v in price_history_all.items():
        total = sum(v)
        if total > largest:
            largest = total
            largest_key = k

    results = largest
    print(largest_key)

    return results


def show(grid: list[str], debug: bool = False) -> None:
    if debug:
        print()
        for y, row in enumerate(grid):
            print(f"{y:02}", "".join([str(x) for x in row]))


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test1a", debug=True))  # 37327623
    # print("Real1: ", run(part=1, debug=False))  # 12664695565
    # print("Test2: ", run(part=2, test_suffix="-test2b", debug=True))  # 23
    print("Real2: ", run(part=2, debug=False))  # 1444
