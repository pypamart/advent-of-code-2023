from pathlib import Path

INPUT_FILEPATH = Path("input.txt")


def extract_calibration_value_from(text: str) -> int:
    digits = remove_letters(text)
    first_digit = digits[0]
    last_digit = digits[-1]
    return int(first_digit + last_digit)


def remove_letters(text: str) -> str:
    return "".join([letter for letter in text if letter.isdigit()])


if __name__ == "__main__":

    with open(INPUT_FILEPATH, "r") as file:
        input_lines = file.readlines()

    calibration_values = [
        extract_calibration_value_from(line.strip()) 
        for line in input_lines]
    
    print(sum(calibration_values))

