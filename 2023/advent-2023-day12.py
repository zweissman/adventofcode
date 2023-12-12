# pylint: disable=too-many-return-statements,too-many-statements,too-many-branches,duplicate-code,unused-argument
# pylint: disable=unnecessary-list-index-lookup

FILE_NAME = "2023/input/12.txt"

from math import comb
from functools  import reduce

def run(part: int, test_run: bool = False, debug: bool = False):
    if test_run:
        file = FILE_NAME.replace(".txt", "-test.txt")
    else:
        file = FILE_NAME

    with open(file, encoding="utf-8") as f:
        data = f.readlines()

    data = [x.strip() for x in data]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def show(grid: list[str], debug: bool = False):
    if debug:
        print()
        for y in range(len(grid)):
            print("".join([str(x) for x in grid[y]]))

def is_invalid(elements, values)->bool:
    if len(elements) > len(values):
        return True

    for i in range(len(elements)):
        element = elements[i]
        value = values[i]
        if len(element) < value:
            return True
    
    print(elements, values)
    return False

def part1(data: list[str], debug: bool = False) -> int:
    results = 0

    max_grid = 0
    grid=[]
    for d in data:
        if not d.startswith("//"):
            grid.append(d.strip())

    #show(grid,debug)

    while len(grid) > 0:
        # max_grid = max(max_grid, len(grid))
        if len(grid) % 10000 == 0:
            print(len(grid))
        row = grid.pop(0)
        spring_str, value_str = row.split(" ")
        if debug: print (spring_str)

        spring_str,value_str= reduce_elements(spring_str, value_str, debug)

        if spring_str == "":
            continue

        first_unknown = spring_str.find("?")
        if first_unknown > -1:
            grid.append(spring_str.replace("?", "#", 1) + " " + value_str)
            grid.append(spring_str.replace("?", ".", 1) + " " + value_str)


        else:
            elements = spring_str.split(".")
            elements = [x for x in elements if x != ""]

            values = value_str.split(",")
            values = [int(x) for x in values]
            

            if len(elements) != len(values):
                continue

            for i in range(len(elements)):
                element = elements[i]
                value = values[i]

                if len(element) != value:
                    break

            else:
                results += 1
                if debug: print (elements, values)
                if debug: print("Found one")

    print(f"{max_grid=}")
    return results


def reduce_elements(element_str:str, value_str:str, debug:bool) -> tuple[list[str], list[int]]:

    while element_str.find('..') > -1:
        element_str = element_str.replace('..', '.').strip('.')

    # elements = element_str.split(".")
    # elements = [x for x in elements if x != ""]
    # values = value_str.split(",")
    # values = [int(x) for x in values]

    words = element_str.strip('.').split(".")
    values = value_str.split(",")

    i = 0
    word = words[i]
    value = int(values[i])

    if len(word) < value:
        # Word is too short
        return "", value_str

    first_not_spring = word.find("?")
    if first_not_spring == -1 and len(word) != value:
        # Word is too long
        return "", value_str

    if len(word) == value:
        words[i] = "#" * value

    elif word.startswith('?') and word.endswith('?'):
        if len(word) - 1 == value:
            updated_word = "?" + "#" * (value - 1) + "?"
            words[i] = updated_word


    i = -1
    word = words[i]
    value = int(values[i])

    if len(word) < value:
        # Word is too short
        return "", value_str

    first_not_spring = word.find("?")
    if first_not_spring == -1 and len(word) != value:
        # Word is too long
        return "", value_str

    if len(word) == value:
        words[i] = "#" * value

    elif word.startswith('?') and word.endswith('?'):
        if len(word) - 1 == value:
            updated_word = "?" + "#" * (value - 1) + "?"
            words[i] = updated_word

    return ".".join(words), value_str

    # # Find the first element with a ? in it
    # for i in range(len(elements)):
    #     element = elements[i]
    #     value = values[i]

    #     for x in range(value, 0 , -1):
    #         first_index = element.find("#" * x)
    #         if -1 < first_index <= value:
    #             test_string = element[max(0, first_index-value):first_index+value]
    #             if test_string.count("#") == value:
    #                 # We found what what we are looking for.
    #                 element = element[first_index+value+1:] # Take an extra off for the spacer
    #                 elements[i] = element
    #                 values.pop(i)

    #                 return reduce_elements(elements, values, debug)
    #             else:
    #                 print("do work")
    #                 pass
    #     else:
    #         # All we have a ? in this element
    #         return elements, values

    #     if debug: print (elements, values)

    # return elements, values

def get_element_count(element: str) -> int:
    while element.find('..') > -1:
        element = element.replace('..', '.').strip('.')

    return element.count(".") + 1


def part2(data: list[str], empty_row_count: int = 999999, debug: bool = False) -> int:
    results = 0

    grid = []

    for i, d in enumerate(data):
        d = d.strip()
        grid.append(list(d))

    show(grid, debug)


    return results


if __name__ == "__main__":
    print("Test1: ", run(part=1, test_run=True, debug=True))  # 21
    #print("Real1: ", run(part=1, test_run=False, debug=False))  # 5686 too low
    # print("Test2: ", run(part=2, test_run=True, debug=True)) # 
    #print("Real2: ", run(part=2, test_run=False, debug=False))  # 
