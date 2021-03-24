deck_of_cards = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 14
}
input_cards = []
for _ in range(6):
    input_cards.append(input())

avg_rank = sum(deck_of_cards.get(key) for key in input_cards) / 6
print(avg_rank)
