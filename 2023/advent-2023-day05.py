# pylint: disable=too-many-return-statements,too-many-statements,too-many-branches,duplicate-code,unused-argument
# pylint: disable=unnecessary-list-index-lookup

from collections import defaultdict

FILE_NAME = "2023/input/05.txt"


def run(part: int, test_run: bool = False, debug: bool = False):
    if test_run:
        file = FILE_NAME.replace(".txt", "-test.txt")
    else:
        file = FILE_NAME

    with open(file, encoding="utf-8") as f:
        data = f.readlines()

    data = [x.strip() for x in data]
    part_function = part1 if part == 1 else part2

    return part_function(data, debug)


class Zrange:
    def __init__(self, dest_start: int, source_start: int, length: int):
        self.dest_start = dest_start
        self.dest_end = dest_start + length
        self.source_start = source_start
        self.source_end = source_start + length

    def __repr__(self):
        return f"Zrange({self.source_start}-{self.source_start+self.length}={self.dest_start},{self.dest_start+self.length})"

    def __repr__(self) -> str:
        return f"Zmap({len(self.ranges)})"


class Zmap:
    def __init__(self):
        self.ranges = []

    def add(self, dest_start: int, source_start: int, length: int):
        self.ranges.append(Zrange(dest_start, source_start, length))

    def eval(self, x: int) -> int:
        for range in self.ranges:
            if range.source_start <= x <= range.source_end:
                return x - range.source_start + range.dest_start
        else:
            return x


def part1(data: list[str], debug: bool = False) -> int:
    results = 0

    seeds = set(data.pop(0).split(": ")[1].split(" "))
    data.pop(0)

    data.pop(0)
    seed_soil_map = process_map(data)
    data.pop(0)
    soil_fertilizer_map = process_map(data)
    data.pop(0)
    fertilizer_water_map = process_map(data)
    data.pop(0)
    water_light_map = process_map(data)
    data.pop(0)
    light_temp_map = process_map(data)
    data.pop(0)
    temp_humidity_map = process_map(data)
    data.pop(0)
    humidity_location_map = process_map(data)

    locations = []
    for s in seeds:
        seed = int(s)
        soil = seed_soil_map.eval(seed)
        fertilizer = soil_fertilizer_map.eval(soil)
        water = fertilizer_water_map.eval(fertilizer)
        light = water_light_map.eval(water)
        temp = light_temp_map.eval(light)
        humidity = temp_humidity_map.eval(temp)
        location = humidity_location_map.eval(humidity)

        locations.append(location)

    return min(locations)


def process_map(data: list[str]) -> dict:
    zmap = Zmap()
    while data:
        line = data.pop(0)
        if line == "":
            break

        dest, source, length = line.split(" ")
        zmap.add(int(dest), int(source), int(length))

    return zmap


def process_map_reverse(data: list[str]) -> dict:
    zmap = Zmap()
    while data:
        line = data.pop(0)
        if line == "":
            break

        source, dest, length = line.split(" ")
        zmap.add(int(dest), int(source), int(length))

    return zmap


def part2(data: list[str], debug: bool = False) -> int:
    seeds = data.pop(0).split(": ")[1].split(" ")
    seed_list = []
    for x in range(0, len(seeds), 2):
        seed_start = int(seeds[x])
        seed_length = int(seeds[x + 1])
        seed_list.append((seed_start, seed_start + seed_length))

    data.pop(0)

    data.pop(0)
    seed_soil_map = process_map_reverse(data)
    data.pop(0)
    soil_fertilizer_map = process_map_reverse(data)
    data.pop(0)
    fertilizer_water_map = process_map_reverse(data)
    data.pop(0)
    water_light_map = process_map_reverse(data)
    data.pop(0)
    light_temp_map = process_map_reverse(data)
    data.pop(0)
    temp_humidity_map = process_map_reverse(data)
    data.pop(0)
    humidity_location_map = process_map_reverse(data)

    location = 20191102
    while location <= 20191103:
        humidity = humidity_location_map.eval(location)
        temp = temp_humidity_map.eval(humidity)
        light = light_temp_map.eval(temp)
        water = water_light_map.eval(light)
        fertilizer = fertilizer_water_map.eval(water)
        soil = soil_fertilizer_map.eval(fertilizer)
        seed = seed_soil_map.eval(soil)

        for seed_range in seed_list:
            if seed_range[0] <= seed <= seed_range[1]:
                return location

        location += 1

        if location % 250000 == 0:
            print(f"{location:,}")

    return None


if __name__ == "__main__":
    # final = run(part=1, test_run=True, debug=True) # 35
    # final = run(part=1, test_run=False, debug=False)  # 600279879
    # final = run(part=2, test_run=True, debug=True) # 46
    final = run(
        part=2, test_run=False, debug=False
    )  # 20,191,103 is too high and 15,000,000 is too low
    print("ANSWER:", final)
