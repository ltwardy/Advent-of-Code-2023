# Advent of Code 2023
# Day 01: Trebuchet?!

import sys

sys.path.append("/")

from shared_functions import fetch_string_data


def parse(raw_data):
    """Make our input more useful for problem-solving. in this case, nothing is needed."""
    return raw_data


def solve_part_1(input_data):
    """Parse a series of alphanumeric strings to extract the correct numerical information."""

    print('''The elves need you to find out why something is wrong with global snow production.
    To this end, they are about to fling you into the sky using a giant trebuchet.  Unfortunately, 
    it needs to be calibrated first, and the calibration document is hard to read. 
    Can you decode the mess and get the correct numbers?''')

    corrected_data = []
    for line in input_data:
        corrected_line = []
        for character in line:
            if character.isnumeric():
                corrected_line.append(character)
                break
        line = line[::-1]
        for character in line:
            if character.isnumeric():
                corrected_line.append(character)
                break
        corrected_data.append(corrected_line)

    numbers = []
    for line in corrected_data:
        num1 = int(line[0])
        num2 = int(line[1])
        num12 = 10 * num1 + num2
        numbers.append(num12)

    total = sum(numbers)
    print(f'The correction factor should be {total}.')
    print()
    # bing! correct!


def solve_part_2(input_data):
    """Now parse the same dataset, treating spelled-out number words as the numbers they mean."""

    print('''Oops! You didn't take into account the elves habit of using spelled-out numbers as well as numerical digits
     on their paperwork. ''')

    spelled_out_nums = {"one": 1,
                        "two": 2,
                        "three": 3,
                        "four": 4,
                        "five": 5,
                        "six": 6,
                        "seven": 7,
                        "eight": 8,
                        "nine": 9,
                        "zero": 0}

    reverse_nums = {"eno": 1,
                    "owt": 2,
                    "eerht": 3,
                    "ruof": 4,
                    "evif": 5,
                    "xis": 6,
                    "neves": 7,
                    "thgie": 8,
                    "enin": 9,
                    "orez": 0}

    corrected_data = []
    for line in input_data:
        corrected_line = []

        # find the first number
        for index, character in enumerate(line):
            if character.isnumeric():
                corrected_line.append(int(character))
                break
            else:
                if character in "otfsenz":
                    window3 = line[index:index + 3]
                    if window3 in spelled_out_nums.keys():
                        corrected_line.append(spelled_out_nums[window3])
                        break
                    window4 = line[index:index + 4]
                    if window4 in spelled_out_nums.keys():
                        corrected_line.append(spelled_out_nums[window4])
                        break
                    window5 = line[index:index + 5]
                    if window5 in spelled_out_nums.keys():
                        corrected_line.append(spelled_out_nums[window5])
                        break

        # find the second number
        line = line[::-1]
        for index, character in enumerate(line):
            if character.isnumeric():
                corrected_line.append(int(character))
                break
            else:
                if character in "eorxnt":
                    window3 = line[index:index + 3]
                    if window3 in reverse_nums.keys():
                        corrected_line.append(reverse_nums[window3])
                        break
                    window4 = line[index:index + 4]
                    if window4 in reverse_nums.keys():
                        corrected_line.append(reverse_nums[window4])
                        break
                    window5 = line[index:index + 5]
                    if window5 in reverse_nums.keys():
                        corrected_line.append(reverse_nums[window5])
                        break

        corrected_data.append(corrected_line)

    numbers = []
    for line in corrected_data:
        num1 = int(line[0])
        num2 = int(line[1])
        num12 = 10 * num1 + num2
        numbers.append(num12)
    # print(numbers)
    total = sum(numbers)
    print(f'The correction factor should actually be {total}.')
    # Yay! this works too! (Came back to it in February and threw out my first effort as even more graceless than this.)


def solution(filename):
    """From a list of strings, extract useful numerical information."""

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
        arg = '../data/day_01_input.txt'
        # arg = "../data/day_01_testing1.txt"
        # arg = "../data/day_01_testing2.txt"

    print(f"Data file = '{arg}'.")  # debug
    solution(arg)
