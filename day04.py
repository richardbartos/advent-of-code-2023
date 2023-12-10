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

def eval_scratchcards_star2(data):
    """
    >>> eval_scratchcards_star2(["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    ... "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    ... "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    ... "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    ... "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    ... "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"])
    30
    """

    total_scratchcards = 0
    edited_data = data
    card_multiply = [0] * 198
    index = 0

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

        for x in range(card_multiply[index]):
            for y in range(x):
                card_multiply[index + y + 1] += 1

        if card_matches > 0:
            card_multiply[index] += 1
            for y in range(card_matches):
                card_multiply[index + y + 1] += 1

        print(card_multiply)

        # if card_matches > 0:
        #    print("End od card. " + str(card_matches) + " matches. | " + str(2 ** (card_matches - 1)) + " points added. Total points: " + str(points_total))
        # else:
        #    print("End od card. " + str(card_matches) + " matches. | 0 points added. Total points: " + str(points_total))

        index += 1

    return sum(card_multiply)


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'day04.txt')) as fh:
        for line in fh.readlines():
            line = line.strip()
            data_input.append(line)

    print("Total points: " + str(eval_scratchcards(data_input)))
