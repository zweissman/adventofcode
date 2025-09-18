"""
--- Day 9: All in a Single Night ---
Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?

Your puzzle answer was 141.

--- Part Two ---
The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?

Your puzzle answer was 736.
"""

import itertools


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
    show(data, debug=debug)
    lookup: dict[tuple[str, str], int] = {}
    cities: set[str] = set()

    for row in data:
        cities_string, distance = row.split(" = ")
        city1, city2 = cities_string.split(" to ")
        lookup[(city1, city2)] = int(distance)
        lookup[(city2, city1)] = int(distance)

        cities.update([city1, city2])

    results = find_shortest_route(lookup, cities, debug)

    return results


def find_shortest_route(
    lookup: dict[tuple[str, str], int], cities: set[str], debug: bool = False
) -> int:
    shortest_distance = 99999999

    for route in itertools.permutations(cities):
        distance = 0
        start = route[0]
        path = start
        for city in route[1:]:
            distance += lookup.get((start, city), 0)
            start = city
            path += ", " + city

        if distance < shortest_distance:
            shortest_distance = distance
            if debug:
                print("New shortest route:" + path)

    return shortest_distance


def part2(data: list[str], debug: bool = False) -> int:
    results = 0
    show(data, debug=debug)
    lookup: dict[tuple[str, str], int] = {}
    cities: set[str] = set()

    for row in data:
        cities_string, distance = row.split(" = ")
        city1, city2 = cities_string.split(" to ")
        lookup[(city1, city2)] = int(distance)
        lookup[(city2, city1)] = int(distance)

        cities.update([city1, city2])

    results = find_longest_route(lookup, cities, debug)

    return results


def find_longest_route(
    lookup: dict[tuple[str, str], int], cities: set[str], debug: bool = False
) -> int:
    longest_distance = 0

    for route in itertools.permutations(cities):
        distance = 0
        start = route[0]
        path = start
        for city in route[1:]:
            distance += lookup.get((start, city), 0)
            start = city
            path += ", " + city

        if distance > longest_distance:
            longest_distance = distance
            if debug:
                print("New longest route:" + path)

    return longest_distance


def show(grid: list[str], debug: bool = False) -> None:
    if debug:
        print()
        for y, row in enumerate(grid):
            print(f"{y:02}", "".join([str(x) for x in row]))


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_suffix="-test", debug=True))  # 605
    # print("Real1: ", run(part=1, debug=False))  # 141
    # print("Test2: ", run(part=2, test_suffix="-test", debug=True))  # 982
    print("Real2: ", run(part=2, debug=False))  # 736
