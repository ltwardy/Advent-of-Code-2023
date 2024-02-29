# Advent of Code 2023
# Day 01: Trebuchet

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
        num12 = 10*num1 + num2
        numbers.append(num12)

    total = sum(numbers)
    print(f'The correction factor should be {total}.')
    print()
    # bing! correct!

def solve_part_2(input_data):
    """Now parse the same dataset, treating speller-out number words as the numbers they mean."""

    print('''Oops! You didn't take into account the elves habit of using spelled-out numbers 
    as well as numerical digits on their paperwork. ''')

    spelled_out_nums = {"one":1,
                  "two":2,
                  "three":3,
                  "four":4,
                  "five":5,
                  "six":6,
                  "seven":7,
                  "eight":8,
                  "nine":9,
                  "zero":0}
    def number_word(stringdata):
        numstring = "onetwothreefourfivesixseveneightninezero"
        if stringdata in numstring:
            return stringdata
        elif stringdata[:4] in numstring:
            return stringdata[:4]
        elif stringdata[:3] in numstring:
            return stringdata[:3]
        else:
            return False

    def spells_a_number_backward(stringdata):
        numstring = "onetwothreefourfivesixseveneightninezero"
        if stringdata in numstring:
            return stringdata
        elif stringdata[1:] in numstring:
            return stringdata[1:]
        elif stringdata[2:] in numstring:
            return stringdata[2:]
        else:
            return False

    corrected_data = []
    for line in input_data:
        print(line)
        corrected_line = []
        line1 = line + "....."
        for count, character in enumerate(line1):
            window = line1[count:count + 5]
            print(window)
            if window[0].isnumeric():   # that is, the text block starts with a digit
                corrected_line.append(window[0])
                break
            if number_word(window):
                corrected_line.append(spelled_out_nums[number_word(window)])
            else:
                continue

        line2 = "....." + line[::-1] + "....."
        print(line2)
        for count, character in enumerate(line2):
            window = line2[count:count+5]
            print(window)
            if window[0].isnumeric():   # that is, the text block starts with a digit
                corrected_line.append(window[0])
                break
            if spells_a_number_backward(window[::-1]):
                corrected_line.append(number_word(spelled_out_nums[window[::-1]]))
            else:
                continue
        print(corrected_line)
        corrected_data.append(corrected_line)

    numbers = []
    for line in corrected_data:
        num1 = int(line[0])
        num2 = int(line[1])
        num12 = 10*num1 + num2
        numbers.append(num12)
    print(numbers)
    total = sum(numbers)
    print(f'The correction factor should actually be {total}.')

    pass


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
        # arg = '../data/day_01.txt'
        arg = "../data/day_01.txt"

    print(f"Data file = '{arg}'.")  # debug
    solution(arg)
