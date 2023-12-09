#!/usr/bin/python3

from re import sub

def partition_data(input_datastr):
    input_data = [sub(r"\s", "", line) for line in input_datastr.splitlines() if len(line)>0]
    result = None

    if "Time" in input_data[0] and "Distance" in input_data[1]:
        """
        times = [int(item) for item in findall(r"\d+", input_data[0])]
        distances = [int(item) for item in findall(r"\d+", input_data[1])]
        """
        result = [(int(input_data[0].split(":")[1]), int(input_data[1].split(":")[1]))]
    return result

def calculate_distance(button_hold_ms, total_time):
    travel_time = total_time - button_hold_ms
    return button_hold_ms * travel_time

def count_record_setters(time, distance):
    return len([calculate_distance(i,time) for i in range(0, time + 1) if calculate_distance(i,time)>distance])

def calculate_product(input_datastr):
    parsed_data = partition_data(input_datastr)
    
    product = 1
    
    for (time,distance) in parsed_data:
        product *= count_record_setters(time,distance)
    return product


test_data = """
Time:      7  15   30
Distance:  9  40  200
"""
def tests():
    assert partition_data(test_data)[0]==(71530,940200)

    assert calculate_distance(2,7)==10
    
    assert count_record_setters(7,9) == 4
    
    assert calculate_product(test_data)==71503
    return "====================\nTests Pass!\n====================\n"
    

if __name__=="__main__":
    print(tests())

    
    f = open("input_files/d06-1.txt","r")
    input_data = f.read() 
    f.close()
    
    print(f'Product of winning methods: {calculate_product(input_data)}.')
