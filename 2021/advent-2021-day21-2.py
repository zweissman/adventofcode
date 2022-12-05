import functools

DATA_TEST = ['Player 1 starting position: 4','Player 2 starting position: 8']
DATA = ['Player 1 starting position: 2','Player 2 starting position: 5']

@functools.cache
def play_turn(p1, p2, p1_score, p2_score):
    p1_wins_total, p2_wins_total = 0, 0
    rolls = get_dice_combos()
    
    for roll in rolls:
        score = get_score(p1 + roll)
        
        if p1_score + score >= 21:
            p1_wins_total += 1
            continue
        
        p2_wins, p1_wins = play_turn(p2, p1 + roll, p2_score, p1_score + score)
        p1_wins_total += p1_wins
        p2_wins_total += p2_wins
        
    return p1_wins_total, p2_wins_total

def get_dice_combos(sides=3):
    for x in range(1, sides + 1):
        for y in range(1, sides + 1):
            for z in range(1, sides + 1):
                yield x + y + z

def get_score(score):
    score = score % 10
    if score == 0:
        return 10
    return score

if __name__ == "__main__":
    data = DATA
    p1 = data[0]
    p1 = int(p1.split(': ')[1])
    p2 = data[1]
    p2 = int(p2.split(': ')[1])
#    universes = Counter()
#    universes[(p1, p2, 0, 0, 1)] = 1

    p1_wins_total, p2_wins_total = play_turn(p1, p2, 0, 0)
    results = max(p1_wins_total, p2_wins_total)

#    results = run(universes)    
    print (results)
