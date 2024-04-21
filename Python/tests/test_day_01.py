from day_01 import extract_calibration_value_from

DATA_TEST = {
    "part1": {"1abc2": 12, "pqr3stu8vwx": 38, "a1b2c3d4e5f": 15, "treb7uchet": 77},
    "part2": {
        "two1nine": 29,
        "eightwothree": 83,
        "abcone2threexyz": 13,
        "xtwone3four": 24,
        "4nineeightseven2": 42,
        "zoneight234": 14,
        "7pqrstsixteen": 76,
    },
}

PATTERNS_TABLE = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def test_extract_calibration_value_from_text_with_digit():
    for text, expected in DATA_TEST["part1"].items():
        assert extract_calibration_value_from(text, PATTERNS_TABLE) == expected


def test_extract_calibration_value_from_text_with_written_number():
    for text, expected in DATA_TEST["part2"].items():
        assert extract_calibration_value_from(text, PATTERNS_TABLE) == expected
