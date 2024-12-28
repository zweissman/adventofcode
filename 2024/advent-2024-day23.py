from collections import defaultdict

import networkx as nx


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
    network = defaultdict(list)

    for line in data:
        a, b = line.split("-")
        network[a].append(b)
        network[b].append(a)

    good = set()

    for k, v in network.items():
        # print(k, v)
        for i, comp in enumerate(v):
            for j in range(i + 1, len(v)):
                comp2 = v[j]
                if comp2 in network[comp]:
                    if k.startswith("t") or comp.startswith("t") or comp2.startswith("t"):
                        results += 1
                        good.add(str(sorted([k, comp, comp2])))

    if debug:
        print(good)

    return len(good)


def part2(data: list[str], debug: bool = False) -> str:
    G = nx.Graph()

    for line in data:
        a, b = line.split("-")
        G.add_edge(a, b)

    cliques = list(nx.find_cliques_recursive(G))
    cliques.sort(key=len)
    if debug:
        print(cliques)
    biggest_clique = cliques[-1]

    return ",".join(sorted(biggest_clique))


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 12
    # print("Real1: ", run(part=1, debug=False))  # 1062
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # co,de,ka,ta
    print("Real2: ", run(part=2, debug=False))  # bz,cs,fx,ms,oz,po,sy,uh,uv,vw,xu,zj,zm
