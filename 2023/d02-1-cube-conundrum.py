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


def sum_of_possible_games(game_list, bag_constraints):
    sum = 0
    for game in game_list:
        [game_number, rounds] = [data.strip(" ") for data in game.split(":")]
        game_number = int(sub("Game ", "",game_number))

        if is_game_possible(rounds, bag_constraints):
            sum += game_number
    return sum

test_game = [game for game in """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".splitlines() if len(game)>0]

def tests():
    bag_constraints = {'red':12, 'green':13, 'blue':14}
    assert sum_of_possible_games(test_game, bag_constraints) == 8

    return "====================\nTests Pass!\n====================\n"
    

if __name__=="__main__":
    print(tests())
    
    f= open("input_files/d02-1.txt","r")
    games = [game.rstrip("\n") for game in f.readlines() if "Game" in game]
    f.close()

    game_sum = sum_of_possible_games(games, {'red':12, 'green':13, 'blue':14})
    print(f'Sum of possible games: {game_sum}.')
