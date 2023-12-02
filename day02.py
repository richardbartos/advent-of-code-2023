import os.path
import re

data_input = []

max_red = 12
max_green = 13
max_blue = 14


def find_possible_games(data):
    """
    >>> find_possible_games(["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    ... "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    ... "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    ... "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"])
    8
    """

    count = 0
    edited_data = data

    for item in edited_data:
        match = re.search(r, item)
        print(match)

    return count


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'day02.txt')) as fh:
        for line in fh.readlines():
            line = line.strip()
            data_input.append(line)

    print("Sum of all calibration numbers: " + str(find_possible_games(data_input)))
