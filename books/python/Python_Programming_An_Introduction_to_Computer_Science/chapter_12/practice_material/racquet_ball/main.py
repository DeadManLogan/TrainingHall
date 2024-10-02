class RBallGame:
    def play():
        return
    
    def get_scores(self):
        return

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
    
def get_inputs():
    return

def main():
    probA, probB, n = get_inputs()

    stats = SimStats()
    for (i) in range(n):
        the_game = RBallGame(probA, probB)
        the_game.play()
        stats.update(the_game)

    stats.print_report()