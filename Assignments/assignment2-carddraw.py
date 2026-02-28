# This program simulates drawing 5 cards from a shuffled deck and checks for pairs, triples, straights, and flushes.
# Author : Joanna Mnich


import requests

# Shuffle a new deck and get deck_id
deck_id = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1").json()['deck_id']

# Draw 5 cards
cards = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2").json()['cards']

print("You drew:")
for c in cards:
    print(f"{c['value']} of {c['suit']}")

# Map card values to numbers
values_order = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,
                '9':9,'10':10,'JACK':11,'QUEEN':12,'KING':13,'ACE':14}

vals = [values_order[c['value']] for c in cards]
suits = [c['suit'] for c in cards]

# Check combinations
pair = any(vals.count(v) == 2 for v in vals)
triple = any(vals.count(v) == 3 for v in vals)
flush = len(set(suits)) == 1
straight = sorted(vals)
straight = all(straight[i+1]-straight[i]==1 for i in range(len(straight)-1))

# Congratulate user
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
