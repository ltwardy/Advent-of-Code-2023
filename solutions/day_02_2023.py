# Advent of Code 2023
# Day 02: Cube Conundrum


from shared_functions import fetch_string_data


def parse(raw_data):
    """Return a dictionary of games and their results."""

    clean_data = dict()
    for line in raw_data:
        game, results = line.split(": ")
        rounds_list = results.split("; ")
        good_game = []
        for raw_round in rounds_list:
            raw_round = raw_round.split(", ")
            good_round = {"green": 0, "red": 0, "blue": 0}
            for cube in raw_round:
                cube = cube.split(" ")
                good_round[cube[-1]] = int(cube[0])
            good_game.append(good_round)
        clean_data[int(game[5:])] = good_game

    return clean_data


def solve_part_1(input_data):
    """Decide which games in the input dictionary are possible given the starting conditions."""

    print('''An Elf would like to play a game with you.  Can you figure out how many cubes he has in his bag?''')
    redmax = 12
    greenmax = 13
    bluemax = 14
    game_sum = 0
    for gamenum in input_data.keys():
        print("Game ", gamenum)
        for game_round in input_data[gamenum]:
            print(game_round)
            if (game_round["green"] > greenmax) or (game_round["red"] > redmax) or (game_round["blue"] > bluemax):
                print("Impossible!")
                break
        else:
            game_sum += gamenum
        print()

    print(f"The sum of the ID's of the possible games is {game_sum}.")


def solve_part_2(input_data):
    """Find the minimum cube set to make each game possible."""
    total_score = 0
    for game in input_data.keys():
        print(input_data[game])
        print()
        bluemin = 0
        redmin = 0
        greenmin = 0
        for game_round in input_data[game]:
            green, red, blue = game_round["green"], game_round["red"], game_round["blue"]
            if greenmin < green:
                greenmin = green
            if redmin < red:
                redmin = red
            if bluemin < blue:
                bluemin = blue
        game_power = greenmin * redmin * bluemin
        total_score += game_power

    print(f"The sum of all the powers of individual games is {total_score}")
    # Success! in less than two hours of work, after doing NOTHING Python-related for months!
    # I am very pleased.


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
        arg = "../data/day_02_input.txt"
        # arg = "../data/day_02_testing.txt"

    # print(f"Data file = '{arg}'")  # debug
    solution(arg)
