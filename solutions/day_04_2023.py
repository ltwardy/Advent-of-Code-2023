# Advent of Code 2023
# Day 04: Scratchcards


from shared_functions import fetch_string_data


# def intersection(card:tuple):
#     list1, list2 = card
#     return set(list1) & set(list2)

def find_winning_numbers(card:tuple):
    reference, my_nums = card
    winners = []
    for num in my_nums:
        if num in reference:
            winners.append(num)
    return winners


def parse(raw_data):
    """Make our input more useful for problem-solving."""
    # return a list of tuples, each one a pair of lists of integers

    def list_from_string(string_of_numbers):
        nums = string_of_numbers.split(" ")
        ints = [int(num) for num in nums if num.isnumeric()]
        return ints

    useful_data = []
    for line in raw_data:
        line = line.split(": ")
        line = line[1].split(" | ")
        useful_card = (list_from_string(line[0]), list_from_string(line[1]))
        useful_data.append(useful_card)

    return useful_data

def solve_part_1(input_data):
    """Describe the puzzle."""
    winners = [find_winning_numbers(line) for line in input_data]
    points = []
    for line in winners:
        how_many_winners = len(line)
        if how_many_winners == 0:
            continue
        else:
            card_points = 2 ** (how_many_winners - 1)
        points.append(card_points)
    score = sum(points)
    print(f"The total points on these scratchcards is {score}")
    # yay! finally!


def solve_part_2(input_data):
    """Describe the next puzzle."""
    pass


def solution(filename):
    """Take a collection of list pairs and find which numbers in the second list are also in the first."""
    # process data from filename to make it usable by our solving functions
    raw_data = fetch_string_data(filename)
    processed_data = parse(raw_data)

    print("An elf needs help adding up their lottery winnings.")
    solve_part_1(processed_data)
    solve_part_2(processed_data)


# This can be run as a script from the command line, with data filename as argument.
if __name__ == "__main__":
    import sys

    try:
        arg = sys.argv[1]
    except IndexError:
        # arg = "testing.txt"
        arg = "../data/day_04_input.txt"
        # arg = "../data/day_04_testing.txt"


    print(f"Data file = '{arg}'.")  # debug
    solution(arg)
