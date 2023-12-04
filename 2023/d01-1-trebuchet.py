#!/usr/bin/python3

from re import sub

def get_value(input_str):
    """
    returns the calibration value:
    The calibration value can be found by combining the first digit and the last digit 
        (in that order) to form a single two-digit number.
    """
    digits = sub(r'[^\d]', '', input_str)
    if len(digits) >=1:
        return int(digits[0] + digits[-1])
    else:
        print(f"Error: calibration value not valid. Str: {input_str}.")
        return 0

def sum_values(str_list):
    """
    for strings in the list: calculate the sum of the calibration values.
    """
    total = 0
    for string in str_list:
        total += get_value(string)
    return total

def tests():

    assert get_value("hi1234")==14
    assert sum_values(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]) == 142

    return "====================\nTests Pass!\n====================\n"
    

if __name__=="__main__":
    print(tests())
    
    f = open("input_files/d01-1.txt","r")
    input_strings = [string.rstrip("\n") for string in f.readlines()]
    f.close()

    total = sum_values(input_strings)
    print(f'Sum of calibration values: {total}')
