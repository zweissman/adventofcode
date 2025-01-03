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

    hands: dict = {}
    for row in data:
        hand, bid = row.split(" ")
        hand = (
            hand.replace("A", "E")
            .replace("T", "A")
            .replace("J", "B")
            .replace("Q", "C")
            .replace("K", "D")
        )
        name = name_hand(hand, 1, debug)
        if debug:
            print(name)

        if name in hands:
            hands[name].append((hand, bid))
        else:
            hands[name] = [(hand, bid)]

    hands = {
        k: v for k, v in sorted(hands.items(), key=lambda item: (item[0], item[1][0]), reverse=True)
    }

    if debug:
        print(hands)
    rank = 1
    for k, v in hands.items():
        for z in sorted(v):
            results += rank * int(z[1])
            rank += 1

    return results


def name_hand(hand: str, part: int, debug: bool) -> int:
    if debug:
        print(hand)
    hand = "".join(sorted(list(hand)))
    hand_dict: dict[str, int] = {}
    jokers = 0
    for c in hand:
        if c == "0":
            jokers += 1
        elif c in hand_dict:
            hand_dict[c] += 1
        else:
            hand_dict[c] = 1

    sorted_hand_dict = {
        k: v for k, v in sorted(hand_dict.items(), key=lambda item: item[1], reverse=True)
    }
    if debug:
        print(sorted_hand_dict)

    if part == 2:
        if jokers == 5:
            sorted_hand_dict["0"] = jokers
        elif jokers > 0:
            top_card = list(sorted_hand_dict.keys())[0]
            if debug:
                print(top_card)
            sorted_hand_dict[top_card] += jokers

    for k, v in sorted_hand_dict.items():
        if v == 5:
            return 1  # 5-of-a-kind
        if v == 4:
            return 2  # 4-of-a-kind
        if v == 3:
            if 2 in sorted_hand_dict.values():
                return 3  # full house
            else:
                return 4  # 3-of-a-kind
        if v == 2:
            if len(sorted_hand_dict) == 3:
                return 5  # 2 pairs
            else:
                return 6  # 1 pair
        return 7  # high card

    return 0


def part2(data: list[str], debug: bool = False) -> int:
    results = 0

    hands: dict[int, list[tuple]] = {}
    for row in data:
        hand, bid = row.split(" ")
        hand = (
            hand.replace("A", "E")
            .replace("T", "A")
            .replace("J", "0")  # joker is weakest rank
            .replace("Q", "C")
            .replace("K", "D")
        )
        name = name_hand(hand, 2, debug)
        if debug:
            print(name)

        if name in hands:
            hands[name].append((hand, bid))
        else:
            hands[name] = [(hand, bid)]

    hands = {
        k: v for k, v in sorted(hands.items(), key=lambda item: (item[0], item[1][0]), reverse=True)
    }

    if debug:
        print(hands)
    rank = 1
    for k, v in hands.items():
        for z in sorted(v):
            results += rank * int(z[1])
            rank += 1

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 6440
    # print("Real1: ", run(part=1, debug=False))  # 253866470
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # 5905
    print("Real2: ", run(part=2, debug=False))  # 254494947
