import os.path
import re

data_input = []

max_red = 12
max_green = 13
max_blue = 14


def find_possible_games(data):
    """
    >>> find_possible_games(["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    ... "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    ... "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    ... "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    ... "Game 5: 10 red, 1 blue, 3 green; 2 blue, 10 red, 2 green"])
    8
    """

    count = 0
    edited_data = data

    for item in edited_data:
        game_possible = True
        game = item.split(": ")
        game[0] = ''.join(filter(str.isdigit, game[0]))
        game[1] = game[1].split("; ")
        # print(item)

        for game_throw in game[1]:
            count_throw_red = 0
            count_throw_green = 0
            count_throw_blue = 0

            # How expensive is creating a list in a list in a list? :thinking_face: I know regex might be better here
            game_throw = game_throw.split(", ")

            for single_cubes_throw in game_throw:
                if str(single_cubes_throw).find("red") != -1:
                    count_throw_red += int(''.join(filter(str.isdigit, single_cubes_throw)))
                elif str(single_cubes_throw).find("green") != -1:
                    count_throw_green += int(''.join(filter(str.isdigit, single_cubes_throw)))
                elif str(single_cubes_throw).find("blue") != -1:
                    count_throw_blue += int(''.join(filter(str.isdigit, single_cubes_throw)))

            if not (count_throw_red <= max_red and count_throw_green <= max_green and count_throw_blue <= max_blue):
                game_possible = False

        if game_possible:
            count += int(game[0])

    return count


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'day02.txt')) as fh:
        for line in fh.readlines():
            line = line.strip()
            data_input.append(line)

    print("Sum of all IDs of possible games: " + str(find_possible_games(data_input)))
