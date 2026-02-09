import requests

# 1️⃣ Shuffle a new deck
shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(shuffle_url)
data = response.json()
deck_id = data['deck_id']

# 2️⃣ Draw 5 cards
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
response = requests.get(draw_url)
cards_data = response.json()['cards']

# 3️⃣ Print value and suit of each card
print("You drew:")
for card in cards_data:
    print(f"{card['value']} of {card['suit']}")

# 4️⃣ Check for pairs, triples, straights, flush
values_order = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,
                '9':9,'10':10,'JACK':11,'QUEEN':12,'KING':13,'ACE':14}

# Count values and suits
value_counts = {}
suit_counts = {}
card_values = []

for card in cards_data:
    val = card['value']
    suit = card['suit']
    card_values.append(values_order[val])
    value_counts[val] = value_counts.get(val,0)+1
    suit_counts[suit] = suit_counts.get(suit,0)+1

# Check pairs/triples
pair = triple = False
for count in value_counts.values():
    if count == 2:
        pair = True
    if count == 3:
        triple = True

# Check flush (all same suit)
flush = any(count == 5 for count in suit_counts.values())

# Check straight
card_values_sorted = sorted(card_values)
straight = all(card_values_sorted[i+1]-card_values_sorted[i]==1 for i in range(4))

# 5️⃣ Congratulate user
if flush:
    print("\nCongratulations! You got a flush (all same suit)!")
elif straight:
    print("\nCongratulations! You got a straight!")
elif triple:
    print("\nCongratulations! You got a triple!")
elif pair:
    print("\nCongratulations! You got a pair!")
else:
    print("\nNo special combinations this time. Try again!")
