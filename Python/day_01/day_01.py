from pathlib import Path
import json

INPUT_FILEPATH = Path("input.txt")
PATTERNS_FILEPATH = Path("patterns.json")


def read_patterns_from(filepath: Path, tablename: str) -> dict:
    with open(filepath, "r") as file:
        patterns = json.load(file)
    return patterns[tablename]


def extract_calibration_value_from(text: str, patterns_table: dict) -> int:
    first_digit = search_first_digit(text, patterns_table)
    last_digit = search_last_digit(text, patterns_table)
    return first_digit * 10 + last_digit


def search_first_digit(text: str, patterns_table: dict) -> int:
    first_digit = None
    for i in range(len(text)):
        for pattern, value in patterns_table.items():
            if text[i:].startswith(pattern):
                first_digit = value
                break
        if first_digit:
            break
    return first_digit


def search_last_digit(text: str, patterns_table: dict) -> int:
    last_digit = None
    for i in range(len(text)):
        for pattern, value in patterns_table.items():
            if (i == 0 and text.endswith(pattern)) or text[:-i].endswith(pattern):
                last_digit = value
                break
        if last_digit:
            break
    return last_digit


def extract_sum_of_all_calibration_values_from(
    filepath: Path, patterns_table: dict
) -> int:
    with open(filepath, "r") as file:
        input_lines = file.readlines()

    calibration_values = [
        extract_calibration_value_from(line.strip(), patterns_table)
        for line in input_lines
    ]

    return sum(calibration_values)


if __name__ == "__main__":

    patterns_table = read_patterns_from(PATTERNS_FILEPATH, "part1")
    part1_result = extract_sum_of_all_calibration_values_from(
        INPUT_FILEPATH, patterns_table
    )
    print(f"Part 1: {part1_result}")

    patterns_table = read_patterns_from(PATTERNS_FILEPATH, "part2")
    part2_result = extract_sum_of_all_calibration_values_from(
        INPUT_FILEPATH, patterns_table
    )
    print(f"Part 2: {part2_result}")
