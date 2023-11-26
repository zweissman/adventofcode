DATA_TEST = [3,4,3,1,2]
DATA = [1,1,3,5,1,1,1,4,1,5,1,1,1,1,1,1,1,3,1,1,1,1,2,5,1,1,1,1,1,2,1,4,1,4,1,1,1,1,1,3,1,1,5,1,1,1,4,1,1,1,4,1,1,3,5,1,1,1,1,4,1,5,4,1,1,2,3,2,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,5,1,1,1,3,4,1,1,1,1,3,1,1,1,1,1,4,1,1,3,1,1,3,1,1,1,1,1,3,1,5,2,3,1,2,3,1,1,2,1,2,4,5,1,5,1,4,1,1,1,1,2,1,5,1,1,1,1,1,5,1,1,3,1,1,1,1,1,1,4,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,3,2,1,1,1,1,2,2,1,2,1,1,1,5,5,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,4,2,1,4,1,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,5,1,1,1,1,1,1,1,1,3,1,1,3,3,1,1,1,3,5,1,1,4,1,1,1,1,1,4,1,1,3,1,1,1,1,1,1,1,1,2,1,5,1,1,1,1,1,1,1,1,1,1,4,1,1,1,1]
TANK = []

class FishClass(object):
    def __init__(self, countdown, breed_cycle):
        self.id = len(TANK) + 1
        self.countdown = countdown
        self.breed_cycle = breed_cycle

    def new_day(self):
        if self.countdown == 0:
            # Spawn new
            fish = type(self)(self.breed_cycle + 1)
            TANK.append(fish)

            self.countdown = self.breed_cycle - 1
        else:
            self.countdown -= 1

    def __repr__(self):
         return f"{self.id}: {self.countdown} of {self.breed_cycle}"

    def __str__(self):
        return f"{self.id}: {self.countdown} of {self.breed_cycle}"

class Lanternfish(FishClass):
    LANTERNFISH_BREED_CYCLE = 7

    def __init__(self, countdown):
        super().__init__(countdown, self.LANTERNFISH_BREED_CYCLE)

def run(data, number_of_days):
    results = 0

    setup_tank(data)

    for day in range(1, number_of_days + 1):
        print(f"Running day {day}")
        for index in range(len(TANK)):
            # Run the range like this so we don't trigger a new day for new fish added to the tank today.
            fish = TANK[index]
            fish.new_day()

        # for fish in TANK:
        #     print(fish)

    return len(TANK)

def setup_tank(data):
    for fish in data:
        new_fish = Lanternfish(fish)
        TANK.append(new_fish)

if __name__ == "__main__":
    results = run(DATA, 80)
    print (results)
