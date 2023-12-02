import os.path
from operator import itemgetter
import re

data_input = []

number_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def replace_strings_with_digits(data):
    matches = []

    last_found_number = re.match(".+([0-9])[^0-9]*$", data)

    if str(data).find("one") != -1:
        for m in re.finditer("one", data):
            matches.append([m.start(), "one"])

    if str(data).find("two") != -1:
        for m in re.finditer("two", data):
            matches.append([m.start(), "two"])

    if str(data).find("three") != -1:
        for m in re.finditer("three", data):
            matches.append([m.start(), "three"])

    if str(data).find("four") != -1:
        for m in re.finditer("four", data):
            matches.append([m.start(), "four"])

    if str(data).find("five") != -1:
        for m in re.finditer("five", data):
            matches.append([m.start(), "five"])

    if str(data).find("six") != -1:
        for m in re.finditer("six", data):
            matches.append([m.start(), "six"])

    if str(data).find("seven") != -1:
        for m in re.finditer("seven", data):
            matches.append([m.start(), "seven"])

    if str(data).find("eight") != -1:
        for m in re.finditer("eight", data):
            matches.append([m.start(), "eight"])

    if str(data).find("nine") != -1:
        for m in re.finditer("nine", data):
            matches.append([m.start(), "nine"])
    # print(data)
    # print(matches)
    matches = sorted(matches, key=itemgetter(0))

    if len(matches) > 2:
        del matches[1:len(matches) - 1]

    print(matches)

    for match_item in matches:
        if last_found_number and last_found_number.start(1) > int(match_item[0]):
            data = str(data).replace(match_item[1], str(number_dict[match_item[1]]))

    return data


def find_sum_calibration_data(data):
    """
    >>> find_sum_calibration_data(["1abc2",
    ... "pqr3stu8vwx",
    ... "a1b2c3d4e5f",
    ... "treb7uchet"])
    142
    """

    count = 0
    edited_data = data

    for item in edited_data:
        cleaned_data = ''.join(filter(str.isdigit, item))
        if len(cleaned_data) == 2:
            count += int(cleaned_data)
        elif len(cleaned_data) == 1:
            count += int(cleaned_data + cleaned_data)
        elif cleaned_data:
            count += int(cleaned_data[0] + cleaned_data[-1])

    return count


def find_sum_calibration_data_with_text(data):
    """
    >>> find_sum_calibration_data_with_text(["two1nine",
    ... "eightwothree",
    ... "abcone2threexyz",
    ... "xtwone3four",
    ... "4nineeightseven2",
    ... "zoneight234",
    ... "7pqrstsixteen",
    ... "fivefivethree75two7three",
    ... "zrxprsixfiveone8bvbdmxjzbmthree",
    ... "three1kxqr21ninemhrmheightwoc",
    ... "stbqnrhdqnjcvjgthtmht8xndfgprq3eightwol"])
    517
    """

    count = 0
    edited_data = data

    for item in edited_data:
        print("Orig: " + item)
        item = replace_strings_with_digits(item)
        print("Edit: " + item)
        cleaned_data = ''.join(filter(str.isdigit, item))
        print("Cleared: " + cleaned_data)
        print("––––––")
        if len(cleaned_data) == 2:
            count += int(cleaned_data)
        elif len(cleaned_data) == 1:
            count += int(cleaned_data + cleaned_data)
        elif len(cleaned_data) != 0:
            count += int(cleaned_data[0] + cleaned_data[-1])

    return count


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'day01.txt')) as fh:
        for line in fh.readlines():
            line = line.strip()
            data_input.append(line)

    print("Sum of all calibration numbers: " + str(find_sum_calibration_data(data_input)))
    print("Sum of all calibration numbers inc. text digits: " + str(find_sum_calibration_data_with_text(["stbqnrhdqnjcvjgthtmht8xndfgprq3eightwol"])))
