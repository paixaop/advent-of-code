import re
from collections import Counter
from functools import reduce, cmp_to_key


card_values = {
    'A': 14,
    'K': 13, 
    'Q': 12, 
    'J': 11, 
    'T': 10, 
    '9': 9,
    '8': 8, 
    '7': 7, 
    '6': 6, 
    '5': 5, 
    '4': 4, 
    '3': 3,
    '2': 2
}

card_values_joker = {
    'A': 14,
    'K': 13, 
    'Q': 12, 
    'J': 1, 
    'T': 10, 
    '9': 9,
    '8': 8, 
    '7': 7, 
    '6': 6, 
    '5': 5, 
    '4': 4, 
    '3': 3,
    '2': 2
}

def hand_type(hand):
    if hand == [5]:
        # Five of a Kind
        return 7
    if hand == [4, 1]:
        # Four of a Kind
        return 6
    if hand == [3, 2]:
        # Full House
        return 5
    if hand == [3, 1, 1]:
        # Three of a Kind
        return 4
    if hand == [2, 2, 1]:
        # Two Pair 
        return 3
    if hand == [2, 1, 1, 1]:
        # One Pair
        return 2
    # High Card
    return 1


def rank_hand(cards):
    counts = Counter(cards)
    t = list(counts.values())
    t.sort(reverse=True)        
    return hand_type(t)


def parse(data):
    data = data.split("\n")
    hands = []
    for line in data:
        cards, bid = line.split()
        bid = int(bid)
        cards = list(cards)
        score = rank_hand(cards)
        
        hands.append({
            "cards": cards,
            "bid": bid,
            "score": score
        })

    return hands


def compare(hand1, hand2):
    if hand1['score'] > hand2['score']:
        return 1
    if hand1['score'] == hand2['score']:
        for i, card1 in enumerate(hand1['cards']):
            if card1 != hand2['cards'][i]:   
                card2 = hand2['cards'][i] 
                if  card_values[card1] > card_values[card2]:
                    return 1
                else:
                    return -1
        return 0
    return -1
     
def compare_joker(hand1, hand2):
    if hand1['score'] > hand2['score']:
        return 1
    if hand1['score'] == hand2['score']:
        for i, card1 in enumerate(hand1['cards']):
            if card1 != hand2['cards'][i]:   
                card2 = hand2['cards'][i] 
                if  card_values_joker[card1] > card_values_joker[card2]:
                    return 1
                else:
                    return -1
        return 0
    return -1

def part_a(data):
    data = parse(data)

    rank = sorted(data, key = cmp_to_key(compare))
    total = 0
    for i, r in enumerate(rank):
        total += (i+1) * r['bid']

    return total

def replace_joker(cards, new_card):
    l = [new_card if c =='J' else c for c in cards]
    score = rank_hand(l)
    return l, score

def card_replace(cards):
    score = rank_hand(cards)
    new_hands = []
    for card in card_values_joker.keys():
        temp, stemp = replace_joker(cards[0:], card)    
        new_hands.append({
            "cards": temp,
            "score": stemp
        })

    new_hands = sorted(new_hands, key=cmp_to_key(compare_joker))
    if new_hands:
        return new_hands[-1]
    return {
        'cards': cards,
        'score': score
    }
        

def part_b(data):
    data = parse(data)

    # check if there's a joker
    for i, hand in enumerate(data):
        if 'J' in hand['cards']:
            new_hand = card_replace(hand['cards'])
            data[i]['new_cards'] = new_hand['cards']
            data[i]['score'] = new_hand['score']

    rank = sorted(data, key = cmp_to_key(compare_joker))
    total = 0
    for i, r in enumerate(rank):
        total += (i+1) * r['bid']

    return total

test_data_part_a = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

test_data_part_b = test_data_part_a

if __name__ == "__main__":
    from mysolutions import common
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 6440)
    common.run(part_b, test_data_part_b, data, 5905)