#!/usr/bin/python3
from re import sub

def is_game_possible(game, bag_constraints):
    rounds = [round.strip(" ") for round in game.split(";")]
    for game_round in rounds:
        rgb = {game_data.strip(" ").split(" ")[1]: int(game_data.strip(" ").split(" ")[0]) \
                for game_data in game_round.split(",")}
        for color in ["red", "green", "blue"]:
            if color in rgb.keys() and bag_constraints[color] < rgb[color]:
                return False
    return True

def find_min_necessary(game):
    """
    Determine the minimum number of cubes necessary to result in a given game result.
    """
    rounds = [round.strip(" ") for round in game.split(";")]
    bag_constraints = {"red":0,"green":0,"blue":0}

    for game_round in rounds:
        rgb = {game_data.strip(" ").split(" ")[1]: int(game_data.strip(" ").split(" ")[0]) \
                for game_data in game_round.split(",")}

        for color in rgb.keys():
            if rgb[color] > bag_constraints[color]:
                bag_constraints[color] = rgb[color]
    return bag_constraints

def power_of_game(game_data):
    product = 1
    minimum_bag = find_min_necessary(game_data)

    for key in minimum_bag.keys():
        product *= minimum_bag[key]
    return product

def sum_of_power_of_games(game_list):
    sum_result = 0
    for game in game_list:
        [game_number, rounds] = [data.strip(" ") for data in game.split(":")]
        game_number = int(sub("Game ", "",game_number))
        sum_result += power_of_game(rounds)
    return sum_result

test_game = [game for game in """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".splitlines() if len(game)>0]

def tests():
    test_round = "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    test_result = find_min_necessary(test_round)
    assert test_result['red']==4 and test_result['blue']==6 and test_result['green']==2
    assert power_of_game(test_round)==48

    assert sum_of_power_of_games(test_game) == 2286
    
    return "====================\nTests Pass!\n====================\n"
    

if __name__=="__main__":
    print(tests())
    
    f= open("input_files/d02-1.txt","r")
    games = [game.rstrip("\n") for game in f.readlines() if "Game" in game]
    f.close()
    
    print(f'Sum of possible games: {sum_of_power_of_games(games)}.')
