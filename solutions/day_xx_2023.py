# Advent of Code 2023
# Day XX: Puzzle name


from shared_functions import fetch_string_data


def parse(raw_data):
    """Make our input more useful for problem-solving."""
    pass


def solve_part_1(input_data):
    """Describe the puzzle."""
    pass


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
        # arg = "../data/day_xx_input.txt"
        # arg = "../data/day_xx_testing.txt"


    print(f"Data file = '{arg}'.")  # debug
    solution(arg)
