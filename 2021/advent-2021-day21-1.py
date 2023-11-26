DATA_TEST = ['Player 1 starting position: 4','Player 2 starting position: 8']
DATA = ['Player 1 starting position: 2','Player 2 starting position: 5']

def run(p1, p2):
    roll_count = 0
    p1_score, p2_score = 0, 0
    die = roll_die()
    turn = p1
    while max(p1_score, p2_score) < 1000:
        roll_count += 3
        roll = die.__next__()
        print(f"{roll_count}: {roll}: {p1_score, p2_score}")
       # roll_total = sum([x for x in die])
        if turn is p1:
            p1 += roll
            p1_score += get_score(p1)
            turn = p2
        else:
            p2 += roll
            p2_score += get_score(p2)
            turn = p1

    results = min(p1_score, p2_score) * roll_count

    return results

def get_score(score):
    score = score % 10
    if score == 0:
        return 10
    return score

def roll_die(count=3):
    i = 0
    results = 0
    while True:
        for _ in range(count):
            i += 1
            if i == 101:
                i = 1
            results += i

        yield results
        results = 0

if __name__ == "__main__":
    data = DATA
    p1 = data[0]
    p1 = int(p1.split(': ')[1])
    p2 = data[1]
    p2 = int(p2.split(': ')[1])
    results = run(p1, p2)
    print (results)
