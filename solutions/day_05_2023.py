# Advent of Code 2023
# Day 05: If You Give A Seed A Fertilizer


from shared_functions import fetch_string_data


def generate_values(start,end):
    for item in range(start, end + 1):
        yield item

def parse(raw_data):
    """Make our input more useful for problem-solving."""
    line = raw_data.pop(0)
    if not line.startswith("seeds:"):
        raise ValueError("First line should be seed list but is not.")
    line = line.split(" ")
    line.pop(0)
    seeds = [int(seed) for seed in line]

    maps = dict()
    mapi = []
    raw_data.pop(0)
    while raw_data:
        line = raw_data.pop(0)
        if line == "":
            # print(map)
            maps[mapi[0]] = mapi[1:]
            mapi = []
            # print(maps)
            continue
        elif "map" in line:
            line = line.split(" ")
            mapi.append(line[0])
        else:
            line = line.split(" ")
            line = [int(char) for char in line]
            mapi.append(tuple(line))

    return seeds, maps


def solve_part_1(input_data):
    """Use a byzantine set of transformations to convert seed numbers to numbered locations."""
    seeds, maps = input_data

    def perform_transform(value, transform):
        result = value
        instructions = maps[transform]
        for line in instructions:
            if line[1] <= value < (line[1] + line[2]):
                result = line[0] + (value - line[1])
                break
        return result


    soils = [perform_transform(seed, "seed-to-soil") for seed in seeds]
    ferts = [perform_transform(soil, "soil-to-fertilizer") for soil in soils]
    waters = [perform_transform(fert, "fertilizer-to-water") for fert in ferts]
    lights = [perform_transform(water, "water-to-light") for water in waters]
    temps = [perform_transform(light, "light-to-temperature") for light in lights]
    humids = [perform_transform(temp, "temperature-to-humidity") for temp in temps]
    locs = [perform_transform(humid, "humidity-to-location") for humid in humids]

    print(f"The lowest numbered location for this set of seeds is {min(locs)}")
    print()
    # I'm so pleased that this worked.



def solve_part_2(input_data):
    """Do the same thing, but with more numbers."""

    def perform_transform(value, transform):
        result = value
        instructions = maps[transform]
        for line in instructions:
            if line[1] <= value < (line[1] + line[2]):
                result = line[0] + (value - line[1])
                break
        return result

    seeds, maps = input_data
    print(f"{seeds=}")
    print("maps=")
    for page in maps.keys():
        print("     ", maps[page])

    more_seeds = []
    for i, seed_start in enumerate(seeds):
        print(i, seed_start)
        if i == len(seeds) - 1:
            break
        elif i % 2 == 0:
            # print("odd")
            seedset_length = seeds[i+1]
            seed_end = seed_start + seedset_length - 1
            new_seeds = (seed_start, seed_end )
            more_seeds.append(new_seeds)
        # else:
            # print("even")

    print()
    # print(more_seeds)
    # print(maps)

    minimums = []
    for seed_set in  more_seeds:
        print(seed_set)
        soils = [perform_transform(seed, "seed-to-soil") for seed in generate_values(*seed_set)]
        # soils = [perform_transform(seed, "seed-to-soil") for seed in more_seeds]
        ferts = [perform_transform(soil, "soil-to-fertilizer") for soil in soils]
        waters = [perform_transform(fert, "fertilizer-to-water") for fert in ferts]
        lights = [perform_transform(water, "water-to-light") for water in waters]
        temps = [perform_transform(light, "light-to-temperature") for light in lights]
        humids = [perform_transform(temp, "temperature-to-humidity") for temp in temps]
        locs = [perform_transform(humid, "humidity-to-location") for humid in humids]
        # print(locs)
        minimums.append(min(locs))
        print(minimums)

    print(f"The lowest numbered location for this set of seeds is {min(minimums)}")
    # At last it works for the test data...
    # but it's super slow for the real data :(



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
        arg = "../data/day_05_input.txt"
        # arg = "../data/day_05_testing.txt"


    print(f"Data file = '{arg}'.")  # debug
    solution(arg)
