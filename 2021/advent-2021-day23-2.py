DATA_TEST = ['BA', 'CD', 'BC', 'DA']
DATA_TEST = ['BDDA', 'CCBD', 'BBAC', 'DACA']
DATA = ['AB', 'DC', 'BD', 'CA']
DATA = ['ADDB', 'DCBC', 'BBAD', 'CACA']

from collections import Counter
from copy import deepcopy

COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

def run(data):
    hall = list('.' * 11)
    rooms = {'A': list(data[0]), 'B': list(data[1]), 'C': list(data[2]), 'D': list(data[3])}
    results = move(hall, rooms)
    
    return results

def move(hall, rooms):

    DP = {}

    # given a state, what is the cost to get to "done"?
    show(hall, rooms)
    # move top -> L or R
    # move L or R -> 
    # always move to destination ASAP
    key = (tuple((k, tuple(v)) for k,v in rooms.items()), tuple(hall))
    if done(rooms):
        return 0
    if key in DP:
        return DP[key]
    
    # move to dest if possible
    for i, c in enumerate(hall):
        if c in rooms and can_move_to(c, rooms[c]):
            if clear_path(c, i, hall):
                di = dest_idx(rooms[c])
                assert di is not None
                dist = di + 1 + abs(bot_idx(c)-i)
                cost = COST[c] * dist
                new_hall = list(hall)
                new_hall[i] = '.'
                hall[i] = '.'
                new_rooms = deepcopy(rooms)
                new_rooms[c][di] = c
                #print(f'Moved top={i} c={c} dest={di}')
                return cost + move(new_hall, new_rooms)

    ans = int(1e9)
    for k, col in rooms.items():
        if not can_move_from(k, col):
            continue
        ki = top_idx(col)
        if ki is None:
            continue
        c = col[ki]
        for to_ in range(len(hall)):
            if to_ in [2, 4, 6, 8]:
                continue
            if hall[to_] != '.':
                continue
            if clear_path(k, to_, hall):
                dist = ki + 1 + abs(to_ - bot_idx(k))
                new_hall = list(hall)
                assert new_hall[to_] == '.'
                new_hall[to_] = c
                new_rooms = deepcopy(rooms)
                assert new_rooms[k][ki] == c
                new_rooms[k][ki] = '.'
                #print(f'Moved col={k} idx={ki} c={c} to {to_}')
                ans = min(ans, COST[c]*dist + move(new_hall, new_rooms))
    DP[key] = ans
    #print(len(DP), ans)
    return ans
 
def done(rooms):
    for k, v in rooms.items():
        for vv in v:
            if vv != k:
                return False
    return True

def can_move_from(k, col):
  for c in col:
    if c!=k and c!='.':
      return True
  return False

def can_move_to(k,col):
  for c in col:
    if c!=k and c!='.':
      return False
  return True

def bot_idx(bot):
  return {'A': 2, 'B': 4, 'C': 6, 'D': 8}[bot]

def top_idx(col):
  for i,c in enumerate(col):
    if c!='.':
      return i
  return None

def dest_idx(col):
  for i,c in reversed(list(enumerate(col))):
    if c=='.':
      return i
  return None

def between(a, bot, top):
  # 0 1 A 3 B 5 C 7 D 9 10
  return (bot_idx(bot)<a<top) or (top<a<bot_idx(bot))
assert between(1, 'A', 0)

def clear_path(bot, top_idx, top):
  for ti in range(len(top)):
    if between(ti, bot, top_idx) and top[ti]!='.':
      return False
  return True

def show(hall, rooms):
  C = Counter()
  for c in hall:
    C[c] += 1
  for k,v in rooms.items():
    for c in v:
      C[c] += 1
  assert C['A'] == 4
  assert C['B'] == 4
  assert C['C'] == 4
  assert C['D'] == 4
  assert C['.'] == 11
  assert hall[2] == '.'
  assert hall[4] == '.'
  assert hall[6] == '.'
  assert hall[8] == '.'


if __name__ == "__main__":
    results = run(DATA_TEST)
    print (results)