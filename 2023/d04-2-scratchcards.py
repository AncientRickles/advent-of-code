#!/usr/bin/python3
from re import sub,findall

def count_matches(card):
    (number, game) = card.split(":")
    number = int(sub("Card ", "", number))
    (winners, results) = [item.strip(" ") for item in  game.split("|")]
    winners = [int(item) for item in findall(r'\d+',winners)]
    results = [int(item) for item in findall(r'\d+',results)]

    matches = 0
    for winning_number in winners:
        if winning_number in results:
            matches += results.count(winning_number)
    return matches

def calculate_score(game_data):
    hopper = []

    for i in range(0,len(game_data)):
        game_round = game_data[i]
        hopper += [game_round]
        print(f'adding {game_round} to hopper')

        match_count = count_matches(game_round)
        for j in range(1, match_count + 1):
            if i + j < len(game_data):
                hopper += [game_data[i + j]] * hopper.count(game_round)
                print(f'adding {hopper.count(game_round)} copies of {game_data[i+j]} to hopper.')
    print(f'==========\nTotal Game Score: {len(hopper)}.')
    return len(hopper)
        

sample_card = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""



def tests():
    sample_data = [line.rstrip("\n") for line in sample_card.splitlines() if "Card" in line]

    assert count_matches(sample_data[0]) == 4
    assert len(sample_data) == 6

    assert calculate_score(sample_data) == 30

    return "====================\nTests Pass!\n====================\n"
    

if __name__=="__main__":
    print(tests())
    f = open("input_files/d04-1.txt","r")
    input_data = [line.rstrip("\n") for line in f.readlines() if "Card" in line]
    f.close()
    
    print(f'Total score of sample: {calculate_score(input_data)}.')
