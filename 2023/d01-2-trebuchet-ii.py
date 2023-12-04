#!/usr/bin/python3

from re import sub

def get_value(input_str):
    """
    returns the calibration value:
    The calibration value can be found by combining the first digit and the last digit 
        (in that order) to form a single two-digit number.

    Note: words that are spelled out (ie: 'one') count as well.
    """
    digits = input_str
    subs = {'one': "1", 'two': "2", 'three': '3', 'four': '4', \
            'five': '5', 'six': '6', 'seven': '7', 'eight':'8', 'nine':'9'}
    for sub_key in subs.keys():
        digits = sub(sub_key, f'{sub_key}{subs[sub_key]}{sub_key}', digits)
    digits = sub(r'[^\d]', '', digits)

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
    assert get_value('two1nine') ==29
    assert sum_values(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]) == 142
    assert sum_values(['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen'])==281

    return "====================\nTests Pass!\n====================\n"
    

if __name__=="__main__":
    print(tests())
    
    f = open("input_files/d01-1.txt","r")
    input_strings = [string.rstrip("\n") for string in f.readlines()]
    f.close()

    total = sum_values(input_strings)
    print(f'Sum of calibration values: {total}')
