#!/usr/bin/python3

from re import match,sub

def parse_input(input_datastr):
    input_data = [sub(r"[\(\) ]", r"", line) for line in input_datastr.splitlines() if len(line)>0]
    
    directions = []
    for line in input_data[1:]:
        direction_key = line.split("=")[0]
        direction_value = tuple(line.split("=")[1].split(","))
        directions += [(direction_key, direction_value)]
    result = (input_data[0], directions)
    return result
        
def follow_map(input_mapstr, start_string, end_string, verbose=False):
    (path, directions) = parse_input(input_mapstr)
    work_path = path
    
    current_spot = start_string
    if verbose:(f"Starting spot: {current_spot}")
    i = 0

    while True:
        if len(work_path)==0:
            work_path = path
        if match(f"^.*{end_string}$", current_spot):
            return i
        i+= 1
        char = work_path[0]
        work_path = work_path[1:]

        current_direction = [d for d in directions if d[0]==current_spot][0]
        if char == "L":
            current_spot = current_direction[1][0]
            if verbose: print(f'Going {char} on {current_direction}. New Current Spot: {current_spot}.')
        if char == "R":
            current_spot = current_direction[1][1]
            if verbose: print(f'Going {char} on {current_direction}. New Current Spot: {current_spot}.')



test_data = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

test_data_2 = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""
def tests():
    assert parse_input(test_data)[0] == "RL"
    assert parse_input(test_data)[1][0][1]==("BBB","CCC")
    assert parse_input(test_data)[1][0][0]=="AAA"
    assert parse_input(test_data)[1][-1] == ( "ZZZ", ("ZZZ","ZZZ"))

    assert follow_map(test_data,"AAA","ZZZ") == 2
    assert follow_map(test_data_2, "AAA", "ZZZ") == 6

    return "====================\nTests Pass!\n====================\n"
    

if __name__=="__main__":
    print(tests())

    f = open("input_files/d08-1.txt","r")
    input_datastr = f.read() 
    f.close()
    
    (path, directions) = parse_input(input_datastr)
    
    
    print(f'Total Distance: {follow_map(input_datastr, "AAA", "ZZZ", True)}.')
