# Advent of Code 2023
# Day 03: Gear Ratios

import numpy as np
from shared_functions import fetch_string_data
from shared_functions import find_neighbors


def parse(raw_data):
    """Return a list of significant symbols and a numpy 2-dimensional array of data."""
    # What's a symbol?
    # I may need to start by processing the input to find everything that's not a digit or a period.
    symbols = []
    for line in raw_data:
        for character in line:
            if (not character.isnumeric()) and (not character == ".") and (character not in symbols):
                symbols.append(character)

    better_data = []
    for line in raw_data:
        line = list(line)
        better_data.append(line)
    better_data = np.array(better_data)
    return symbols, better_data


def find_legal_neighbors(coordinate_pair, upper_bounds):
    legal_neighbor_locs = []
    neighbors = find_neighbors(coordinate_pair)
    for neighbor in neighbors:
        if ((neighbor[0] >= 0) and (neighbor[0] < upper_bounds[0]) and
                (neighbor[1] >= 0) and (neighbor[1] < upper_bounds[1])):
            legal_neighbor_locs.append(neighbor)

    return legal_neighbor_locs


def solve_part_1(symbols, schematic):
    """Identify important numbers in a 2D grid arrangement."""
    print("An elf asks you for help identifying the numbers they need on a schematic diagram.")
    print(schematic)

    upper_bounds = np.shape(schematic)

    # iterate through schematic array to locate the symbols and save their locations in a list
    symbol_locs = []
    for iy, ix in np.ndindex(schematic.shape):
        char = schematic[iy, ix]
        if char in symbols:
            symbol_locs.append((iy, ix))

    # find any digits adjacent to each symbol that haven't already been captured
    digit_locs = []
    for location in symbol_locs:
        neighbors = find_legal_neighbors(location, upper_bounds)
        for neighbor in neighbors:
            if (neighbor not in digit_locs) and schematic[neighbor].isnumeric():
                digit_locs.append(neighbor)

    # for each digit, find the longest string of digits in the same row that contain this digit and capture it to a list
    part_numbers = []
    start_locations = []
    for location in digit_locs:
        working_place = location
        # crawl left until we find the first digit in this number
        while schematic[working_place].isnumeric():
            y, x = working_place
            working_place = y, x-1
        y, x = working_place
        working_place = y, x + 1

        if working_place in start_locations:
            continue    # this means it's a spurious/duplicate number, so go on to the next one
        else:
            start_locations.append(working_place)
            # now crawl right and capture all the consecutive digits to find the part number
            part_number = []
            while schematic[working_place].isnumeric():
                digit = schematic[working_place]
                part_number.append(digit)
                y, x = working_place
                if x == upper_bounds[1] - 1:
                    break
                working_place = y, x + 1

            part_numbers.append(int("".join(part_number)))

    # add up the list of captured numbers and return that as our answer
    print(f"The sum of the part numbers on this schematic is {sum(part_numbers)}.")
    return


def solve_part_2(schematic):
    """Find all the asterisks '*'  adjacent to exactly two numbers and report a score based oon those numbers."""
    print("Wait, we also need to know something about the gears on this schematic.")

    upper_bounds = np.shape(schematic)

    # iterate through schematic array to locate the asterisks and save their locations in a list
    star_locs = []
    for iy, ix in np.ndindex(schematic.shape):
        char = schematic[iy, ix]
        if char == "*":
            star_locs.append((iy, ix))

    # find any digits adjacent to each asterisk
    gears_and_neighbors = dict()
    for star in star_locs:
        star_neighbors = []
        neighbors = find_legal_neighbors(star, upper_bounds)
        for neighbor in neighbors:
            if schematic[neighbor].isnumeric():
                star_neighbors.append(neighbor)
        gears_and_neighbors[star] = star_neighbors

    # for each digit, find the longest string of digits in the same row that contain this digit and capture it to a list
    gear_ratios = []
    for gear in gears_and_neighbors.keys():
        adjacent_nums = []
        part_numbers = []
        for neighbor in gears_and_neighbors[gear]:
            # crawl left until we find the first digit in this number
            working_place = neighbor
            char = schematic[working_place]
            while char.isnumeric():
                y, x = working_place
                working_place = y, x - 1
                char = schematic[working_place]
            y, x = working_place
            working_place = y, x + 1

            if working_place in adjacent_nums:
                continue  # this means it's a spurious/duplicate number, so go on to the next one
            else:
                adjacent_nums.append(working_place)
                # now crawl right and capture all the consecutive digits to find the part number
                part_number = []
                while schematic[working_place].isnumeric():
                    digit = schematic[working_place]
                    part_number.append(digit)
                    y, x = working_place
                    if x == upper_bounds[1] - 1:
                        break
                    working_place = y, x + 1
                part_numbers.append(int("".join(part_number)))
        if len(part_numbers) == 2:
            gear_ratio = part_numbers[0] * part_numbers[1]
            gear_ratios.append(gear_ratio)

    print(f"The sum of the gear ratios on this schematic is {sum(gear_ratios)}.")
    # Yay! it works! That was clumsy but effective.

def solution(filename):
    """Briefly describe the puzzle here."""
    # process data from filename to make it usable by our solving functions
    raw_data = fetch_string_data(filename)
    symbol_list, processed_data = parse(raw_data)

    solve_part_1(symbol_list, processed_data)
    solve_part_2(processed_data)


# This can be run as a script from the command line, with data filename as argument.
if __name__ == "__main__":
    import sys

    try:
        arg = sys.argv[1]
    except IndexError:
        arg = "../data/day_03_input.txt"
        # arg = "../data/day_03_testing.txt"

    print(f"Data file = '{arg}'.")  # debug
    solution(arg)
