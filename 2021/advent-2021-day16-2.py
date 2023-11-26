DATA_TEST1 = 'C200B40A82'
DATA_TEST2 = '04005AC33890'
DATA_TEST3 = '880086C3E88112'
DATA_TEST4 = 'CE00C43D881120'
DATA_TEST5 = 'F600BC2D8F'
DATA_TEST6 = 'D8005AC2A8F0'
DATA_TEST7 = '9C005AC2F8F0'
DATA_TEST8 = '9C0141080250320F1802104A08'
DATA = 'C20D59802D2B0B6713C6B4D1600ACE7E3C179BFE391E546CC017F004A4F513C9D973A1B2F32C3004E6F9546D005840188C51DA298803F1863C42160068E5E37759BC4908C0109E76B00425E2C530DE40233CA9DE8022200EC618B10DC001098EF0A63910010D3843350C6D9A252805D2D7D7BAE1257FD95A6E928214B66DBE691E0E9005F7C00BC4BD22D733B0399979DA7E34A6850802809A1F9C4A947B91579C063005B001CF95B77504896A884F73D7EBB900641400E7CDFD56573E941E67EABC600B4C014C829802D400BCC9FA3A339B1C9A671005E35477200A0A551E8015591F93C8FC9E4D188018692429B0F930630070401B8A90663100021313E1C47900042A2B46C840600A580213681368726DEA008CEDAD8DD5A6181801460070801CE0068014602005A011ECA0069801C200718010C0302300AA2C02538007E2C01A100052AC00F210026AC0041492F4ADEFEF7337AAF2003AB360B23B3398F009005113B25FD004E5A32369C068C72B0C8AA804F0AE7E36519F6296D76509DE70D8C2801134F84015560034931C8044C7201F02A2A180258010D4D4E347D92AF6B35B93E6B9D7D0013B4C01D8611960E9803F0FA2145320043608C4284C4016CE802F2988D8725311B0D443700AA7A9A399EFD33CD5082484272BC9E67C984CF639A4D600BDE79EA462B5372871166AB33E001682557E5B74A0C49E25AACE76D074E7C5A6FD5CE697DC195C01993DCFC1D2A032BAA5C84C012B004C001098FD1FE2D00021B0821A45397350007F66F021291E8E4B89C118FE40180F802935CC12CD730492D5E2B180250F7401791B18CCFBBCD818007CB08A664C7373CEEF9FD05A73B98D7892402405802E000854788B91BC0010A861092124C2198023C0198880371222FC3E100662B45B8DB236C0F080172DD1C300820BCD1F4C24C8AAB0015F33D280'

def run(parts):

    # print(f"parts: {parts}")

    v, t = int("".join(parts[0:3]), 2), int("".join(parts[3:6]), 2)
    parts[:] = parts[6:]

    # print(f"v: {v}, t: {t}")

    if t == 4:
        # literal
        block = []
        while True:
            start = parts[0]
            block += parts[1:5]
            parts[:] = parts[5:]
            if start == "0":
                break
        literal = int("".join(block), 2)
        # print(f"Literal {literal}")
        return (v, t, literal)

    else:
        # operator

        results = []

        i = parts[0]
        parts[:] = parts[1:]

        if i == "0":
            # 15-bits
            bits = 15
            length = int("".join(parts[:bits]), 2)
            parts[:] = parts[bits:]

            block = parts[:length]
            parts[:] = parts[length:]
            while len(block) > 0:
                results.append(run(block))
        else:
            # 11-bits
            bits = 11

            sub = int("".join(parts[:bits]), 2)
            parts[:] = parts[bits:]

            for _ in range(sub):
                results.append(run(parts))

        return (v, t, results)

def get_answer(results):
    op = results[1]
    values = results[2]

    if op == 0:
        # Add
        return sum(map(get_answer, values))
    elif op == 1:
        # Product
        product = 1
        for x in values:
            product *= get_answer(x)
        return product
    elif op == 2:
        # Min
        return min(map(get_answer, values))
    elif op == 3:
        # Max
        return max(map(get_answer, values))
    elif op == 4:
        return values
    elif op == 5:
        # >
        return get_answer(values[0]) > get_answer(values[1])
    elif op == 6:
        # <
        return get_answer(values[0]) < get_answer(values[1])
    elif op == 7:
        # ==
        return get_answer(values[0]) == get_answer(values[1])

def decode_data(data):
    results = ""
    decode = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }

    for letter in list(data):
        results += decode[letter]
    return results


if __name__ == "__main__":
    parts = decode_data(DATA)
    parts = [str(x) for x in parts]


    results = run(parts)
   # print (results)

    answer = get_answer(results)
    print(answer)

# 345367612078 is low
# 1549026292886 is correct
'''
100     v4
000     t0
0       choose 15-bit
000001011010110    726 length
00011
00111
00010
010000

'''