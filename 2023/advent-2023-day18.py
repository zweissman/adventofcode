# def run(part: int, test_run: bool = False, debug: bool = False):
#     file_name = "2023/input/18.txt"
#     if test_run:
#         file_name = file_name.replace(".txt", "-test2.txt")

#     with open(file_name, encoding="utf-8") as file:
#         file_data = file.readlines()

#     data = [x.strip() for x in file_data]
#     part_function = part1 if part == 1 else part2

#     return part_function(data=data, debug=debug)


# dir_map = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}


# def show(grid: list[list[str]], debug: bool = False):
#     if debug:
#         for y in range(len(grid)):
#             print("".join([str(x) for x in grid[y]]))
#         print()


# def part1(data: list[str], debug: bool = False) -> int:
#     pass


# def shoelace(grid: list, debug: bool) -> int:
#     pass


# def part1_old(data: list[str], debug: bool = False) -> int:
#     results = 0
#     commands = []

#     # max_x, max_y = 316, 226
#     max_x, max_y = 10, 10
#     grid = [["."] * max_x for _ in range(max_y)]  # col x # row
#     for command in commands:
#         command = command.strip()
#         if not command.startswith("#"):
#             grid.append(list(command))

#     show(grid, debug)

#     # x, y = 66, 209
#     x, y = 0, 0
#     grid[y][x] = "#"

#     for line in data:
#         assert x >= 0 and y >= 0

#         direction, distance, color = line.split(" ")
#         distance = int(distance)
#         color = color.strip("(").strip(")")

#         if direction == "R":
#             for _ in range(0, distance):
#                 x += 1
#                 grid[y][x] = "#"
#         elif direction == "L":
#             for _ in range(0, distance):
#                 x -= 1
#                 grid[y][x] = "#"
#         elif direction == "U":
#             for _ in range(0, distance):
#                 y -= 1
#                 grid[y][x] = "#"
#         elif direction == "D":
#             for _ in range(0, distance):
#                 y += 1
#                 grid[y][x] = "#"

#         if debug:
#             print(f"{direction}: {distance}")
#         show(grid, debug)

#     print("\n\n")

#     for row in grid:
#         result = row_count(row, True)
#         results += result

#         if debug and result > 0:
#             print(f"row: {result} total {results}\n")

#     return results


# def row_count_old(original_row, debug=False):
#     results = 0

#     row = "".join(original_row).strip(".")
#     if row == "":
#         return 0

#     if debug:
#         print(row)

#     if row.count(".") == 0:
#         return len(row)

#     for i in range(len(row)):
#         if row[i] == "#":
#             results += 1
#         else:
#             break
#     else:
#         return results

#     row = row[i:]

#     # Look to see if we have an edge
#     next_wall = row.find("##")
#     if next_wall != -1:
#         results += next_wall + 1
#         row = row[next_wall + 1 :]

#     next_wall = row.find("#")
#     assert next_wall != -1
#     results += next_wall
#     row = row.strip(".")

#     for i in range(len(row)):
#         if row[i] == "#":
#             results += 1
#         else:
#             break
#     else:
#         return results

#     return results + row_count(row[i:], debug)


# def part2(data: list[str], debug: bool = False) -> int:
#     grid = []

#     for d in data:
#         d = d.strip()
#         if not d.startswith("#"):
#             grid.append(list(d))

#     show(grid, debug)


# if __name__ == "__main__":
#     print("Test1: ", run(part=1, test_run=True, debug=True))  # 62
#     # print("Real1: ", run(part=1, test_run=False, debug=False))  # not 87244, not 45313, 26529 is low
#     # print("Real2: ", run(part=2, test_run=False, debug=False))  #
