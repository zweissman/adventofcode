# from treelib import Tree


# def run(data, folder_name, debug=False):
#     results = 0
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
#     # tree = run(DATA_TEST, "/", debug=True)
#     # tree = run(DATA_TEST_NEW, "/", debug=True)
#     tree = run(DATA, "/", debug=False)

#     tree.show()

#     drive_size = 70000000
#     update_size = 30000000
#     used_size = get_folder_sizes(tree.subtree("/"))
#     to_free_up = update_size - (drive_size - used_size)

#     options = []
#     results = 0
#     for node in tree.all_nodes_itr():
#         if node.is_root():
#             folder_size = get_folder_sizes(tree.subtree(node.tag))
#             print("FOLDER", node.tag, folder_size)

#             if folder_size >= to_free_up:
#                 options.append(folder_size)

#     results = min(options)

#     print("ANSWER:", results)
