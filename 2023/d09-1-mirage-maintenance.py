#!/usr/bin/python3

from re import findall

def parse_input(input_datastr):
    input_datastrs = [list(findall(r"[-\d]+", line.rstrip("\n"))) for line in input_datastr.splitlines() if len(line)>0]

    input_data = []
    for input_line in input_datastrs:
        input_data += [ [int(num) for num in input_line] ] 
    return input_data

def find_prior_value(dataline):
    data_array = [dataline]

    while len([item for item in data_array[-1] if item != 0])>0:
        current_line = data_array[-1]
        next_line = []
        for i in range(len(current_line) - 1):
            next_line += [current_line[i + 1] - current_line[i]]
        if len(next_line)>0:
            data_array += [next_line]
        else:
            data_array += [[0]]

    reversed_array = [data_array[i] for i in range(len(data_array)-1,-1,-1)]
    result = 0

    for i in range(len(reversed_array) - 1):
        result += reversed_array[i+1][0]
    return result


test_data = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

def tests():
    parsed_data = parse_input(test_data)

    assert parsed_data[0][0]==0
    assert parsed_data[-1][-1]==45

    assert find_prior_value(parsed_data[-1]) ==5

    results = [find_prior_value(line) for line in parsed_data]
    assert sum(results) == 2
    return "====================\nTests Pass!\n====================\n"
    

if __name__=="__main__":
    print(tests())
    
    with open("input_files/d09-1.txt","r") as f:
        input_datastr = f.read()

    results = [find_next_value(line) for line in parse_input(input_datastr)]
    

    print(f"Sum of predicted values: {sum(results)}")
