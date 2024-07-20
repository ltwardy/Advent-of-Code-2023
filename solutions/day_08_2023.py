# Advent of Code 2023
# Day 08: Haunted Wasteland


from shared_functions import fetch_string_data


def parse(raw_data):
    """Make our input more useful for problem-solving."""

    raw_pattern = raw_data.pop(0)
    raw_pattern = [letter for letter in raw_pattern]
    pattern = []
    for letter in raw_pattern:
        if letter == "R":
            pattern.append(1)
        elif letter == "L":
            pattern.append(0)
        else:
            raise ValueError
    _null = raw_data.pop(0)

    better_data = dict()
    for line in raw_data:
        new_line = line.split(" = ")
        key = new_line[0]
        wordpair = new_line[1]
        word1 = wordpair[1:4]
        word2 = wordpair[-4:-1]
        wordpair = (word1, word2)
        better_data[key] = wordpair
    return pattern, better_data


def solve_part_1(input_data):
    """Choose left or right elements from each pair as instructed until reaching the endpoint"""
    pattern, nodelist = input_data
    print(pattern)
    print(nodelist)
    cursor = "AAA"
    endpoint = "ZZZ"
    directions = [letter for letter in pattern]
    step = directions[0]
    count = 0
    while cursor != endpoint:
        print(cursor, "--->", nodelist[cursor])
        # print(directions[step])
        cursor = nodelist[cursor][(directions[step])]
        print(cursor)
        step += 1
        step = step % len(directions)
        count += 1

    print(f"This set of instructions terminated after {count} instructions.")
    # Success! That wasn't too bad...but part two looks hideous.



def solve_part_2(input_data):
    """Describe the next puzzle."""
    pass


def solution(filename):
    """Follow the directions to escape a haunted desert."""
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
        arg = "../data/day_08_input.txt"
        # arg = "../data/day_08_testing1.txt"
        # arg = "../data/day_08_testing2.txt"


    print(f"Data file = '{arg}'.")  # debug
    solution(arg)
