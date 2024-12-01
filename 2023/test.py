def solution(tree):
    # Type your solution here
    if len(tree) == 0:
        # empty tree
        return 0

    depth = get_depth(tree, 0)
    return depth


def get_depth(tree: list[int], level: int) -> int:
    level_size = 2**level

    if max(tree[:level_size]) == -1:
        # root without children
        return level

    print(f"{level=} {level_size=}, {tree[:level_size]}")

    print(f"{level=} remove {(level + 1) ** 2}")

    next_level = tree[level_size:]

    if len(tree) <= level_size:
        return level + 1

    return get_depth(next_level, level + 1)


if __name__ == "__main__":
    tree = [1, -1, -1]
    final = solution(tree)
    print("ANSWER:", final)
