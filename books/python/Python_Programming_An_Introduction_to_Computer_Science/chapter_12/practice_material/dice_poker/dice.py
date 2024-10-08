from random import randrange

class Dice:
    def __init__(self):
        self.dice = [0]*5
        self.roll_all()

    def roll(self, which):
        for pos in which:
            self.dice[pos] = randrange(1, 7)

    def roll_all(self):
        self.roll(range(5))

    def values(self):
        return self.dice[:]
    
    def score(self):
        counts = [0]*7
        for value in self.dice:
            counts[value] = counts[value] + 1

        if 5 in counts:
            return "Five of a kind", 30
        elif 4 in counts:
            return "Four of a kind", 15
        elif (3 in counts) and (2 in counts):
            return "Full House", 12
        elif 3 in counts:
            return "Three of a kind", 8
        elif not (2 in counts) and (counts[0]==0 or counts[6]==0):
            return "Straight", 20
        elif counts.count(2)==2:
            return "Two Pairs", 5
        else:
            return "Garbage", 0