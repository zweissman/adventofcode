from math import lcm


class Signal:
    def __init__(self, module_to, module_from, signal_level):
        self.module_to = module_to
        self.module_from = module_from
        self.signal_level = signal_level

    def __repr__(self):
        return f"{self.module_from} -{self.signal_level}-> {self.module_to}"


class Module:
    def __init__(self, name: str, command_line: str):
        self.name = name
        self.command_line = command_line
        self.type = "Unknown"

    def __repr__(self):
        return f"{self.type}[{self.name}] -> {self.command_line}"

    def get_name(self) -> str:
        return self.name

    def input(self, signal: Signal) -> list[Signal]:  # pylint: disable=unused-argument
        return self.output()

    def output(self) -> list[Signal]:
        return []

    def update_references(self, module_reference_name: str) -> None:
        pass


class FlipFlopModule(Module):
    def __init__(self, name: str, command_line: str):
        super().__init__(name, command_line)
        self.state = False
        self.type = "FF"

    def __repr__(self) -> str:
        return f"{super().__repr__()} || {self.state}"

    def input(self, signal: Signal) -> list[Signal]:
        if signal.signal_level == "low":
            self.state = not self.state
            return self.output()

        return []

    def output(self) -> list[Signal]:
        results = []

        if self.state:
            signal_level = "high"
        else:
            signal_level = "low"

        for module_to in self.command_line.split(", "):
            results.append(Signal(module_to, self.name, signal_level))

        return results


class ConjunctionModule(Module):
    def __init__(self, name: str, command_line: str):
        super().__init__(name, command_line)
        self.inputs: dict[str, str] = {}
        self.type = "Conj"

    def __repr__(self) -> str:
        return f"{super().__repr__()} || {self.inputs}"

    def update_references(self, module_reference_name: str) -> None:
        self.inputs[module_reference_name] = "low"

    def input(self, signal: Signal) -> list[Signal]:
        self.inputs[signal.module_from] = signal.signal_level
        return self.output()

    def output(self) -> list[Signal]:
        signal_level = "low"

        for _, v in self.inputs.items():
            if v != "high":
                signal_level = "high"
                break

        results: list[Signal] = []
        for module_to in self.command_line.split(", "):
            results.append(Signal(module_to, self.name, signal_level))

        return results


class BroadcasterModule(Module):
    def __init__(self, name: str, command_line: str):
        super().__init__(name, command_line)
        self.type = "BC"

    def input(self, signal: Signal) -> list[Signal]:
        return self.output()

    def output(self) -> list[Signal]:
        results = []
        commands = self.command_line.split(", ")

        for module_to in commands:
            results.append(Signal(module_to, self.name, "low"))

        return results


def run(part: int, test_run: bool = False, debug: bool = False):
    file_name = "2023/input/20.txt"
    if test_run:
        file_name = file_name.replace(".txt", "-test.txt")

    with open(file_name, encoding="utf-8") as file:
        file_data = file.readlines()

    data = [x.strip() for x in file_data]
    part_function = part1 if part == 1 else part2

    return part_function(data=data, debug=debug)


def part1(data: list[str], debug: bool = False) -> int:
    results = 0
    modules: dict[str, Module] = {}
    signals: list[Signal] = []

    for line in data:
        if line.startswith("#"):
            continue

        module_name, command_line = line.split(" -> ")
        if module_name == "broadcaster":
            modules[module_name] = BroadcasterModule(module_name, command_line)
        elif module_name.startswith("%"):
            module_name = module_name[1:]
            modules[module_name] = FlipFlopModule(module_name, command_line)
        elif module_name.startswith("&"):
            module_name = module_name[1:]
            modules[module_name] = ConjunctionModule(module_name, command_line)
        else:
            raise Exception(f"Unknown module type: {line}")

    for line in data:
        if line.startswith("#"):
            continue
        module_name, command_line = line.split(" -> ")
        module_name = module_name[1:]
        for module_to in command_line.split(", "):
            if module_to != "output":
                if module_to in modules:
                    modules[module_to].update_references(module_name)

    low, high = 0, 0
    for button_presses in range(1, 1001):
        if debug:
            print(f"\n{button_presses=}")
        low += 1
        signals.extend(modules["broadcaster"].output())

        while signals:
            signal = signals.pop(0)

            if signal.signal_level == "low":
                low += 1
            else:
                high += 1

            if debug:
                print(signal)

            if signal.module_to != "output":
                if signal.module_to in modules:
                    outputs = modules[signal.module_to].input(signal)
                    signals.extend(outputs)

        if debug:
            print(low, high, low * high)

    results = low * high

    return results


def part2(data: list[str], debug: bool = False) -> int:
    modules: dict[str, Module] = {}
    signals: list[Signal] = []

    for line in data:
        if line.startswith("#"):
            continue

        module_name, command_line = line.split(" -> ")
        if module_name == "broadcaster":
            modules[module_name] = BroadcasterModule(module_name, command_line)
        elif module_name.startswith("%"):
            module_name = module_name[1:]
            modules[module_name] = FlipFlopModule(module_name, command_line)
        elif module_name.startswith("&"):
            module_name = module_name[1:]
            modules[module_name] = ConjunctionModule(module_name, command_line)
        else:
            raise Exception(f"Unknown module type: {line}")

    for line in data:
        if line.startswith("#"):
            continue
        module_name, command_line = line.split(" -> ")
        module_name = module_name[1:]
        for module_to in command_line.split(", "):
            if module_to != "output":
                if module_to in modules:
                    modules[module_to].update_references(module_name)

    button_presses = 0
    results = {}
    while True:
        button_presses += 1
        if button_presses % 1000 == 0:
            print(f"{button_presses=}")

        if debug:
            print(f"\n{button_presses=}")
        signals.extend(modules["broadcaster"].output())

        while signals:
            signal = signals.pop(0)

            if debug:
                print(signal)

            if signal.module_to != "output":
                if signal.module_to in modules:
                    outputs = modules[signal.module_to].input(signal)
                    signals.extend(outputs)

            for k, v in modules["cl"].inputs.items():  # type: ignore[attr-defined]
                if v == "high":
                    if k not in results:
                        print(k, button_presses)
                        results[k] = button_presses

            if len(results) == 4:
                return lcm(*results.values())


if __name__ == "__main__":
    # print("Test1: ", run(part=1, test_run=True, debug=True))  # 11687500
    # print("Real1: ", run(part=1, test_run=False, debug=False))  # 938065580
    # TODO: BROKEN
    # print("Test2: ", run(part=2, test_run=True, debug=True))  #
    print("Real2: ", run(part=2, test_run=False, debug=False))  # 250628960065793
