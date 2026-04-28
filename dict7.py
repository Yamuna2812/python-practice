votes = {"A": 2, "B": 3, "C": 1}

winner = max(votes, key=votes.get)
print("Winner:", winner)