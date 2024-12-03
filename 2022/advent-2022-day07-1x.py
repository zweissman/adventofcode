# import collections


# def run(data, folder_name, debug=False):
#     results = 0
#     tree = {}
#     hier = collections.OrderedDict()

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
#                     return tree, hier

#                 folder_name = right
#                 folder, sub_hier = run(data, folder_name, debug=debug)
#                 tree.update(folder)
#                 hier.update(sub_hier)
#                 if debug:
#                     print("FOLDER:", folder)

#             elif command == "ls":
#                 files = []
#                 while len(data) > 0:
#                     row = data.pop(0)
#                     if row.startswith("$"):
#                         break
#                     if row.startswith("dir"):
#                         sub_folder = row.replace("dir ", "")
#                         hier[folder_name] = hier.get(folder_name, [])
#                         hier[folder_name].append(sub_folder)
#                         continue
#                     else:
#                         size, name = row.split(" ")
#                         files.append(size)

#                 tree[folder_name] = files
#                 if len(data) > 0:
#                     data.insert(0, row)
#                 else:
#                     return tree, hier

#             else:
#                 raise Exception(f"Unknown command {command}")

#     if debug:
#         print("\n\nTREE", tree)
#     if debug:
#         print("\n\nHIER", hier)
#     hier = collections.OrderedDict(reversed(list(hier.items())))

#     # resolve hierarchy
#     for folder, items in hier.items():
#         for item in items:
#             tree[folder].extend(tree[item])

#     if debug:
#         print("\n\nTREE", tree)

#     for folder, contents in tree.items():
#         folder_size = sum([int(file) for file in contents])
#         if folder_size <= 100000:
#             results += folder_size

#     return results


# if __name__ == "__main__":
#     #    results = run(DATA_TEST, "/", debug=True)
#     results = run(DATA, "/", debug=True)
#     print("ANSWER:", results)
