DATA_TEST = [3,4,3,1,2]
DATA = [1,1,3,5,1,1,1,4,1,5,1,1,1,1,1,1,1,3,1,1,1,1,2,5,1,1,1,1,1,2,1,4,1,4,1,1,1,1,1,3,1,1,5,1,1,1,4,1,1,1,4,1,1,3,5,1,1,1,1,4,1,5,4,1,1,2,3,2,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,5,1,1,1,3,4,1,1,1,1,3,1,1,1,1,1,4,1,1,3,1,1,3,1,1,1,1,1,3,1,5,2,3,1,2,3,1,1,2,1,2,4,5,1,5,1,4,1,1,1,1,2,1,5,1,1,1,1,1,5,1,1,3,1,1,1,1,1,1,4,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,3,2,1,1,1,1,2,2,1,2,1,1,1,5,5,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,4,2,1,4,1,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,5,1,1,1,1,1,1,1,1,3,1,1,3,3,1,1,1,3,5,1,1,4,1,1,1,1,1,4,1,1,3,1,1,1,1,1,1,1,1,2,1,5,1,1,1,1,1,1,1,1,1,1,4,1,1,1,1]

def run(data, number_of_days):
    results = 0
    tank = {}

    for fish in data:
        tank[fish] = tank.get(fish, 0) + 1

    for day in range(1, number_of_days + 1):
        print(f"Running day {day}")
        new_tank = {}
        number_of_spawning = tank.get(0, 0)
        for key, value in tank.items():
            if key != 0:
                new_tank[key - 1] = value

        new_tank[6] = number_of_spawning + new_tank.get(6, 0)
        new_tank[8] = number_of_spawning

        tank = new_tank

    results = 0
    for key, value in sorted(tank.items()):
        if value != 0:
#                print(f"{key}: {value}")
            results += value

    return results


if __name__ == "__main__":
    results = run(DATA, 256)
    print (results)
