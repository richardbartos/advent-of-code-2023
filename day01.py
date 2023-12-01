import os.path

data_input = []

def find_sum_calibration_data(data):
    """
    >>> find_sum_calibration_data(["1abc2",
    ... "pqr3stu8vwx",
    ... "a1b2c3d4e5f",
    ... "treb7uchet"])
    142
    """

    count = 0

    for item in data:
        cleaned_data = ''.join(filter(str.isdigit, item))
        if len(cleaned_data) == 2:
            count += int(cleaned_data)
        elif len(cleaned_data) == 1:
            count += int(cleaned_data + cleaned_data)
        else:
            count += int(cleaned_data[0] + cleaned_data[-1])

    return count


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'day01.txt')) as fh:
        for line in fh.readlines():
            line = line.strip()
            data_input.append(line)

    print("Sum of all calibration numbers: " + str(find_sum_calibration_data(data_input)))
