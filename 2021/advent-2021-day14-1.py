DATA_TEST = ['NNCB','','CH -> B','HH -> N','CB -> H','NH -> C','HB -> C','HC -> B','HN -> C','NN -> C','BH -> H','NC -> B','NB -> B','BN -> B','BB -> N','BC -> B','CC -> N','CN -> C']
DATA = ['SVCHKVFKCSHVFNBKKPOC','','NC -> H','PK -> V','SO -> C','PH -> F','FP -> N','PN -> B','NP -> V','NK -> S','FV -> P','SB -> S','VN -> F','SC -> H','OB -> F','ON -> O','HN -> V','HC -> F','SN -> K','CB -> H','OP -> K','HP -> H','KS -> S','BC -> S','VB -> V','FC -> B','BH -> C','HH -> O','KH -> S','VF -> F','PF -> P','VV -> F','PP -> V','BO -> H','BF -> B','PS -> K','FO -> O','KF -> O','FN -> H','CK -> B','VP -> V','HK -> F','OV -> P','CS -> V','FF -> P','OH -> N','VS -> H','VO -> O','CP -> O','KC -> V','KV -> P','BK -> B','VK -> S','NF -> V','OO -> V','FH -> H','CN -> O','SP -> B','KN -> V','OF -> H','NV -> H','FK -> B','PV -> N','NB -> B','KK -> P','VH -> P','CC -> B','HV -> V','OC -> H','PO -> V','NO -> O','BP -> C','NH -> H','BN -> O','BV -> S','CV -> B','HS -> O','NN -> S','NS -> P','KB -> F','CO -> H','HO -> P','PB -> B','BS -> P','SH -> H','FS -> V','SF -> O','OK -> F','KP -> S','BB -> C','PC -> B','OS -> C','SV -> N','SK -> K','KO -> C','SS -> V','CF -> C','HB -> K','VC -> B','CH -> P','HF -> K','FB -> V']

def run(data, steps):
    results = 0
    rules = {}
    poly = data.pop(0)
    data.pop(0)
    for rule in data:
        a, b = rule.split(' -> ')
        rules[a] = b

    print (poly)
    print(rules)


    for step in range(1, steps + 1):
#        print (f"{step}: {poly}")
        new_poly = ""
        for index in range(len(poly) - 1):
            between = rules.get(poly[index:index+2], "")
            new_poly += poly[index] + between
        new_poly += poly[-1]

        poly = new_poly

        from collections import defaultdict
        count = defaultdict(int)
        for c in poly:
            count[c] += 1
        count = dict(count)
        low = count[min(count, key=count.get)]
        high = count[max(count, key=count.get)]

        results = high - low


    return results

if __name__ == "__main__":
    results = run(DATA, 10)
    print (results)

#1588