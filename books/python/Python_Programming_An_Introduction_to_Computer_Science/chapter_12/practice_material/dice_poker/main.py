from dice import Dice
from poker_app import PokerApp
from poker_interface import TextInterface

def main():
    # d = Dice()
    # d.values()
    # print(d.values())
    inter = TextInterface()
    app = PokerApp(inter)
    app.run()

if __name__ == "__main__":
    main()