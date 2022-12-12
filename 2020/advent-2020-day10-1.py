DATA_TEST = [16,10,15,5,1,11,7,19,6,12,4]
DATA_TEST2 = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]
DATA = [145,3,157,75,84,141,40,20,60,48,15,4,2,21,129,113,54,28,69,42,34,1,155,63,151,8,139,135,33,81,70,132,150,112,102,59,154,53,144,149,116,13,41,156,85,22,165,51,14,125,52,64,16,134,110,71,107,124,164,160,10,25,66,74,161,111,122,166,140,87,126,123,146,35,91,106,133,26,77,19,86,105,39,99,76,58,31,96,78,88,168,119,27,45,9,92,138,38,97,32,7,98,167,95,55,65]

def run(data): 
    counters = {"1":0, "2": 0, "3": 0}
    data.append(0)  # charging outlet
    data.append(max(data) + 3) # device built in
    data.sort()
    print(data)


    for index in range(len(data) - 1):
        print(f"{data[index]} - {data[index+1]} = {data[index+1] - data[index]}")
        diff = data[index+1] - data[index]
        counters[str(diff)] += 1
            
    return counters

if __name__ == "__main__":
    results = run(DATA_TEST)
    print(f"Results {results}")
    print(results["1"] * results["3"])