DATA_TEST = ['start-A','start-b','A-c','A-b','b-d','A-end','b-end']
DATA_TEST2 =['dc-end','HN-start','start-kj','dc-start','dc-HN','LN-dc','HN-end','kj-sa','kj-HN','kj-dc']
DATA_TEST3 = ['fs-end','he-DX','fs-he','start-DX','pj-DX','end-zg','zg-sl','zg-pj','pj-he','RW-he','fs-DX','pj-RW','zg-RW','start-pj','he-WI','zg-he','pj-fs','start-RW']
DATA = ['he-JK','wy-KY','pc-XC','vt-wy','LJ-vt','wy-end','wy-JK','end-LJ','start-he','JK-end','pc-wy','LJ-pc','at-pc','xf-XC','XC-he','pc-JK','vt-XC','at-he','pc-he','start-at','start-XC','at-LJ','vt-JK']
from collections import Counter

def run(data):
    results = 0
    caves = setup_caves(data)
    paths = []

    print (caves)

    for cave in caves['start']:
        path = visit_cave(cave, caves, ['start'])
        paths.extend(path)

    results = len(paths)
    return results

def visit_cave(this_cave, caves, path):
    paths = []
    if this_cave in path:
        if this_cave.islower():
            counts = Counter([x for x in path if x.islower() and x != 'start'])
            max_val_key = max(counts, key=counts.get)
            max_val = counts[max_val_key]
            if max_val == 2:
                # Don't care what cave it is, we have already visited a small cave twice
                return []
    path.append(this_cave)

    for cave in caves[this_cave]:
        if cave == 'end':
            paths.append(path + [cave])
            continue

        new_paths = visit_cave(cave, caves, path.copy())
        for new_path in new_paths:
            if len(new_path) > 0:
                paths.append(new_path)

#         if len(new_paths) > 0:
#             for new_path in new_paths:
#                 if new_path[-1] == 'end':
# #                    paths.extend(path + new_path)
#                     pass

    return paths


def setup_caves(data):
    caves = {}
    for path in data:
        a, b = path.split('-')
        if a != 'end' and b != 'start':
            paths = caves.get(a, [])
            paths.append(b)
            caves[a] = paths

        if a!= 'start' and b != 'end':
            paths = caves.get(b, [])
            paths.append(a)
            caves[b] = paths
    return caves


if __name__ == "__main__":
    results = run(DATA)
    print (results)
