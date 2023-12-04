
def main():
    with open('input', 'r') as f:
        lines = [line.strip() for line in f]
    
    # Part 1
    total = 0
    for line in lines:
        line = line.split(':')[1]
        left, right = line.split('|')
        winning_cards = set(int(val.strip()) for val in left.split()) & set(int(val.strip()) for val in right.split())
        if not winning_cards:
            continue

        total += 2 ** (len(winning_cards) - 1)
    print(total)

    # Part 2
    card_totals = [1] * len(lines)
    for line in lines:
        card, line = line.split(':')
        card = int(card.strip(':').split()[1])
        left, right = line.split('|')
        winning_cards = set(int(val.strip()) for val in left.split()) & set(int(val.strip()) for val in right.split())
        if not winning_cards:
            continue

        for i in range(len(winning_cards)):
            card_totals[card+i] += card_totals[card-1]
        
    total = sum(card_totals)
    print(total)


main()
