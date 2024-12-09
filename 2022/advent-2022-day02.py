FILE_NAME = "2022/input/02.txt"


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
    score = 0

    for row in data:
        them = row[0]
        me = row[2]
        if debug:
            print(them, me)
        if me == "X":
            score = 1
            if them == "A":
                score += 3
            elif them == "C":
                score += 6
        elif me == "Y":
            score = 2
            if them == "B":
                score += 3
            elif them == "A":
                score += 6
        else:
            score = 3
            if them == "C":
                score += 3
            elif them == "B":
                score += 6
        if debug:
            print(score)
        results += score

    return results


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    score = 0

    for row in data:
        them = row[0]
        outcome = row[2]
        if debug:
            print(them, outcome)

        # A X Rock
        # B Y Paper
        # C Z Sciss

        if outcome == "X":
            # lose
            score = 0
            if them == "A":
                me = "Z"
            elif them == "B":
                me = "X"
            else:
                me = "Y"
        elif outcome == "Y":
            # Draw
            score = 3
            if them == "A":
                me = "X"
            elif them == "B":
                me = "Y"
            else:
                me = "Z"
        else:
            # Win
            score = 6
            if them == "A":
                me = "Y"
            elif them == "B":
                me = "Z"
            else:
                me = "X"

        if me == "X":
            score += 1
        elif me == "Y":
            score += 2
        else:
            score += 3

        if debug:
            print("me", me)
        if debug:
            print("score", score)
        results += score

    return results


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # 15
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 14531
    # print("Test2: ", run(part=2, test_run=True, debug=True))  # 12
    print("Real2: ", run(part=2, test_run=False, debug=False))  # 11258
