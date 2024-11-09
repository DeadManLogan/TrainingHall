from random import *

class RBallGame:
    def __init__(self,probA, probB):
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.server = self.playerA

    def play(self):
        while not self.is_over():
            if self.server.wins_serve():
                self.server.increase_score()
            else:
                self.change_server()
    
    def get_scores(self):
        return self.playerA.get_score(), self.playerB.get_score()
    
    def is_over(self):
        a, b = self.get_scores()
        return a == 15 or b == 15 or \
            (a == 7 and b == 0) or (b == 7 and a == 0)
    
    def change_server(self):
        if self.server == self.playerA:
            self.server = self.playerB
        else:
            self.server = self.playerA


class SimStats:
    def __init__(self):
        self.winsA = 0
        self.winsB = 0
        self.shutoutsA = 0
        self.shutoutsB = 0

    def update(self, game):
        scoreA, scoreB = game.get_scores()
        if scoreA > scoreB:
            self.winsA += 1
            if scoreB == 0:
                self.shutoutsA += 1
        else:
            self.winsB += 1
            if scoreA == 0:
                self.shutoutsB += 1

    def print_line(self, label, wins, shuts, ngames):
        template = "Player {0}:{1:5} ({2:5.1%}) {3:11}      ({4})"
        if wins == 0:
            shut_str = "----"
        else:
            shut_str = "{0:4.1%}".format(float(shuts)/wins)
        print(template.format(label, wins, float(wins)/ngames, shuts, shut_str))
    
    def print_report(self):
        ngames = self.winsA + self.winsB
        print(f"Summary of {ngames} games: \n")
        print("     wins (%total)   shutouts (%wins)    ")
        print("---------------------------------------")
        self.print_line("A", self.winsA, self.shutoutsA, ngames)
        self.print_line("A", self.winsB, self.shutoutsB, ngames)

class Player:
    def __init__(self, prob):
        self.prob = prob
        self.score = 0

    def wins_serve(self):
        return random() < self.prob
    
    def increase_score(self):
        self.score += 1

    def get_score(self):
        return self.score
    
def get_inputs():
    a = float(input("Player A probability: "))
    b = float(input("Player B probability: "))
    n = int(input("Number of games: "))
    return a, b, n

def main():
    probA, probB, n = get_inputs()

    stats = SimStats()
    for (i) in range(n):
        the_game = RBallGame(probA, probB)
        the_game.play()
        stats.update(the_game)

    stats.print_report()

if __name__ == "__main__":
    main()