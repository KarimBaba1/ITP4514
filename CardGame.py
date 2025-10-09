import random
import pandas as pd

#  suits and ranks
suits = ["Spade", "Heart", "Club", "Diamond"]
ranks = ["Ace"] + [f"{i:02d}" for i in range(2, 11)] + ["Jack", "Queen", "King"]

deck = [(suit, rank) for suit in suits for rank in ranks]

random.shuffle(deck)

while True:
    num_players = int(input("How many players? "))
    cards_per_player = int(input("How many cards for each player? "))

    if num_players * cards_per_player > len(deck):
        print("Incorrect input, please input again!")
    else:
        break

for player in range(1, num_players + 1):
    hand = deck[(player - 1) * cards_per_player : player * cards_per_player]

    df = pd.DataFrame(hand, columns=["suit", "number"])

    print(f"\nPlayer {player}'s hand:")
    print(df)

