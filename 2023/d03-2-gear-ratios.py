#!/usr/bin/python3
from re import sub, finditer

def find_adjacent_symbols(schematic, row, start_index, end_index):
    adj_symbols = []
    
    expand_up = True if row > 0 else False
    expand_down = True if row < len(schematic) - 2 else False
    expand_left = True if start_index > 0 else False
    expand_right = True if end_index < len(schematic[row]) - 1 else False
    
    if expand_up and expand_left: adj_symbols += [(schematic[row - 1][start_index - 1],row - 1, start_index - 1)]
    if expand_up and expand_right: adj_symbols += [(schematic[row - 1][end_index + 1],row - 1, end_index + 1)]
    if expand_down and expand_left: adj_symbols += [(schematic[row + 1][start_index - 1],row+1, start_index - 1)]
    if expand_down and expand_right: adj_symbols += [(schematic[row + 1][end_index + 1], row + 1, end_index + 1)]
    if expand_left: adj_symbols += [(schematic[row][start_index - 1], row, start_index - 1)]
    if expand_right: adj_symbols += [(schematic[row][end_index + 1],row ,end_index + 1 )]
    if expand_up: 
        for i in range(start_index,end_index + 1):
            adj_symbols += [(schematic[row - 1][i], row - 1, i)]
    if expand_down:
        for i in range(start_index,end_index + 1):
            adj_symbols += [(schematic[row + 1][i], row + 1, i)]

    return adj_symbols

def find_matching_symbols(schematic, row, start_index, end_index, symbol):
    adj_chars = find_adjacent_symbols(schematic, row, start_index, end_index)
    return [match for match in adj_chars if match[0]==symbol]
    

def find_numbers_with_symbol(schematic, symbol):
    """
    Finds all numbers in a schematic string. Returns a list of tuples:
        (number, row, start_index, end_index, matching_symbols)
    """
    result = []

    for i in range(0,len(schematic)):
        row_string = schematic[i]
        matches = [(item.group(), item.span()[0],item.span()[1] - 1) \
                for item in list(finditer(r"\d+",row_string))]


        result += [(int(item[0]), i, item[1], item[2], \
                find_matching_symbols(schematic, i, item[1], item[2], symbol) ) \
                for item in matches]
        # Include only results with positive matches for the symbol:
        result = [item for item in result if len(item[-1]) > 0]
    return result

def find_sum_of_adjacent_products(schematic,symbol):
    total = 0
    matches = find_numbers_with_symbol(schematic,symbol)

    for i in range(0,len(matches) - 1):
        for j in range(i + 1,len(matches)):
            matching_set = list(set(matches[i][-1] + matches[j][-1]))
            for item in matching_set:
                if item in matches[i][-1] and item in matches[j][-1]:
                    total += matches[i][0] * matches[j][0]
    return total


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

    test_str_1 = [item[0] for item in find_adjacent_symbols(test_data, 0, 0, 2)]
    assert test_str_1.count(".") == 4 and test_str_1.count("*")==1

    test_str_2 = [item[0] for item in find_adjacent_symbols(test_data,2,6,8)]
    assert test_str_2.count(".")==8 and test_str_2.count("#")==1

    test_str_3 = [item[0] for item in find_adjacent_symbols(test_data,9,5,7)]
    assert test_str_3.count(".")==6 and test_str_3.count("*")==1

    assert len(find_matching_symbols(test_data,0,0,2,"*")) == 1
    
    assert (467, 0, 0, 2, [('*', 1, 3)]) in find_numbers_with_symbol(test_data, "*")

    assert find_sum_of_adjacent_products(test_data, "*") == 467835
    
    return "====================\nTests Pass!\n====================\n"
    

if __name__=="__main__":
    print(tests())
    f= open("input_files/d03-1.txt","r")
    schematic = [line.rstrip("\n") for line in f.readlines() if len(line) > 0]
    f.close()

    print(f'Sum of gear ratios: {find_sum_of_adjacent_products(schematic, "*")}')
