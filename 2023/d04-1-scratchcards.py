#!/usr/bin/python3
from re import sub,findall

def check_card(card):
    (number, game) = card.split(":")
    number = int(sub("Card ", "", number))
    (winners, results) = [item.strip(" ") for item in  game.split("|")]
    winners = [int(item) for item in findall(r'\d+',winners)]
    results = [int(item) for item in findall(r'\d+',results)]

    score = 0
    for winning_number in winners:
        if winning_number in results:
            score += results.count(winning_number)
    score = pow(2, score - 1) if score >0 else 0
    return score

def sum_all_cards(cards):
    result = 0
    for card in cards:
        result += check_card(card)
    return result


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
    assert check_card(sample_data[0]) == 8

    assert sum_all_cards(sample_data) == 13
    return "====================\nTests Pass!\n====================\n"
    

if __name__=="__main__":
    print(tests())

    f = open("input_files/d04-1.txt","r")
    input_data = [line.rstrip("\n") for line in f.readlines() if "Card" in line]
    f.close()
    
    print(f'Total score of sample: {sum_all_cards(input_data)}.')
