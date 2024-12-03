# from treelib import Tree

# FILE_NAME = "2022/input/07.txt"

# def run(part: int, test_run: bool = False, debug: bool = False):
#     if test_run:
#         file = FILE_NAME.replace(".txt", "-test.txt")
#         folder_name = ""
#     else:
#         file = FILE_NAME
#         folder_name = ""

#     with open(file, encoding="utf-8") as f:
#         data = f.readlines()

#     data = [x.strip() for x in data]
#     part_function = part1 if part == 1 else part2

#     return part_function(data=data, folder_name=folder_name, debug=debug)

# def part1(data: list[str], folder_name: str, debug: bool = False) -> int:
#     tree = Tree()
#     tree.create_node(folder_name, folder_name)
#     if debug:
#         tree.show()

#     while len(data) > 0:
#         row = data.pop(0)
#         #        if debug: print("-->", row)
#         if row == "$ cd /":
#             # ignore
#             continue
#         if row.startswith("$"):
#             # Command
#             command = row[2:]
#             if debug:
#                 print("COMMAND:", command)
#             if command.startswith("cd"):
#                 # Change dir
#                 _, right = command.split(" ")
#                 if right == "..":
#                     return tree

#                 sub_folder_name = right
#                 if folder_name != "/":
#                     sub_folder_name = f"{folder_name}/{sub_folder_name}"
#                 else:
#                     sub_folder_name = f"/{sub_folder_name}"

#                 sub_tree = run(data, sub_folder_name, debug=debug)
#                 print("****SUB*****")
#                 sub_tree.show()
#                 print("****TREE*****")
#                 tree.show()
#                 tree.paste(folder_name, sub_tree)
#                 print("****TREE AFTER*****")
#                 tree.show()

#             elif command == "ls":
#                 while len(data) > 0:
#                     row = data.pop(0)
#                     if row.startswith("$"):
#                         break
#                     if row.startswith("dir"):
#                         sub_folder = row.replace("dir ", "")
#                         # tree.create_node(sub_folder, sub_folder, parent=folder_name)
#                     else:
#                         size, name = row.split(" ")
#                         item_name = f"{size}|{name}"
#                         tree.create_node(item_name, item_name, parent=folder_name)

#                     if debug:
#                         tree.show()

#                 data.insert(0, row)
#             else:
#                 raise Exception(f"Unknown command {command}")

#     return tree


# def get_folder_sizes(tree):
#     total_size = 0

#     for node in tree.all_nodes_itr():
#         if node.is_leaf():
#             size, _ = node.tag.split("|")
#             total_size += int(size)

#     return total_size

# def part2(data: list[str], folder_name:str, debug: bool = False) -> int:
#     tree = Tree()
#     tree.create_node(folder_name, folder_name)
#     if debug:
#         tree.show()

#     while len(data) > 0:
#         row = data.pop(0)
#         #        if debug: print("-->", row)
#         if row == "$ cd /":
#             # ignore
#             continue
#         if row.startswith("$"):
#             # Command
#             command = row[2:]
#             if debug:
#                 print("COMMAND:", command)
#             if command.startswith("cd"):
#                 # Change dir
#                 _, right = command.split(" ")
#                 if right == "..":
#                     return tree

#                 sub_folder_name = right
#                 if folder_name != "/":
#                     sub_folder_name = f"{folder_name}/{sub_folder_name}"
#                 else:
#                     sub_folder_name = f"/{sub_folder_name}"

#                 sub_tree = run(data, sub_folder_name, debug=debug)
#                 print("****SUB*****")
#                 sub_tree.show()
#                 print("****TREE*****")
#                 tree.show()
#                 tree.paste(folder_name, sub_tree)
#                 print("****TREE AFTER*****")
#                 tree.show()

#             elif command == "ls":
#                 while len(data) > 0:
#                     row = data.pop(0)
#                     if row.startswith("$"):
#                         break
#                     if row.startswith("dir"):
#                         sub_folder = row.replace("dir ", "")
#                         # tree.create_node(sub_folder, sub_folder, parent=folder_name)
#                     else:
#                         size, name = row.split(" ")
#                         item_name = f"{size}|{name}"
#                         tree.create_node(item_name, item_name, parent=folder_name)

#                     if debug:
#                         tree.show()

#                 data.insert(0, row)
#             else:
#                 raise Exception(f"Unknown command {command}")

#     return tree


# def get_folder_sizes(tree):
#     total_size = 0

#     for node in tree.all_nodes_itr():
#         if node.is_leaf():
#             size, _ = node.tag.split("|")
#             total_size += int(size)

#     return total_size

# if __name__ == "__main__":
#     print("Test1: ", run(part=1, test_run=True, debug=True))  #
#     print("Real1: ", run(part=1, test_run=False, debug=False))  #
#     print("Test2: ", run(part=2, test_run=True, debug=True))  #
#     print("Real2: ", run(part=2, test_run=False, debug=False))  #

# # if __name__ == "__main__":
# #     # tree = run(DATA_TEST, "/", debug=True)
# #     # tree = run(DATA_TEST_NEW, "/", debug=True)
# #     tree = run(DATA, "/", debug=False)

# #     tree.show()

# #     results = 0
# #     for node in tree.all_nodes_itr():
# #         if node.is_root():
# #             folder_size = get_folder_sizes(tree.subtree(node.tag))
# #             print("FOLDER", node.tag, folder_size)

# #             if folder_size <= 100000:
# #                 results += folder_size

# #     print("ANSWER:", results)
