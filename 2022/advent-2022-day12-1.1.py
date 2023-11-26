DATA_TEST = ["Sabqponm", "abcryxxl", "accszExk", "acctuvwj", "abdefghi"]
DATA = [
    "abaaaaaaaaccccccccccccccccccaaaaaccccaaaaaaccccccccccccccccccccccaaaaaaaaaacccccccccccccccccccccccccccccccaaaaaccccccccccccccccccccccccccccccccccccccccccaaaaaa",
    "abaaaaaaaacccccccccccccccccccaaaaaccccaaaacccccaaaacccccccccccccccaaaaaaaaaacccccccccccccccccccccccccccccaaaaaaccccccccccccccccccccccccccccccccccccccccccccaaaa",
    "abccaaaaaaccccccccccccccccccaaaaaaccccaaaaccccaaaaaccccccccccaaaaaaaaaaaaaaacccccccccccccccccccccccccccccaaaacccccccccccccccccccccccccccccaaaccccccccccccccaaaa",
    "abcaaaaaaaccccccccccccccccccaaaaccccccaccaccccaaaaaacccccccccaaaaaaaaaaaaaaacccccccccccccccccccccacccccccccaacccccccccccccccccccccccccccccaaaccccccccccccccaaaa",
    "abccaacccaccccccccccccccccccccaaacccccccccccccaaaaaaccccccccccaaaaaaaaacaaacccccccccccccccccccaaaacccccccccccccccccccccccccaacccccccaaccccaaacccccccccccccaaaaa",
    "abcaaaaaacccccccccccccccccccccccccccccccccccccaaaaaccccccccccaaaaaaaaaaccccaacaaccccccccccccccaaaaaacccccccccccccccccccccccaacccccccaaaacaaaaccccccccccccccaccc",
    "abccaaaaacccccccccccccccccccccccccccccccccccaaccaaacccccccccaaaaaaaaaaaacccaaaaccccccccccccccccaaaaacccccccccccccccaacaaaaaaacccccccaaaaaaaaacccccccccccccccccc",
    "abccaaaaaacccccccccccccccccccccccccccccaaacaaaccccccccccccccaaaaaaaaaaacccaaaaacccccccccccccccaaaaacccccccccccccaaaaaccaaaaaaaaccccccaaaaaalllllllcccaacccccccc",
    "abccaaaaaaccccccaaaaacccccccccaaaccccccaaaaaaaccccccccccccccaaacaaacaaacccaaaaaaccccccccccccccaccaaccccccccccccccaaaaacaaaaaaaaajkkkkkkkkkklllllllccccaaaaacccc",
    "abccaaaaacccccccaaaaacccccccccaaaaccccccaaaaaaccccccccaacaacccccaaacccccccacaaaaccccccccaaaccccccccccccccccccccccaaaaaccaaaaaaajjkkkkkkkkkkllssllllcccaaaaacccc",
    "abcccaaaaccccccaaaaaacccccccccaaaaccccccaaaaaaaaccccccaaaaacccccaaccccccccccaacccccccccaaaacccccccccccccccaaccccaaaaaccaaaaaacjjjjkkkkkkkkssssssslllccaaaaccccc",
    "abcccccccccccccaaaaaacccccccccaaaccccccaaaaaaaaacaaccccaaaaacccccccccccccccaaccccccccccaaaaccccccccccccccaaacccccccaaccaaaaaajjjjrrrrrrsssssssssslllcccaaaccccc",
    "abcccccccccccccaaaaaacccccccccccccccccaaaaaaaaaaaaaaacaaaaaacccccccccccaaacaacccccccccccaaaccccaaacccccaaaaaaaaccccccccaacaaajjjrrrrrrrsssssuusssslmcccaaaacccc",
    "abcccccccccccccccaacccccccccccccccaacaaaacaaaccaaaaaacaaaaccccccccccccccaaaaaccccccccccccccccccaaaaacccaaaaaaaaccccccccccccaajjjrrrruuurssuuuuvsqqmmcddaaaacccc",
    "abccccccccccccccccccccccccccccccccaaaaacccaaacccaaaaccccaaccccccccccccccaaaaaaacccccccccccccccaaaaaaccccaaaaaacccccccccccccccjjrrruuuuuuuuuuuuvvqqmmmdddccccccc",
    "abcccccccccccccccccccccccacccccccccaaaaaccaaacccaaaaccccccccccccccccccccaaaaaaacccccccccccccccaaaaaaccccaaaaaacccccccccaaccccjjjrrtuuuuuuuuyyvvvqqmmmddddcccccc",
    "abccccccccccccccccccccaaaaccccccccaaaaaacccccaacaccacccccccccccccccccccaaaaaaccccccccccccccccccaaaaaccccaaaaaaccccccccaaaccccjjjrrttuxxxuuxyyyvvqqmmmmdddcccccc",
    "abcccccccccaacccccccccaaaaaaccccccaaaaccccccaaaccccccccccccccccccccccccaacaaaccccccccccccccccccaacaaccccaaccaaccccaaaaaaaccccjjjrrtttxxxxxyyyyvvqqqmmmddddccccc",
    "abccccccccaaaacccccccccaaaacccccccccaaccccccaaacaaaccccccccccccccccccaaccccaacccccccccccccccccccccccccccccccccccccaaaaaaaaaacijjqrtttxxxxxyyyvvvqqqqmmmdddccccc",
    "abcccccacaaaaaccccccccaaaaaccccccccccccccaaaaaaaaaacccccccccccccccccaaaccccccccccccccccccccccccccccccccccccccccccccaaaaaaaaaciiiqqqttxxxxxyyyvvvvqqqqmmmdddcccc",
    "SbcccccaaaaaaaaaacccccaacaaccccccccccccccaaaaaaaaaccccccccccccccaaacaaacccccccccccccccccccccccccccccccccccccccccccccaaaaaaaciiiqqqtttxxxEzzyyyyvvvqqqmmmdddcccc",
    "abcccccaaaaaaaaaaccccccccccccaaccccccccccccaaaaaccccccccccccccccaaaaaaaaaacccccccaacccccccccccccaacccccccccccccccccaaaaaaccciiiqqqttxxxxyyyyyyyyvvvqqqmmmeddccc",
    "abcccccccaaaaaacccccccccccaaaaccccccccccaaaaaaaaacccccccaaaacccccaaaaaaaaacccccaaaaccccccccccaacaaaccccccccccccccccaaaaaaaciiiqqqtttxxyyyyyyyyyvvvvqqqnnneeeccc",
    "abcccccccaaaaaacccccccccccaaaaaaccccccccaaaaaaaaaaccccccaaaaccccccaaaaaaaccccccaaaaaaccccccccaaaaacccccccccccccccccaaccaaaciiiqqtttxxxxwwyyywwvvvvrrrnnnneeeccc",
    "abcccccccaaaaaaccccccccccccaaaaacccccccaaaaaaacaaaccccccaaaacccccaaaaaacccccccccaaaaccccccccccaaaaaaccccaaccccccccccccccaaciiqqqtttxxxwwwyywwwwvvrrrrnnneeecccc",
    "abccccccaaaaaaaaccccccccccaaaaaccccccccaaaaaaccccccccccccaaacccccaaaaaaacccccccaaaaaccccccccaaaaaaaaacccaaccccccccccccccccciiqqqtttttwwswwyywwrrrrrrnnnneeecccc",
    "abccccccccccccacccccccccccaccaaccccaaccaaaaaacccccccccccaccccccccaaacaaacccccccaacaaccccccccaaaaacaaaaaaaacccccccccaacccccciiqqqqttssssswwwwwrrrrnnnnnneeeecccc",
    "abcccccccccccccccccccccccccccccaaaaaaccccaacccccccaaacaaacccccccccccccaacaaacccccccccccccccccccaaaccaaaaaaaaccccaacaacccccciiiqqpppsssssswwwwrrrnnnnneeeeeccccc",
    "abcccccccccccccccccccccccccccccaaaaaaaccccccccccccaaaaaaaccccccccccccccccaaacccccccccccccccccccaaaccaaaaaaaaacccaaaaacccccchhhhppppppppssswwwrroonnfeeeeacccccc",
    "abccccccccccccccccccccaaaaaccccaaaaaaaaccccccccccccaaaaaaccccccccccccccaaaaaaaacccccccccccccccccccccaaaaaaaaaccccaaaaaaccccchhhhhpppppppsssssrroonfffeeaaaacccc",
    "abccccccccccccccccccccaaaaacccccaaaaaaaccccccccccccaaaaaaaaccccccccccccaaaaaaaacccccccccccccccccccccaaaaaacccccaaaaaaaacccccchhhhhhhppppsssssrooofffffaaaaacccc",
    "abcccccaacaaacccccccccaaaaaacccaaaaaacccccccccccccaaaaaaaaacccccccccccccaaaaacccccccccccccccccccccccaaaaaaaccccaaaaaccaccccccchhhhhhhhpppssssrooofffcaaaaaccccc",
    "abcccccaaaaaacccccccccaaaaaacccaaaaaaccccccccccccaaaaaaaaaacccccccccccccaaaaaaccccccccccccccccccccccaccaaaccccccacaaaccaacccccccchhhhhgppooooooofffcaaaaacccccc",
    "abcccccaaaaaacccccccccaaaaaaccccccaaacaacccccccccaaacaaaccccccccccaaacccaaaaaaccccccccccccccccccccccccccaaacccccccaaacaaaccccccccccchgggoooooooffffcaaaaaaccccc",
    "abaccccaaaaaaaccccccccccaaccccccccaaaaaacccccccccccccaaaccccccccccaaaaccaaaccacaacaacccccccccccccccccccccccccccccccaaaaaaaaccccccccccggggoooooffffccaccaaaccccc",
    "abacccaaaaaaaaccccccccccccccccccccaaaaaccccccccccccccaacccccccaaacaaaacccaaccccaaaaacccccccccccccccccccaacaacccccccaaaaaaaacccccccccccggggggggfffcccccccccccccc",
    "abacccaaaaaaaaccccccccaaacccccccccaaaaaaccccccccccccccccccccccaaacaaaacaaaaccccaaaaaaccccccccaaccccccccaaaaaccccccccaaaaaaacccccccccccaaggggggffcccccccccccccca",
    "abcccccccaaacccccccccaaaaaaccccccaaaaaaaacccccccccccccccccccaaaaaaaaaaaaaaaccccaaaaaaccccccacaaaacccccccaaaaacccccccaaaaaccccccccccccaaacgggggaccccccccccccccaa",
    "abcccccccaaccccccccccaaaaaaccccccaaaaaaaacccccccaaacccccccccaaaaaaaaaaaaaaaacccaaaaaaccccccaaaaaaccccccaaaaaaccccccaaaaaaacccccccccccaaaccccaaaccccccccccaaacaa",
    "abcccccccccccccccccccaaaaaccccccccccaaccccccccaaaaaccccccccccaaaaaaaaaaaaaaaaccccaaaccccccccaaaacccccccaaaaccccccccccccaaccccccccccccccccccccccccccccccccaaaaaa",
    "abccccccccccccccccccccaaaaacccccccccaaccccccccaaaaaacccccccccaaaaaaaaaaaaaaaacccccccccccccccaaaacccccccccaacccccccccccccccccccccccccccccccccccccccccccccccaaaaa",
]
DEBUG = False
BOARD = []
MAX_STEPS = 999999
MAX_HEIGHT = "a"
PITS = []

