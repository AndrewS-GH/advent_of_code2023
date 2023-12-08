from collections import Counter
from functools import cmp_to_key, partial


# Part 1 Structures
order = "AKQJT98765432"
card_strength_p1 = {ch: len(order) - i for i, ch in enumerate(order)}

hand_scores_p1 = [
    (7, lambda hand: all(char == hand[0] for char in hand)),
    (6, lambda hand: 4 in Counter(hand).values()),
    (5, lambda hand: sorted(Counter(hand).values()) == [2, 3]),
    (4, lambda hand: 3 in Counter(hand).values()),
    (3, lambda hand: sorted(Counter(hand).values()) == [1, 2, 2]),
    (2, lambda hand: 2 in Counter(hand).values()),
    (1, lambda hand: len(Counter(hand)) == len(hand)),
]

# Part 2 structures
order = "AKQT98765432J"
card_strength_p2 = {ch: len(order) - i for i, ch in enumerate(order)}

def five_of_kind(hand):
    counter = Counter(hand)
    return len(counter) == 1 or (len(counter) == 2 and 'J' in counter)

def four_of_kind(hand):
    counter = Counter(hand)
    if 'J' not in counter:
        return 4 in counter.values()
    
    nums_js = counter.pop('J')
    return (4 - nums_js) in counter.values()

def full_house(hand):
    counter = Counter(hand)
    if 'J' not in counter:
        return sorted(counter.values()) == [2, 3]
    
    return len(counter) == 3

def three_of_kind(hand):
    counter = Counter(hand)
    if 'J' not in counter:
        return 3 in counter.values()
    
    nums_js = counter.pop('J')
    return (3 - nums_js) in counter.values()

def two_pair(hand):
    counter = Counter(hand)
    if 'J' not in counter:
        return sorted(counter.values()) == [1, 2, 2]
    
    return len(counter) == 4

def one_pair(hand):
    counter = Counter(hand)
    if 'J' not in counter:
        return 2 in counter.values()

    return True

def high_card(hand):
    counter = Counter(hand)
    if 'J' not in counter:
        return len(counter) == len(hand)
    
    counter.pop('J')
    return all(val == 1 for val in counter.values())

hand_scores_p2 = [
    (7, five_of_kind),
    (6, four_of_kind),
    (5, full_house),
    (4, three_of_kind),
    (3, two_pair),
    (2, one_pair),
    (1, high_card),
]


def compare_hands(hand1: tuple[str, int], hand2: tuple[str, int], 
                  hand_scores: list[int, callable], card_strength: dict[str, int]):
    hand1, hand2 = hand1[0], hand2[0]
    
    def get_score(hand):
        for score, func in hand_scores:
            if func(hand):
                return score
        
        return 0
    
    hand1_score, hand2_score = get_score(hand1), get_score(hand2)
    if hand1_score > hand2_score:
        return 1
    elif hand1_score < hand2_score:
        return -1
    
    for h1_ch, h2_ch in zip(hand1, hand2):
        if card_strength[h1_ch] > card_strength[h2_ch]:
            return 1
        elif card_strength[h1_ch] < card_strength[h2_ch]:
            return -1
    
    return 0
    

def main():
    with open('input', 'r') as f:
        lines = [line.strip().split() for line in f]
    
    hands_to_bids = {hand: int(bid) for hand, bid in lines}

    # Part 1
    comp_hands = partial(compare_hands, hand_scores=hand_scores_p1, card_strength=card_strength_p1)
    sorted_hand_to_bids = dict(sorted(hands_to_bids.items(), key=cmp_to_key(comp_hands)))
    total_winnings = sum((i+1) * bid for i, bid in enumerate(sorted_hand_to_bids.values()))
    print(total_winnings)

    # Part 2
    comp_hands = partial(compare_hands, hand_scores=hand_scores_p2, card_strength=card_strength_p2)
    sorted_hand_to_bids = dict(sorted(hands_to_bids.items(), key=cmp_to_key(comp_hands)))
    total_winnings = sum((i+1) * bid for i, bid in enumerate(sorted_hand_to_bids.values()))
    print(total_winnings)

main()
