# Advent of Code 2023
# Day 05: If You Give A Seed A Fertilizer


from shared_functions import fetch_string_data


def parse(raw_data):
    """Make our input more useful for problem-solving."""
    line = raw_data.pop(0)
    if not line.startswith("seeds:"):
        raise ValueError("First line should be seed list but is not.")
    line = line.split(" ")
    line.pop(0)
    seeds = [int(seed) for seed in line]

    maps = dict()
    map = []
    raw_data.pop(0)
    while raw_data:
        line = raw_data.pop(0)
        if line == "":
            # print(map)
            maps[map[0]] = map[1:]
            map = []
            # print(maps)
            continue
        elif "map" in line:
            line = line.split(" ")
            map.append(line[0])
        else:
            line = line.split(" ")
            line = [int(char) for char in line]
            map.append(tuple(line))

    return seeds, maps


def solve_part_1(input_data):
    """Describe the puzzle."""
    seeds, maps = input_data
    print(f"{seeds=}")
    print(f"{maps=}")

    def perform_transform(value, transform):
        result = value
        instructions = maps[transform]
        for line in instructions:
            if line[1] <= value < (line[1] + line[2]):
                result = line[0] + (value - line[1])
                break
        return result

    # for seed in seeds:
    #     soil = perform_transform(seed, "seed-to-soil")
    #     print(seed, " becomes ", soil)

    soils = [perform_transform(seed, "seed-to-soil") for seed in seeds]
    ferts = [perform_transform(soil, "soil-to-fertilizer") for soil in soils]
    waters = [perform_transform(fert, "fertilizer-to-water") for fert in ferts]
    lights = [perform_transform(water, "water-to-light") for water in waters]
    temps = [perform_transform(light, "light-to-temperature") for light in lights]
    humids = [perform_transform(temp, "temperature-to-humidity") for temp in temps]
    locs = [perform_transform(humid, "humidity-to-location") for humid in humids]

    print(f"The lowest numbered location for this set of seeds is {min(locs)}")
    # I'm so pleased that this worked.

def solve_part_2(input_data):
    """Describe the next puzzle."""
    pass


def solution(filename):
    """Briefly describe the puzzle here."""
    # process data from filename to make it usable by our solving functions
    raw_data = fetch_string_data(filename)
    processed_data = parse(raw_data)

    solve_part_1(processed_data)
    solve_part_2(processed_data)


# This can be run as a script from the command line, with data filename as argument.
if __name__ == "__main__":
    import sys

    try:
        arg = sys.argv[1]
    except IndexError:
        # arg = "testing.txt"
        # arg = "../data/day_05_input.txt"
        arg = "../data/day_05_testing.txt"


    print(f"Data file = '{arg}'.")  # debug
    solution(arg)
