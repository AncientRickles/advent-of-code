#!/usr/bin/python3

def partition_data(input_data):
    data_partition = []
    
    while len(input_data) > 0:
        for i in range(1,len(input_data)):
            if "map" in input_data[i]:
                data_partition += [input_data[0:i - 1]]
                input_data = input_data[i:]
                break
            elif i == len(input_data) - 1:
                data_partition += [input_data]
                input_data = []
    for i in range(0,len(data_partition)):
        data_partition[i] = [item for item in data_partition[i] if len(item) >0]
    (seed_data, unprocessed_mappings) = (data_partition[0][0], data_partition[1:])
    
    seed_data = [int(item) for item in seed_data.split(":")[1].split(" ") if len(item) >0]
    
    result_mappings = []
    for mapping in unprocessed_mappings:
        if "map" in mapping[0]:
            mapping_info = mapping[0].split(" ")[0]
            (map_from, map_to) = (mapping_info.split("-")[0], mapping_info.split("-")[2])
        mappings = [item.split(' ') for item in mapping[1:]]
        for i in range(0,len(mappings)): 
            mappings[i] = [int(item) for item in mappings[i]]
        result_mappings += [(map_from, map_to, sorted(mappings, key=lambda x: x[1]))]
    
    return (seed_data, result_mappings)

def map_input(map_function, input_value):
    for mapping in map_function[-1]:
        if input_value >= mapping[1] and input_value < mapping[1] + mapping[2]:
            return (map_function[1], input_value + mapping[0] - mapping[1])
    return (map_function[1], input_value)

def reverse_map_input(map_function, input_value):
    for mapping in map_function[-1]:
        if input_value >= mapping[0] and input_value < mapping[0] + mapping[2]:
            return (map_function[0], input_value - mapping[0] + mapping[1])
    return (map_function[0], input_value)

def follow_mapping(map_functions, input_value):
    map_from = "seed"
    current_value = input_value

    while map_from != "location":
        next_mapping = [item for item in map_functions if f'{map_from}' in item[0]]
        next_mapping = next_mapping[0] if len(next_mapping)>0 else None

        if next_mapping != None:
            (map_from, current_value) = map_input(next_mapping, current_value)
    return current_value

def reverse_follow_mapping(map_functions, input_value):
    map_from = "location"
    current_value = input_value

    while map_from != "seed":
        next_mapping = [item for item in map_functions if f'{map_from}' in item[1]]
        next_mapping = next_mapping[0] if len(next_mapping)>0 else None

        if next_mapping != None:
            (map_from, current_value) = reverse_map_input(next_mapping, current_value)
    return current_value

def find_minimum_location(input_data):
    data_partition = partition_data(input_data)

    location_values = [follow_mapping(data_partition[1], seed) for seed in data_partition[0]]

    return min(location_values)

def is_in_range(number, ranges):
    """
    Determine if a number is present in a set of ranges.
    [(1,5), (7,2)] returns True for 1-5, 7-8, otherwise False
    """
    for single_range in ranges:
        if number >= single_range[0] and number < single_range[0] + single_range[1]:
            return True
    return False

def find_minimum_location_reverse(input_data):
    i = 0
    data_partition = partition_data(input_data)
    seed_info = data_partition[0]
    
    range_builder = seed_info
    seed_ranges = []
    while len(range_builder)>0:
        seed_ranges += [(range_builder[0], range_builder[1])]
        range_builder = range_builder[2:]

    keep_going = True
    while keep_going:
        seed_value = reverse_follow_mapping(data_partition[1], i) 
        if is_in_range(seed_value, seed_ranges):
            return i
        else:
            i+=1


test_data = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
def tests():
    sample_data = [line.rstrip('\n') for line in test_data.splitlines()]
    
    data_partition = partition_data(sample_data)
    
    assert data_partition[0][0]==79
    
    assert map_input(data_partition[1][0], 99)[-1] == 51
    assert map_input(data_partition[1][0], 79)[-1] == 81
    assert map_input(data_partition[1][0], 14)[-1] == 14

    assert reverse_map_input(data_partition[1][0], 51)[-1] == 99
    assert reverse_map_input(data_partition[1][0], 81)[-1] == 79
    
    assert follow_mapping(data_partition[1], 79) ==82
    assert follow_mapping(data_partition[1], 14) ==43

    assert reverse_follow_mapping(data_partition[1], 82) ==79

    assert find_minimum_location(sample_data) == 35
    
    assert is_in_range(8, [(1,5),(7,2)]) == True 
    assert is_in_range(9, [(1,5),(7,2)]) == False

    assert find_minimum_location_reverse(sample_data)==46

    return "====================\nTests Pass!\n====================\n"
    

if __name__=="__main__":
    print(tests())

    
    f = open("input_files/d05-1.txt","r")
    input_data = [line.rstrip("\n") for line in f.readlines() if len(line) > 0]
    f.close()
    
    print(f'Minimum location from dataset: {find_minimum_location_reverse(input_data)}.')