import copy
import sys
from functools import lru_cache

sys.setrecursionlimit(10000)


def hash_list(l: list) -> int:
    __hash = 0
    for i, e in enumerate(l):
        __hash = hash((__hash, i, hash_item(e)))
    return __hash


def hash_dict(d: dict) -> int:
    __hash = 0
    for k, v in d.items():
        __hash = hash((__hash, k, hash_item(v)))
    return __hash


def hash_item(e) -> int:
    if hasattr(e, "__hash__") and callable(e.__hash__):
        try:
            return hash(e)
        except TypeError:
            pass
    if isinstance(e, (list, set, tuple)):
        return hash_list(list(e))
    elif isinstance(e, (dict)):
        return hash_dict(e)
    else:
        raise TypeError(f"unhashable type: {e.__class__}")


def my_lru_cache(*opts, **kwopts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            __hash = hash_item([id(func)] + list(args) + list(kwargs.items()))

            @lru_cache(*opts, **kwopts)
            def cached_func(args_hash):
                return func(*args, **kwargs)

            return cached_func(__hash)

        return wrapper

    return decorator


def run(data, debug=False):
    global DEBUG, BOARD

    DEBUG = debug

    results = 0
    current = ()
    destination = ()

    for row in data:
        BOARD.append(list(row))

    for y in range(len(BOARD)):
        for x in range(len(BOARD[y])):
            if BOARD[y][x] == "S":
                BOARD[y][x] = "a"
                current = (x, y)
            elif BOARD[y][x] == "E":
                BOARD[y][x] = "z"
                destination = (x, y)
    print("S", current, "E", destination)

    if DEBUG:
        for row in BOARD:
            print(row)

    visited = []

    results = visit(current, visited, destination, "a")

    return results


@my_lru_cache(maxsize=None)
def visit(current, visited, destination, last_spot):
    global DEBUG, BOARD, MAX_STEPS, MAX_HEIGHT

    visited.append(current)

    current_x, current_y = current
    spot = BOARD[current_y][current_x]
    if spot > MAX_HEIGHT:
        print("----- ", spot, " -----")
        MAX_HEIGHT = spot

    if ord(last_spot) > ord(spot):
        if spot == "a":
            if current in PITS:
                return MAX_STEPS
            if in_a_pit(current):
                return MAX_STEPS

    MAX_HEIGHT = max(MAX_HEIGHT, spot)

    if current == destination:
        if DEBUG or True:
            print("AAAAAAAAAAAAAAAAAAAAAAAAAA", len(visited) - 1)
        if DEBUG:
            print(visited)
        return len(visited) - 1

    if len(visited) > MAX_STEPS:
        if DEBUG:
            print("TOO FAR")
        return MAX_STEPS

    queue = []

    if DEBUG:
        print("SPOT", spot, current)

    next = (current_x + 1, current_y)
    next_x, next_y = next
    if next_x < len(BOARD[0]) and next not in visited and next not in queue:
        #        if DEBUG: print("RIGHT CHECK", spot, ord(spot), BOARD[next_y][next_x], ord(BOARD[next_y][next_x]))
        if ord(spot) + 1 >= ord(BOARD[next_y][next_x]):
            #            if DEBUG: print("TRUE")
            queue.append(next)

    next = (current_x, current_y + 1)
    next_x, next_y = next
    if next_y < len(BOARD) and next not in visited and next not in queue:
        #        if DEBUG: print("DOWN CHECK", spot, ord(spot), BOARD[next_y][next_x], ord(BOARD[next_y][next_x]))
        if ord(spot) + 1 >= ord(BOARD[next_y][next_x]):
            #           if DEBUG: print("TRUE")
            queue.append(next)

    next = (current_x, current_y - 1)
    next_x, next_y = next
    if next_y >= 0 and next not in visited and next not in queue:
        #        if DEBUG: print("UP CHECK", spot, ord(spot), BOARD[next_y][next_x], ord(BOARD[next_y][next_x]))
        if ord(spot) + 1 >= ord(BOARD[next_y][next_x]):
            #           if DEBUG: print("TRUE")
            queue.append(next)

    next = (current_x - 1, current_y)
    next_x, next_y = next
    if next_x >= 0 and next not in visited and next not in queue:
        #        if DEBUG: print("LEFT CHECK", spot, ord(spot), BOARD[next_y][next_x], ord(BOARD[next_y][next_x]))
        if ord(spot) + 1 >= ord(BOARD[next_y][next_x]):
            #            if DEBUG: print("TRUE")
            queue.append(next)

    # if DEBUG: print("q", queue)
    steps = 999999
    for q in queue:
        steps = min(steps, visit(q, copy.copy(visited), destination, spot))
        MAX_STEPS = min(MAX_STEPS, steps)

    return steps


@my_lru_cache(maxsize=None)
def in_a_pit(current):
    global BOARD, DEBUG

    spots = []
    visited = []
    queue = [current]
    break_x, break_y = (99, 99)

    while len(queue) > 0:
        current = queue.pop(0)
        current_x, current_y = current
        spot = BOARD[current_y][current_x]

        visited.append(current)

        next = (current_x + 1, current_y)
        next_x, next_y = next
        if (
            next_x < len(BOARD[0])
            and next not in spots
            and next not in visited
            and next not in queue
        ):
            if "a" == BOARD[next_y][next_x]:
                spots.append(next)
                queue.append(next)
            elif BOARD[next_y][next_x] != "c":
                return False

        next = (current_x, current_y + 1)
        next_x, next_y = next
        if next_y < len(BOARD) and next not in spots and next not in visited and next not in queue:
            if "a" == BOARD[next_y][next_x]:
                spots.append(next)
                queue.append(next)
            elif BOARD[next_y][next_x] != "c":
                return False

        next = (current_x, current_y - 1)
        next_x, next_y = next
        if next_y >= 0 and next not in spots and next not in visited and next not in queue:
            if "a" == BOARD[next_y][next_x]:
                spots.append(next)
                queue.append(next)
            elif BOARD[next_y][next_x] != "c":
                return False

        next = (current_x - 1, current_y)
        next_x, next_y = next
        if next_x >= 0 and next not in spots and next not in visited and next not in queue:
            if "a" == BOARD[next_y][next_x]:
                spots.append(next)
                queue.append(next)
            elif BOARD[next_y][next_x] != "c":
                return False

    print("Found PITS", sorted(spots, key=lambda x: x[1]))
    PITS.extend(spots)
    return True


if __name__ == "__main__":
    #    results = run(DATA_TEST, debug=True)
    results = run(DATA, debug=False)
    # 775 is too high
    print("ANSWER:", results)
