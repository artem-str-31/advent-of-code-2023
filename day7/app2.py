from collections import Counter

file_name = 'input.txt'
file = open(file_name, 'r')


cards = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
bids = {}
map = {}
collections = [[] for _ in range(7)]
merged = []
total = 0


def most_common(input_string):
    char_counts = Counter(input_string)
    max_count = max(char_counts.values())
    most_common_chars = [char for char, count in char_counts.items() if count == max_count]
    sorted_chars = sorted(most_common_chars, key=lambda char: cards.get(char, 0), reverse=True)
    if sorted_chars[0] != 'J':
        return sorted_chars[0]
    if len(sorted_chars) > 1:
        return sorted_chars[1]
    return sorted_chars[0]


for line in file.readlines():
    record = line.split()
    key = record[0].replace('J', most_common(record[0]))
    map[key] = record[0]
    bids[record[0]] = int(record[1])


def is_five_of_a_kind(hand):
    hand = sorted(hand)
    return hand[0] == hand[4]


def is_four_of_a_kind(hand):
    hand = sorted(hand)
    return hand[0] == hand[3] or hand[1] == hand[4]


def is_full_house(hand):
    hand = sorted(hand)
    return (hand[0] == hand[2] and hand[3] == hand[4]) or (hand[0] == hand[1] and hand[2] == hand[4])


def is_three_of_a_kind(hand):
    hand = sorted(hand)
    return hand[0] == hand[2] or hand[1] == hand[3] or hand[2] == hand[4]


def is_two_pair(hand):
    hand = sorted(hand)
    return (hand[0] == hand[1] and hand[2] == hand[3]) or (hand[1] == hand[2] and hand[3] == hand[4]) or (hand[0] == hand[1] and hand[3] == hand[4])


def is_pair(hand):
    hand = sorted(hand)
    return hand[0] == hand[1] or hand[1] == hand[2] or hand[2] == hand[3] or hand[3] == hand[4]


def hand_value(hand):
    return [cards[card] for card in hand]


for hand in map.keys():
    if is_five_of_a_kind(hand):
        collections[6].append(hand)
    elif is_four_of_a_kind(hand):
        collections[5].append(hand)
    elif is_full_house(hand):
        collections[4].append(hand)
    elif is_three_of_a_kind(hand):
        collections[3].append(hand)
    elif is_two_pair(hand):
        collections[2].append(hand)
    elif is_pair(hand):
        collections[1].append(hand)
    else:
        collections[0].append(hand)



for i, hand in enumerate(merged):
    merged[i] = map[hand]


for j, collection in enumerate(collections):
    for i, hand in enumerate(collection):
        collections[j][i] = map[collections[j][i]]
    merged = merged + sorted(collection, key=hand_value)




n = len(merged)


for i in range(n):
    print(f'{merged[i]}: {bids[merged[i]]} * {(i+1)}')
    total += bids[merged[i]] * (i+1)


print(total)
file.close()
