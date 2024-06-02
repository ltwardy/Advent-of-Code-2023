# Advent of Code 2023
# Day 06: Wait For It


from shared_functions import fetch_string_data


def fix_kerning(clean_data):
    print(clean_data)
    time = []
    distance = []
    for line in clean_data:
        time.append(str(line[0]))
        distance.append(str(line[1]))
    time = int("".join(time))
    distance = int("".join(distance))
    # print(time, distance)
    return time, distance


def parse(raw_data):
    """Make our input more useful for problem-solving."""

    better_data = []
    for line in raw_data:
        better_data.append(line.split(" "))

    best_data = []
    line2 = []
    for line in better_data:
        for element in line:
            if element != "":
                line2.append(element)
        best_data.append(line2)
        line2 = []

    time_distance = []
    for index in range(1, len(best_data[0])):
        time_distance.append((int(best_data[0][index]), int(best_data[1][index])))
    print(time_distance)
    return time_distance


def solve_part_1(input_data):
    """Choose how long to hold a button down to get a toy boat to move far enough."""

    ways_to_win = []
    for race in input_data:
        win_count = 0
        # print(f"Race duration = {race[0]}, winning distance = {race[1]}")
        total_time, winning_distance = race
        for elapsed in range(total_time):
            travel = elapsed * (total_time - elapsed)
            if travel > winning_distance:
                win_count += 1
        # print(win_count)
        ways_to_win.append(win_count)

    permutes = 1
    for way in ways_to_win:
        permutes = permutes * way
    print(f"There are {permutes} combinations of winning times to these races.")
    # Yay! It works!


def solve_part_2(input_data):
    """Choose how long to hold the button for a single long race."""
    total_time, winning_distance = fix_kerning(input_data)
    win_range = []
    for elapsed in range(total_time):
        travel = elapsed * (total_time - elapsed)
        if travel > winning_distance:
            win_range.append(elapsed)
            break
    for elapsed in range(total_time, 0, -1):
        travel = elapsed * (total_time - elapsed)
        if travel > winning_distance:
            win_range.append(elapsed)
            break
    # print(win_range)
    ways_to_win = 1 + win_range[1] - win_range[0]
    print()
    print(f"In the single long race, there are {ways_to_win} ways to win.")


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
        arg = "../data/day_06_input.txt"
        # arg = "../data/day_06_testing.txt"

    print(f"Data file = '{arg}'.")  # debug
    solution(arg)
