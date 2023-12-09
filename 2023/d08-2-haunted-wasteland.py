#!/usr/bin/python3

from re import match,sub
from math import lcm

def parse_input(input_datastr):
    input_data = [sub(r"[\(\) ]", r"", line) for line in input_datastr.splitlines() if len(line)>0]
    
    directions = []
    for line in input_data[1:]:
        direction_key = line.split("=")[0]
        direction_value = tuple(line.split("=")[1].split(","))
        directions += [(direction_key, direction_value)]
    result = (input_data[0], directions)
    return result
        
def get_next_map_step(path_char, current_spot, directions):
        current_direction = [d for d in directions if d[0]==current_spot][0]
        if path_char == "L":
            return current_direction[1][0]
        if path_char == "R":
            return current_direction[1][1]


def follow_map(input_mapstr, start_string, end_string):
    (path, directions) = parse_input(input_mapstr)
    
    current_spot = start_string
    i = 0

    while True:
        if match(f"^.*{end_string}$", current_spot):
            return i
        char = path[i%len(path)]
        i+= 1
        current_spot = get_next_map_step(char, current_spot, directions)


def follow_map_as_ghost(input_mapstr):
    (path, directions) = parse_input(input_mapstr)
    i = 0
    ghosts = [d[0] for d in directions if d[0][-1]=="A"]
    
    distances = [follow_map(input_mapstr, ghost,"Z") for ghost in ghosts]
    
    total = distances[0]
    for d in distances[1:]:
        total = lcm(total, d)
    return total

    """ 
    while True:
        char = path[i%len(path)]
        print(f"Current Ghosts: {ghosts}")
        if len([ghost for ghost in ghosts if match(f'^.*Z$',ghost)]) == len(ghosts):
            return i
        i+=1
        for j in range(len(ghosts)):
            ghosts[j] = get_next_map_step(char, ghosts[j], directions)
    """

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

test_data_3 = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""
def tests():
    assert parse_input(test_data)[0] == "RL"
    assert parse_input(test_data)[1][0][1]==("BBB","CCC")
    assert parse_input(test_data)[1][0][0]=="AAA"
    assert parse_input(test_data)[1][-1] == ( "ZZZ", ("ZZZ","ZZZ"))

    assert follow_map(test_data,"AAA","ZZZ") == 2
    assert follow_map(test_data_2, "AAA", "ZZZ") == 6

    assert follow_map_as_ghost(test_data_3) == 6

    return "====================\nTests Pass!\n====================\n"
    

if __name__=="__main__":
    print(tests())

    f = open("input_files/d08-1.txt","r")
    input_datastr = f.read() 
    f.close()
    
    
    
    print(f'Total Distance: {follow_map_as_ghost(input_datastr)}.')
