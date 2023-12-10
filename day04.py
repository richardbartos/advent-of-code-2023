import os.path
import re

data_input = []


def eval_scratchcards(data):
    """
    >>> eval_scratchcards(["Card   4: 62 21 85 90 64 44 29  2 86 84 | 98 21 82 55 62 14  3 33  7 90 85 57 94 44 64  5 43 91 96 67 84 78 69 81 29",
    ... "Card   2: 17  9  7 91 32 97 76 39 83 88 | 88 25 46 50 91 18 39 76 17 22 28 82 44 66 52  7 11 56 77  9 40 83 97 32 47"])
    640
    """

    points_total = 0
    edited_data = data

    for item in edited_data:
        card_matches = 0
        game = re.sub(r'^.*?:', '', item)
        game = game.split("|")
        game[0] = game[0].split(" ")
        game[1] = game[1].split(" ")
        while "" in game[0]:
            game[0].remove("")
        while "" in game[1]:
            game[1].remove("")

        for winning_number in game[0]:
            # How did we get here? :upside_down_smile:
            if re.findall(" " + str(winning_number) + " ", " " + " ".join(game[1]) + " "):
                # print("Matched: " + str(winning_number))
                card_matches += 1

        if card_matches > 0:
            points_total += 2 ** (card_matches - 1)

        # if card_matches > 0:
        #    print("End od card. " + str(card_matches) + " matches. | " + str(2 ** (card_matches - 1)) + " points added. Total points: " + str(points_total))
        # else:
        #    print("End od card. " + str(card_matches) + " matches. | 0 points added. Total points: " + str(points_total))

    return points_total


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'day04.txt')) as fh:
        for line in fh.readlines():
            line = line.strip()
            data_input.append(line)

    print("Total points: " + str(eval_scratchcards(data_input)))
