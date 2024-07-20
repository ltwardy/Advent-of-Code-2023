# Advent of Code 2023
# Day 07: Camel Cards


from shared_functions import fetch_string_data


def of_a_kind(aaaaa):
    hand = [a for a in aaaaa]
    unique = set(hand)
    maxcount = 0
    for card in unique:
        cardcount = 0
        for orig in hand:
            if card == orig:
                cardcount += 1
        if cardcount > maxcount:
            maxcount = cardcount

    return maxcount


def find_type_1(aaaaa):
    _type = {"five": 7,
             "four": 6,
             "fullhouse": 5,
             "three": 4,
             "twopair": 3,
             "onepair": 2,
             "highcard": 1
             }
    hand = sorted(aaaaa)
    if len(set(hand)) == 1:
        return 7
    elif len(set(hand)) == 2 and of_a_kind(hand) == 4:
        return 6
    elif len(set(hand)) == 2 and of_a_kind(hand) == 3:
        return 5
    elif len(set(hand)) == 3 and of_a_kind(hand) == 3:
        return 4
    elif len(set(hand)) == 3 and of_a_kind(hand) == 2:
        return 3
    elif len(set(hand)) == 4:
        return 2
    elif len(set(hand)) == 5:
        return 1
    else:
        raise ValueError("Hand1 type not found")


def compare_hands_1(aaaaa, bbbbb):
    a = [char for char in aaaaa]
    b = [char for char in bbbbb]

    card_order = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3,
                  "2": 2}

    for index, _card in enumerate(a):
        if card_order[a[index]] > card_order[b[index]]:
            return 1
        elif card_order[a[index]] < card_order[b[index]]:
            return -1
        else:
            continue
    return 0


class Hand1:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.type = find_type_1(cards)

    def __str__(self):
        return f"cards = {self.cards}, bid = {self.bid}"

    def __repr__(self):
        return f"Hand1(\"{self.cards}\", {self.bid})"

    def __gt__(self, other):
        if self.type > other.type:
            return True
        elif self.type == other.type and compare_hands_1(self.cards, other.cards) == 1:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.cards == other.cards:
            return True
        else:
            return False

    def hand_type(self):
        print(self.cards)


# ----------------------------------------------------------------------------------------------------------------#

def find_type_2(aaaaa):
    _type = {"five": 7,
             "four": 6,
             "fullhouse": 5,
             "three": 4,
             "twopair": 3,
             "onepair": 2,
             "highcard": 1
             }
    hand = sorted(aaaaa)
    if "J" not in hand:
        if len(set(hand)) == 1:  # 5 of a kind
            return 7
        elif len(set(hand)) == 2 and of_a_kind(hand) == 4:  # 4 of a kind
            return 6
        elif len(set(hand)) == 2 and of_a_kind(hand) == 3:  # Full House
            return 5
        elif len(set(hand)) == 3 and of_a_kind(hand) == 3:  # 3 of a kind
            return 4
        elif len(set(hand)) == 3 and of_a_kind(hand) == 2:  # 2 pairs
            return 3
        elif len(set(hand)) == 4:  # 1 pair
            return 2
        elif len(set(hand)) == 5:  # high card (all different)
            return 1
        else:
            raise ValueError("Hand1 type not found")
    else:
        jcount = 0
        for character in hand:
            if character == "J":
                jcount += 1
        if len(set(hand)) == 1:
            return 7  # 5 of a kind is still 5oak if they're all jacks
        elif len(set(hand)) == 2 and of_a_kind(hand) == 4:
            return 7  # 4 of a kind becomes 5 of a kind
        elif len(set(hand)) == 2 and of_a_kind(hand) == 3:
            return 7  # FH becomes 5 of a kind
        elif len(set(hand)) == 3 and of_a_kind(hand) == 3:
            return 6  # 3 of a kind becomes 4 of a kind
        elif len(set(hand)) == 3 and of_a_kind(hand) == 2:
            if jcount == 1:
                return 5  # 2 pairs, 1 jack becomes full house
            elif jcount == 2:
                return 6  # 2 pairs, 2 jacks becomes 4 of a kind
            else:
                raise ValueError("Jack count doesn't match hand options")
        elif len(set(hand)) == 4:
            return 4  # 1 pair becomes 3 of a kind
        elif len(set(hand)) == 5:
            return 2  # high card becomes 1 pair
        else:
            raise ValueError("Hand1 type not found")


def compare_hands_2(aaaaa, bbbbb):
    a = [char for char in aaaaa]
    b = [char for char in bbbbb]

    card_order = {"A": 14, "K": 13, "Q": 12, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2,
                  "J": 1}

    for index, _card in enumerate(a):
        if card_order[a[index]] > card_order[b[index]]:
            return 1
        elif card_order[a[index]] < card_order[b[index]]:
            return -1
        else:
            continue
    return 0


class Hand2:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.type = find_type_2(cards)

    def __str__(self):
        return f"cards = {self.cards}, bid = {self.bid}"

    def __repr__(self):
        return f"Hand2(\"{self.cards}\", {self.bid})"

    def __gt__(self, other):
        if self.type > other.type:
            return True
        elif self.type == other.type and compare_hands_2(self.cards, other.cards) == 1:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.cards == other.cards:
            return True
        else:
            return False

    def hand_type(self):
        print(self.cards)


def parse(raw_data):
    """Make our input more useful for problem-solving."""
    all_hands = []
    for line in raw_data:
        cards, bid = line.split(" ")
        line = Hand1(cards, int(bid))
        all_hands.append(line)
    return all_hands


def solve_part_1(input_data):
    """Parse a set of hands of cards, order them correctly, and find the total score."""
    ordered_hands = sorted(input_data)
    # print(ordered_hands)
    score = 0
    for index, hand in enumerate(ordered_hands):
        # print(index, hand)
        score += ((index + 1) * hand.bid)

    print(f"The total score for this set of hands is {score}.")
    # phew! it works!


def solve_part_2(raw_data):
    """Parse a set of hands, order them correctly by more difficult rules, and find the new score."""
    all_hands = []
    for line in raw_data:
        cards, bid = line.split(" ")
        line = Hand2(cards, int(bid))
        all_hands.append(line)

    ordered_hands = sorted(all_hands)
    # print(ordered_hands)
    score = 0
    for index, hand in enumerate(ordered_hands):
        # print(index, hand)
        score += ((index + 1) * hand.bid)

    print(f"The new, wildcard-containing score for this set of hands is {score}.")
    # Success again!


def solution(filename):
    """Briefly describe the puzzle here."""
    # process data from filename to make it usable by our solving functions
    raw_data = fetch_string_data(filename)
    processed_data = parse(raw_data)

    solve_part_1(processed_data)
    solve_part_2(raw_data)


# This can be run as a script from the command line, with data filename as argument.
if __name__ == "__main__":
    import sys

    try:
        arg = sys.argv[1]
    except IndexError:
        # arg = "testing.txt"
        arg = "../data/day_07_input.txt"
        # arg = "../data/day_07_testing.txt"

    print(f"Data file = '{arg}'.")  # debug
    solution(arg)
