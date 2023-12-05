import os.path
import re

data_input = []


def eval_scratchcards(data):
    """
    >>> eval_scratchcards(["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    ... "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    ... "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    ... "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    ... "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    ... "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ... "Card 7: 31 18 13 56 72 22 10 11 12 | 31 18 13 56 72 22 10 11 12"])
    85
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
            if re.findall(str(winning_number) + " ", " ".join(game[1]) + " "):
                card_matches += 1

        if card_matches > 0:
            points_total += 2 ** (card_matches - 1)

        if card_matches > 0:
            print("End od card. " + str(card_matches) + " matches. | " + str(2 ** (card_matches - 1)) + " points added. Total points: " + str(points_total))
        else:
            print("End od card. " + str(card_matches) + " matches. | 0 points added. Total points: " + str(points_total))

    return points_total


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'day04.txt')) as fh:
        for line in fh.readlines():
            line = line.strip()
            data_input.append(line)

    print("Total points: " + str(eval_scratchcards(data_input)))
