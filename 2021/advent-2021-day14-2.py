DATA_TEST = [
    "NNCB",
    "",
    "CH -> B",
    "HH -> N",
    "CB -> H",
    "NH -> C",
    "HB -> C",
    "HC -> B",
    "HN -> C",
    "NN -> C",
    "BH -> H",
    "NC -> B",
    "NB -> B",
    "BN -> B",
    "BB -> N",
    "BC -> B",
    "CC -> N",
    "CN -> C",
]
DATA = [
    "SVCHKVFKCSHVFNBKKPOC",
    "",
    "NC -> H",
    "PK -> V",
    "SO -> C",
    "PH -> F",
    "FP -> N",
    "PN -> B",
    "NP -> V",
    "NK -> S",
    "FV -> P",
    "SB -> S",
    "VN -> F",
    "SC -> H",
    "OB -> F",
    "ON -> O",
    "HN -> V",
    "HC -> F",
    "SN -> K",
    "CB -> H",
    "OP -> K",
    "HP -> H",
    "KS -> S",
    "BC -> S",
    "VB -> V",
    "FC -> B",
    "BH -> C",
    "HH -> O",
    "KH -> S",
    "VF -> F",
    "PF -> P",
    "VV -> F",
    "PP -> V",
    "BO -> H",
    "BF -> B",
    "PS -> K",
    "FO -> O",
    "KF -> O",
    "FN -> H",
    "CK -> B",
    "VP -> V",
    "HK -> F",
    "OV -> P",
    "CS -> V",
    "FF -> P",
    "OH -> N",
    "VS -> H",
    "VO -> O",
    "CP -> O",
    "KC -> V",
    "KV -> P",
    "BK -> B",
    "VK -> S",
    "NF -> V",
    "OO -> V",
    "FH -> H",
    "CN -> O",
    "SP -> B",
    "KN -> V",
    "OF -> H",
    "NV -> H",
    "FK -> B",
    "PV -> N",
    "NB -> B",
    "KK -> P",
    "VH -> P",
    "CC -> B",
    "HV -> V",
    "OC -> H",
    "PO -> V",
    "NO -> O",
    "BP -> C",
    "NH -> H",
    "BN -> O",
    "BV -> S",
    "CV -> B",
    "HS -> O",
    "NN -> S",
    "NS -> P",
    "KB -> F",
    "CO -> H",
    "HO -> P",
    "PB -> B",
    "BS -> P",
    "SH -> H",
    "FS -> V",
    "SF -> O",
    "OK -> F",
    "KP -> S",
    "BB -> C",
    "PC -> B",
    "OS -> C",
    "SV -> N",
    "SK -> K",
    "KO -> C",
    "SS -> V",
    "CF -> C",
    "HB -> K",
    "VC -> B",
    "CH -> P",
    "HF -> K",
    "FB -> V",
]


def run(data, steps):
    results = 0

    poly = data.pop(0)
    data.pop(0)

    rules = {}
    for q in data:
        pair, letter = q.split(" -> ")
        rules[pair] = letter

    pairs = {}
    for index in range(len(poly) - 1):
        pairs[poly[index] + poly[index + 1]] = pairs.get(poly[index] + poly[index + 1], 0) + 1

    # print(pairs)
    for step in range(1, steps + 1):
        # print(f"step: {step}")
        new_pairs = {}
        for pair in pairs:
            assert len(pair) == 2
            a, b = pair

            letter = rules[pair]
            new_pairs[a + letter] = new_pairs.get(a + letter, 0) + pairs[pair]
            new_pairs[letter + b] = new_pairs.get(letter + b, 0) + pairs[pair]

        pairs = new_pairs
        # print(f"-" * 50)
        # print(pairs)

    left_count, right_count = {}, {}

    # Don't count the letter on both sides of the pair, just one or the other, whichever is greater
    for pair in pairs:
        assert len(pair) == 2
        a, b = pair

        left_count[a] = left_count.get(a, 0) + pairs[pair]
        right_count[b] = right_count.get(b, 0) + pairs[pair]

    max_count = {}
    for letter in set(list(left_count) + list(right_count)):
        max_count[letter] = max(left_count.get(letter, 0), right_count.get(letter, 0))

    # print(max_count)

    low = max_count[min(max_count, key=max_count.get)]
    high = max_count[max(max_count, key=max_count.get)]

    results = high - low

    return results


if __name__ == "__main__":
    results = run(DATA, 40)
    print(results)
