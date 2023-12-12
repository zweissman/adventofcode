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


def part1(data: list[str], debug: bool = False) -> int:
    results = 0

    grid=[]
    for d in data:
        if not d.startswith("//"):
            grid.append(d.strip())

    #show(grid,debug)

    for row in grid:
        spring_str, value_str = row.split(" ")

        elements = spring_str.split(".")
        elements = [x for x in elements if x != ""]

        values = value_str.split(",")
        values = [int(x) for x in values]
        
        if debug: print (elements, values)
        value_total = sum(values) + len(values) - 1
        element_total = sum([len(x) for x in elements]) + len(elements) - 1

        assert value_total <= element_total

        if value_total == element_total:
            # There is only one solution
            results += 1
            continue

        while True:
            element = elements[0]
            value = values[0]

            # The first element matches the size that we are expecting. Remove it
            if len(element) == value:
                elements.pop(0)
                values.pop(0)
            else:
                break

        if debug: print (elements, values)

        while True:
            element = elements[-1]
            value = values[-1]

            # The last element matches the size that we are expecting. Remove it
            if len(element) == value:
                elements.pop()
                values.pop()
            else:
                break

        if debug: print (elements, values)

        elements, values = reduce_elements(elements, values, debug)

        if debug: print (elements, values)

        if len(elements) == 1:
            value_total = sum(values) + len(values) - 1
        else:
            print("do work")

        # combos = []
        # # See if the elements and values match up with sizes
        # for i in range(len(elements)):
        #     element = elements[i]
        #     value = values[i]

        #     # Make sure that all we have are ? or #
        #     assert element.count("?") + element.count("#") == len(element)

        #     if len(element) != value:
        #         # Need to split this element up more
        #         combos.append(comb(len(element), value))

        # if len(combos) == 0:
        #     results += 1
        # else:
        #     results += reduce((lambda x, y: x * y), combos)
    
        if debug: print (results)
        if debug: print (elements, values)

    return results


def reduce_elements(elements, values, debug) -> tuple[list[str], list[int]]:
    # Find the first element with a ? in it
    for i in range(len(elements)):
        element = elements[i]
        value = values[i]

        for x in range(value, 0 , -1):
            first_index = element.find("#" * x)
            if -1 < first_index <= value:
                test_string = element[max(0, first_index-value):first_index+value]
                if test_string.count("#") == value:
                    # We found what what we are looking for.
                    element = element[first_index+value+1:] # Take an extra off for the spacer
                    elements[i] = element
                    values.pop(i)

                    return reduce_elements(elements, values, debug)
                else:
                    print("do work")
                    pass
        else:
            # All we have a ? in this element
            return elements, values

        if debug: print (elements, values)

    return elements, values


def part2(data: list[str], empty_row_count: int = 999999, debug: bool = False) -> int:
    results = 0

    grid = []

    for i, d in enumerate(data):
        d = d.strip()
        grid.append(list(d))

    show(grid, debug)


    return results


if __name__ == "__main__":
     print("Test1: ", run(part=1, test_run=True, debug=True))  # 
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 
    # print("Test2: ", run(part=2, test_run=True, debug=True)) # 
    #print("Real2: ", run(part=2, test_run=False, debug=False))  # 
