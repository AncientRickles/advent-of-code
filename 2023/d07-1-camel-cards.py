#!/usr/bin/python3

def parse_input(input_datastr):
    input_data = [item for item in input_datastr.splitlines() if len(item)>0]
    
    return [(item.split(" ")[0], int(item.split(" ")[1])) for item in input_data]

def check_hand_strength(hand):
    card_set = list(set(hand))
    hand_info = sorted([(card, hand.count(card)) for card in card_set], key=lambda card: card[1], reverse=True)


    if len(card_set)==1:
        return 0
    if len(card_set)==2 and hand_info[0][1]==4:
        return 1
    if len(card_set)==2 and hand_info[1][1]==2:
        return 2
    if hand_info[0][1]==3:
        return 3
    if hand_info[0][1]==2 and hand_info[1][1] == 2:
        return 4
    if hand_info[0][1] ==2:
        return 5
    return 6



def rank_sorter(hand):
    result = [check_hand_strength(hand)]
    for card in hand:
        ranks = "AKQJT98765432"
        result += [ranks.index(card)]
    return result

def get_hand_rank(hand, hands):
    sorted_hands = sorted(hands, key=rank_sorter, reverse=True)
    return sorted_hands.index(hand) + 1

def score_hands(input_datastr):
    hands = parse_input(input_datastr)
    result = 0
    for (hand,wager) in hands:
        rank = get_hand_rank(hand, [cards[0] for cards in hands])
        result += rank * wager
    return result
        

test_data = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""
def tests():
    hands = parse_input(test_data)
    assert hands[0][0] == "32T3K"
    assert hands[-1][1] == 483

    assert check_hand_strength("AAAAA") == 0
    assert check_hand_strength("AAAAK") == 1
    assert check_hand_strength("AAAKK") == 2

    assert check_hand_strength("AAAKQ") == 3
    assert check_hand_strength("AAKKQ") == 4
    assert check_hand_strength("AAKQJ") == 5
    assert check_hand_strength("AQT98") == 6

    assert rank_sorter("AAAKQ") == [3,0,0,0,1,2]
    assert sorted([[1,1],[0,1],[0,2]]) ==[[0,1],[0,2],[1,1]]
    
    assert get_hand_rank("QQQJA", [card[0] for card in hands])== 5
    assert get_hand_rank("32T3K", [card[0] for card in hands])== 1

    assert score_hands(test_data) == 6440

    return "====================\nTests Pass!\n====================\n"
    

if __name__=="__main__":
    print(tests())

    f = open("input_files/d07-1.txt","r")
    input_datastr = f.read() 
    f.close()
    

    print(f'Total Score: {score_hands(input_datastr)}.')
