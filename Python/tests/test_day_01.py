from day_01 import extract_calibration_value_from

EXAMPLE1 = "1abc2"
EXAMPLE2 = "pqr3stu8vwx"
EXAMPLE3 = "a1b2c3d4e5f"
EXAMPLE4 = "treb7uchet"

def test_number_in_example1_is_12():
    assert extract_calibration_value_from(EXAMPLE1) == 12

def test_number_in_example2_is_38():
    assert extract_calibration_value_from(EXAMPLE2) == 38

def test_number_in_example3_is_15():
    assert extract_calibration_value_from(EXAMPLE3) == 15

def test_number_in_example4_is_77():
    assert extract_calibration_value_from(EXAMPLE4) == 77