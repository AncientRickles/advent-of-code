#!/usr/bin/python3
from re import sub, finditer

def find_adjacent_symbols(schematic, row, start_index, end_index):
    output_str = ""
    
    expand_up = True if row > 0 else False
    expand_down = True if row < len(schematic) - 2 else False
    expand_left = True if start_index > 0 else False
    expand_right = True if end_index < len(schematic[row]) - 1 else False
    
    if expand_up and expand_left: output_str += schematic[row - 1][start_index - 1]
    if expand_up: output_str += schematic[row - 1][start_index:end_index + 1]
    if expand_up and expand_right: output_str += schematic[row - 1][end_index + 1]
    if expand_left: output_str += schematic[row][start_index - 1]
    if expand_right: output_str += schematic[row][end_index + 1]
    if expand_down and expand_left: output_str += schematic[row + 1][start_index - 1]
    if expand_down: output_str += schematic[row + 1][start_index:end_index + 1]
    if expand_down and expand_right: output_str += schematic[row + 1][end_index + 1]

    return output_str

def is_adjacent_to_symbol(schematic, row, start_index, end_index):
    test_str = find_adjacent_symbols(schematic, row, start_index, end_index)

    test_str_symbols = sub(r"[\d\.]","",test_str)

    return True if len(test_str_symbols) > 0 else False


def find_all_numbers(schematic):
    """
    Finds all numbers in a schematic string. Returns a list of tuples:
        (number, row, start_index, end_index, is_adjacent)
    """
    result = []

    for i in range(0,len(schematic)):
        row_string = schematic[i]
        matches = [(item.group(), item.span()[0],item.span()[1] - 1) \
                for item in list(finditer(r"\d+",row_string))]


        result += [(int(item[0]), i, item[1], item[2], \
                is_adjacent_to_symbol(schematic, i, item[1], item[2]) ) \
                for item in matches]
    return result

def generate_serial(schematic):
    results = find_all_numbers(schematic)
    
    sum = 0
    for result in results:
        if result[4]==True:
            sum += result[0]
    return sum

test_schematic = """
467..114.
...*.....
..35..633
......#..
617*.....
.....+.58
..592....
......755
...$.*...
.664.598.
"""


def tests():
    test_data = [line for line in test_schematic.split("\n") if len(line)>0]

    test_str_1 = find_adjacent_symbols(test_data, 0, 0, 2) 
    assert test_str_1.count(".") == 4 and test_str_1.count("*")==1

    test_str_2 = find_adjacent_symbols(test_data,2,6,8)
    assert test_str_2.count(".")==8 and test_str_2.count("#")==1

    test_str_3 = find_adjacent_symbols(test_data,9,5,7)
    assert test_str_3.count(".")==6 and test_str_3.count("*")==1

    
    assert is_adjacent_to_symbol(test_data, 0, 0, 2) == True
    assert is_adjacent_to_symbol(test_data, 5, 7, 8) == False

    assert (467, 0, 0, 2, True) in find_all_numbers(test_data)

    assert generate_serial(test_data) == 4361  

    return "====================\nTests Pass!\n====================\n"
    

if __name__=="__main__":
    print(tests())
    
    f= open("input_files/d03-1.txt","r")
    schematic = [line.rstrip("\n") for line in f.readlines() if len(line) > 0]
    f.close()

    print(f'Serial Number for Engine: {generate_serial(schematic)}')
